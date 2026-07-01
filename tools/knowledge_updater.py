#!/usr/bin/env python3
"""
knowledge_updater.py — Personalized Nutrition & Meal Plan (Idea 55)

Evidence-based nutrition knowledge crawler and updater.
Crawls authoritative sources (PubMed, Cochrane, NIH/ODS, WHO, EFSA),
scores entries by recency, evidence tier, and relevance, appends
deduplicated entries to SECOND-KNOWLEDGE-BRAIN.md.

Usage:
    python knowledge_updater.py [--dry-run] [--verbose] [--source SOURCE]

Schedule: Weekly cron recommended.
Dependencies: crawl4ai (optional; degrades gracefully to requests-only mode)

Author: Claude Code
Version: 1.0.0
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import logging
import pathlib
import re
import sys
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set

# Configuration
BRAIN_FILE = pathlib.Path(__file__).resolve().parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
LOG_FILE = pathlib.Path(__file__).resolve().parent.parent / "logs" / "knowledge_updater.log"
MAX_RETRIES = 3
RETRY_DELAY = 2.0

# Configure logging
LOG_FILE.parent.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


# =============================================================================
# Data Structures
# =============================================================================

@dataclass
class Source:
    """Authoritative nutrition evidence source."""
    name: str
    url: str
    description: str
    search_queries: List[str] = field(default_factory=list)
    weight: float = 1.0  # Source reliability weight


@dataclass
class EvidenceEntry:
    """Single evidence-based nutrition entry."""
    title: str
    source: str
    url: str
    date: str
    tier: str
    relevance_score: float
    content_snippet: str = ""
    hash: str = ""

    def __post_init__(self):
        if not self.hash:
            self.hash = self._compute_hash()

    def _compute_hash(self) -> str:
        """Generate unique hash for deduplication."""
        hash_input = f"{self.url}:{self.title}".lower().encode()
        return hashlib.sha1(hash_input).hexdigest()[:12]

    def to_markdown(self) -> str:
        """Convert to markdown format for knowledge brain."""
        return (
            f"- [{self.date}] ({self.tier}) {self.title} — {self.source} — "
            f"{self.url} <!--h:{self.hash}-->"
        )


# =============================================================================
# Source Definitions
# =============================================================================

SOURCES: List[Source] = [
    Source(
        name="PubMed",
        url="https://pubmed.ncbi.nlm.nih.gov",
        description="US National Library of Medicine biomedical literature database",
        search_queries=[
            "nutrition randomized controlled trial",
            "dietary intervention meta-analysis",
            "protein intake systematic review",
            "micronutrient adequacy cohort"
        ],
        weight=1.0
    ),
    Source(
        name="Cochrane",
        url="https://www.cochranelibrary.com",
        description="Leading source for systematic reviews in healthcare",
        search_queries=[
            "diet nutrition intervention",
            "vitamin mineral supplement",
            "mediterranean diet cardiovascular"
        ],
        weight=1.2  # Systematic reviews weighted higher
    ),
    Source(
        name="NIH ODS",
        url="https://ods.od.nih.gov",
        description="NIH Office of Dietary Supplements - evidence-based fact sheets",
        search_queries=[
            "vitamin fact sheet",
            "mineral health professional",
            "supplement safety"
        ],
        weight=1.1
    ),
    Source(
        name="WHO Nutrition",
        url="https://www.who.int/health-topics/nutrition",
        description="World Health Organization nutrition guidelines",
        search_queries=[
            "dietary guidelines",
            "nutrient requirements",
            "global nutrition strategy"
        ],
        weight=1.0
    ),
    Source(
        name="EFSA",
        url="https://www.efsa.europa.eu/en/topics/nutrition",
        description="European Food Safety Authority scientific opinions",
        search_queries=[
            "dietary reference values",
            "nutrition claims",
            "micronutrient requirements"
        ],
        weight=1.0
    ),
    Source(
        name="Academy of Nutrition & Dietetics",
        url="https://www.eatright.org",
        description="Evidence analysis library from nutrition professionals",
        search_queries=[
            "evidence analysis nutrition",
            "position stand",
            "nutrition practice guidelines"
        ],
        weight=0.9
    )
]

# Evidence tier hierarchy (highest to lowest)
EVIDENCE_TIERS = [
    ("systematic review", "Systematic Review"),
    ("meta-analysis", "Meta-Analysis"),
    ("randomized", "Randomized Controlled Trial"),
    ("rct", "Randomized Controlled Trial"),
    ("cohort", "Cohort Study"),
    ("case-control", "Case-Control Study"),
    ("position stand", "Position Stand"),
    ("guideline", "Practice Guideline"),
    ("observational", "Observational Study"),
]

# Keywords for relevance scoring
RELEVANCE_KEYWORDS = [
    "nutrition", "diet", "protein", "carbohydrate", "fat", "micronutrient",
    "vitamin", "mineral", "fiber", "omega-3", "antioxidant", "calorie",
    "energy", "metabolism", "mediterranean", "dash", "intervention",
    "adequacy", "deficiency", "supplement", "food", "meal", "intake",
    "requirement", "recommendation", "guideline", "dri", "rda"
]


# =============================================================================
# Core Functions
# =============================================================================

def determine_evidence_tier(title: str, content: str = "") -> str:
    """
    Determine evidence tier from title and content.

    Args:
        title: Entry title or headline
        content: Optional content/body text for additional context

    Returns:
        Evidence tier label (e.g., "Systematic Review")
    """
    combined = (title + " " + content).lower()

    for pattern, label in EVIDENCE_TIERS:
        if pattern in combined:
            return label

    return "Other"


def calculate_relevance_score(title: str, content: str = "", source_weight: float = 1.0) -> float:
    """
    Calculate relevance score based on keywords and source.

    Args:
        title: Entry title
        content: Optional content text
        source_weight: Reliability weight of the source

    Returns:
        Relevance score (higher = more relevant)
    """
    combined = (title + " " + content).lower()

    # Count keyword matches
    keyword_count = sum(1 for kw in RELEVANCE_KEYWORDS if kw in combined)

    # Tier bonus (higher tiers get bonus)
    tier = determine_evidence_tier(title, content)
    tier_bonus = {
        "Systematic Review": 5.0,
        "Meta-Analysis": 4.5,
        "Randomized Controlled Trial": 4.0,
        "Cohort Study": 2.0,
        "Position Stand": 3.0,
        "Practice Guideline": 3.5,
    }.get(tier, 0.0)

    # Calculate score
    score = (keyword_count * 1.0) + tier_bonus
    score *= source_weight

    return round(score, 2)


def fetch_with_crawl4ai(url: str, max_retries: int = MAX_RETRIES) -> str:
    """
    Fetch content using crawl4ai WebCrawler.

    Args:
        url: URL to fetch
        max_retries: Maximum number of retry attempts

    Returns:
        Extracted markdown text
    """
    for attempt in range(max_retries):
        try:
            from crawl4ai import WebCrawler

            logger.info(f"Crawl4AI: Fetching {url} (attempt {attempt + 1})")
            crawler = WebCrawler(verbose=False)
            crawler.warmup()

            result = crawler.run(url=url)
            markdown = getattr(result, "markdown", "") or ""

            if markdown:
                logger.info(f"Crawl4AI: Successfully fetched {len(markdown)} chars from {url}")
                return markdown
            else:
                logger.warning(f"Crawl4AI: No markdown extracted from {url}")

        except ImportError:
            logger.warning("Crawl4AI not installed, falling back to requests")
            return fetch_with_requests(url, max_retries)
        except Exception as e:
            logger.error(f"Crawl4AI: Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY)

    return ""


def fetch_with_requests(url: str, max_retries: int = MAX_RETRIES) -> str:
    """
    Fetch content using requests library (fallback method).

    Args:
        url: URL to fetch
        max_retries: Maximum retry attempts

    Returns:
        Extracted text content
    """
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        logger.error("requests and beautifulsoup4 required for fallback fetch")
        return ""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for attempt in range(max_retries):
        try:
            logger.info(f"Requests: Fetching {url} (attempt {attempt + 1})")
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()

            # Get text
            text = soup.get_text(separator='\n', strip=True)

            # Clean up excessive whitespace
            text = re.sub(r'\n{3,}', '\n\n', text)

            logger.info(f"Requests: Successfully fetched {len(text)} chars from {url}")
            return text

        except Exception as e:
            logger.error(f"Requests: Attempt {attempt + 1} failed for {url}: {e}")
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY)

    return ""


def extract_entries_from_source(source: Source, verbose: bool = False) -> List[EvidenceEntry]:
    """
    Extract evidence entries from a source.

    Args:
        source: Source configuration
        verbose: Enable detailed logging

    Returns:
        List of evidence entries
    """
    entries = []

    # Use source's main URL
    content = fetch_with_crawl4ai(source.url) or fetch_with_requests(source.url)

    if not content:
        logger.warning(f"No content retrieved from {source.name}")
        return entries

    # Split content into potential entries
    lines = content.split('\n')
    current_entry_lines = []

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            if current_entry_lines:
                entry_text = ' '.join(current_entry_lines)
                if 50 < len(entry_text) < 500:  # Reasonable entry length
                    entry = create_entry_from_text(entry_text, source)
                    if entry:
                        entries.append(entry)
                current_entry_lines = []
            continue

        # Skip non-content lines
        if line.startswith(('<!--', 'Copyright', 'All rights reserved')):
            continue

        # Check if line looks like a title/heading
        if len(line) < 200 and any(char.isalpha() for char in line):
            # If we have accumulated lines, process them
            if current_entry_lines:
                entry_text = ' '.join(current_entry_lines)
                if 50 < len(entry_text) < 500:
                    entry = create_entry_from_text(entry_text, source)
                    if entry:
                        entries.append(entry)
                current_entry_lines = []

            current_entry_lines = [line]
        else:
            if current_entry_lines:
                current_entry_lines.append(line)

    # Process final entry
    if current_entry_lines:
        entry_text = ' '.join(current_entry_lines)
        if 50 < len(entry_text) < 500:
            entry = create_entry_from_text(entry_text, source)
            if entry:
                entries.append(entry)

    if verbose:
        logger.info(f"Extracted {len(entries)} entries from {source.name}")

    return entries


def create_entry_from_text(text: str, source: Source) -> Optional[EvidenceEntry]:
    """
    Create an EvidenceEntry from text if it meets relevance criteria.

    Args:
        text: Entry text
        source: Source configuration

    Returns:
        EvidenceEntry or None if not relevant
    """
    # Check minimum relevance
    combined = text.lower()
    if not any(kw in combined for kw in RELEVANCE_KEYWORDS):
        return None

    # Extract URL if present
    url_match = re.search(r'https?://[^\s<>"{}|\\^`[\]]+', text)
    url = url_match.group(0) if url_match else source.url

    # Clean up title (first sentence or first 100 chars)
    title = text.split('.')[0].strip()[:200]

    # Determine tier and score
    tier = determine_evidence_tier(text)
    score = calculate_relevance_score(text, "", source.weight)

    # Only include if score meets threshold
    if score < 2.0:
        return None

    return EvidenceEntry(
        title=title,
        source=source.name,
        url=url,
        date=dt.date.today().isoformat(),
        tier=tier,
        relevance_score=score,
        content_snippet=text[:500]
    )


def get_existing_hashes(brain_path: pathlib.Path) -> Set[str]:
    """
    Extract all existing entry hashes from knowledge brain.

    Args:
        brain_path: Path to SECOND-KNOWLEDGE-BRAIN.md

    Returns:
        Set of existing hashes
    """
    if not brain_path.exists():
        return set()

    content = brain_path.read_text(encoding='utf-8')
    hashes = set(re.findall(r'<!--h:([0-9a-f]{12})-->', content))

    logger.info(f"Found {len(hashes)} existing entries in knowledge brain")
    return hashes


def append_new_entries(entries: List[EvidenceEntry], brain_path: pathlib.Path,
                      dry_run: bool = False) -> int:
    """
    Append new entries to knowledge brain (deduplicated).

    Args:
        entries: List of evidence entries
        brain_path: Path to SECOND-KNOWLEDGE-BRAIN.md
        dry_run: If True, print but don't write

    Returns:
        Number of entries added
    """
    existing_hashes = get_existing_hashes(brain_path)
    new_entries = [e for e in entries if e.hash not in existing_hashes]

    if not new_entries:
        logger.info("No new entries to add")
        return 0

    # Sort by relevance score
    new_entries.sort(key=lambda e: e.relevance_score, reverse=True)

    # Create markdown block
    today = dt.date.today().isoformat()
    lines = [
        f"\n### Auto-update {today}",
        f"*Source crawl via knowledge_updater.py*",
        ""
    ]

    for entry in new_entries:
        lines.append(entry.to_markdown())

    block = "\n".join(lines) + "\n"

    if dry_run:
        print("\n=== DRY RUN OUTPUT ===")
        print(block)
        print("=== END DRY RUN ===")
        logger.info(f"Dry run: Would add {len(new_entries)} entries")
    else:
        with brain_path.open('a', encoding='utf-8') as f:
            f.write(block)
        logger.info(f"Appended {len(new_entries)} entries to {brain_path}")

    return len(new_entries)


def generate_report(entries: List[EvidenceEntry], added_count: int) -> str:
    """
    Generate summary report of update operation.

    Args:
        entries: All entries collected
        added_count: Number of new entries added

    Returns:
        Report text
    """
    # Count by tier
    tier_counts: Dict[str, int] = {}
    for entry in entries:
        tier_counts[entry.tier] = tier_counts.get(entry.tier, 0) + 1

    # Build report
    lines = [
        "",
        "=== KNOWLEDGE UPDATE REPORT ===",
        f"Date: {dt.date.today().isoformat()}",
        f"Total entries collected: {len(entries)}",
        f"New entries added: {added_count}",
        "",
        "Entries by tier:"
    ]

    for tier, count in sorted(tier_counts.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"  {tier}: {count}")

    lines.append("")
    lines.extend(["=== END REPORT ===", ""])

    return "\n".join(lines)


# =============================================================================
# Main Function
# =============================================================================

def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Update nutrition knowledge brain with evidence-based entries"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print entries without writing to file"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    parser.add_argument(
        "--source",
        choices=[s.name for s in SOURCES],
        help="Update from specific source only"
    )
    parser.add_argument(
        "--sources",
        nargs="+",
        choices=[s.name for s in SOURCES],
        help="Update from multiple specific sources"
    )

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    logger.info("Starting knowledge update run")

    # Determine which sources to query
    if args.source:
        target_sources = [s for s in SOURCES if s.name == args.source]
    elif args.sources:
        target_sources = [s for s in SOURCES if s.name in args.sources]
    else:
        target_sources = SOURCES

    logger.info(f"Querying {len(target_sources)} sources: {[s.name for s in target_sources]}")

    # Collect entries from all sources
    all_entries: List[EvidenceEntry] = []

    for source in target_sources:
        try:
            entries = extract_entries_from_source(source, args.verbose)
            all_entries.extend(entries)
            logger.info(f"Collected {len(entries)} entries from {source.name}")
        except Exception as e:
            logger.error(f"Failed to process {source.name}: {e}")

    # Append new entries
    added_count = append_new_entries(all_entries, BRAIN_FILE, args.dry_run)

    # Generate and print report
    report = generate_report(all_entries, added_count)
    print(report)

    logger.info("Knowledge update run complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
