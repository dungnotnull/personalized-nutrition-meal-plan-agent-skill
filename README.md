# Personalized Nutrition & Meal Plan

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-green.svg)](https://github.com/yourusername/personalized-nutrition-meal-plan)
[![Safety: Gated](https://img.shields.io/badge/Safety-Medical%20Gated-red.svg)](./skills/sub-safety-screener.md)

> Build and grade goal-based personalized meal plans against evidence-based nutrition frameworks (DRI, Mediterranean/DASH, TDEE, protein targets) with a mandatory safety screen.

**Educational purpose only — not a substitute for professional medical advice.**

---

## 🎯 What It Does

This AI skill generates personalized nutrition plans by:

1. **Profiling** — Collects anthropometrics, goals, activity, conditions, allergies, preferences
2. **Screening** — MANDATORY medical/red-flag check (eating disorders, pregnancy, chronic disease)
3. **Researching** — Evidence-based framework comparison (DRI, MyPlate, Mediterranean, DASH)
4. **Scoring** — TDEE calculation, macro/micro adequacy, diet-quality pattern alignment
5. **Planning** — Sample meal plans + prioritized improvement actions

### Key Features

| Feature | Description |
|---------|-------------|
| **Safety-First** | Mandatory medical screening with referral protocols |
| **Evidence-Based** | 7 frameworks (DRI/RDA, MyPlate, Mediterranean, DASH, etc.) |
| **Transparent** | All calculations shown with citations |
| **Actionable** | Improvement actions tagged by effort/impact/evidence |
| **Offline-Capable** | Knowledge brain + degraded mode operation |
| **Auto-Updating** | Weekly PubMed/Cochrane/NIH crawling pipeline |

---

## ⚠️ Important Disclaimers

### Medical Disclaimer
This skill provides **educational nutrition information only**. It is **not medical advice**. Always consult with qualified healthcare professionals (registered dietitian, physician) before making dietary changes, especially if you have medical conditions.

### Crisis Resources
If you are experiencing a medical emergency or mental health crisis:
- **US**: 988 (Crisis Lifeline) or 911 (Emergency)
- **NEDA Helpline**: 1-800-931-2237 (nationaleatingdisorders.org)
- **International**: Contact local emergency services

### Scope
- ✅ General healthy eating guidance
- ✅ Educational meal planning
- ❌ Medical nutrition therapy (refers to RD)
- ❌ Eating disorder treatment (refers to specialist)
- ❌ Pregnancy-specific weight management (refers to OB/RD)

---

## 🚀 Quick Start

### Installation

1. **Clone or download** this repository
2. **Ensure dependencies** (optional, for knowledge updater):
   ```bash
   pip install requests beautifulsoup4
   pip install crawl4ai  # Optional, for enhanced crawling
   ```

### Usage with Claude Code

1. **Place the skill** in your skills directory:
   ```
   ~/.claude/skills/personalized-nutrition-meal-plan/
   ```

2. **Invoke the skill** in Claude Code:
   ```
   Create a personalized nutrition plan for me
   ```

3. **Follow the intake process** — answer questions about:
   - Your goals (weight loss, muscle gain, maintenance)
   - Anthropometrics (age, sex, height, weight)
   - Activity level and exercise
   - Medical conditions and medications
   - Allergies and dietary restrictions
   - Food preferences and constraints

### Manual Usage

1. Review `skills/main.md` for the full workflow
2. Follow sub-skills sequentially:
   - `sub-profile-intake.md` — collect user data
   - `sub-safety-screener.md` — safety screen (MANDATORY)
   - `sub-scoring-engine.md` — calculate needs and score
   - `sub-improvement-roadmap.md` — generate plan

---

## 📁 Project Structure

```
personalized-nutrition-meal-plan/
├── skills/                          # AI skill definitions
│   ├── main.md                      # Main harness (orchestrates workflow)
│   ├── sub-profile-intake.md        # User data collection
│   ├── sub-safety-screener.md       # MANDATORY medical screening
│   ├── sub-scoring-engine.md        # TDEE & nutritional scoring
│   └── sub-improvement-roadmap.md   # Meal planning & actions
├── tools/
│   └── knowledge_updater.py         # Evidence crawler & updater
├── tests/
│   └── test-scenarios.md            # Comprehensive test scenarios
├── SECOND-KNOWLEDGE-BRAIN.md         # Evidence database (auto-updated)
├── PROJECT-detail.md                # Project documentation
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Development tracking
├── CLAUDE.md                        # Claude Code integration
├── README.md                        # This file
├── LICENSE                          # MIT License + health disclaimer
├── CONTRIBUTING.md                  # Contribution guidelines
└── CODE_OF_CONDUCT.md               # Community standards
```

---

## 🔬 Evidence-Based Frameworks

### Supported Frameworks (7)

| Framework | Source | Used For |
|-----------|--------|----------|
| DRI/RDA | NIH/USDA | Macro & micronutrient targets |
| MyPlate | USDA | Food group balance |
| Mediterranean | PREDIMED RCT | Cardiometabolic health |
| DASH | NHLBI | Blood pressure management |
| Mifflin-St Jeor | Am J Clin Nutr | BMR calculation |
| Harris-Benedict | Am J Clin Nutr | BMR calculation (alternative) |
| Protein Targets | ISSN Position Stand | Muscle optimization |

### Evidence Hierarchy

Systematic review > Meta-analysis > RCT > Cohort > Position stand > Observational

### Knowledge Sources

- PubMed (pubmed.ncbi.nlm.nih.gov)
- Cochrane Library (cochranelibrary.com)
- NIH ODS (ods.od.nih.gov)
- WHO Nutrition (who.int/health-topics/nutrition)
- EFSA (efsa.europa.eu)
- Academy of Nutrition & Dietetics (eatright.org)

---

## 🛡️ Safety Features

### Mandatory Safety Screen (Runs Before Any Plan)

The skill **will not generate restrictive meal plans** for users with:

| Red Flag Category | Examples | Action |
|-------------------|----------|--------|
| Eating Disorder Risk | ED history, restrictive eating, body-image distress | REFER to specialist |
| BMI Safety | BMI <16 (severe), 16-16.5 (underweight) | REFER or CAUTION |
| Pregnancy/Lactation | Currently pregnant, breastfeeding | REFER to OB/RD |
| Chronic Disease | Diabetes T1, CKD, CVD, liver disease | REFER to specialist |
| Medication Interactions | Warfarin, MAOIs, lithium | REFER to provider |
| Severe Allergies | Anaphylaxis, FPIES | REFER to allergist |

### Referral Database

- National Eating Disorders Association (nationaleatingdisorders.org)
- Academy of Nutrition & Dietetics (eatright.org/find-an-expert)
- Condition-specific resources (diabetes, kidney, heart, cancer)
- International resources by country

### Veto Power

The safety screener has **veto power over the entire harness**. If a red flag is detected, the skill halts meal planning and provides only:
- Specific referral resources
- General healthy eating education
- No calorie targets or restrictive plans

---

## 🧪 Testing

### Test Scenarios (6 Comprehensive)

Run through these scenarios to verify behavior:

| Scenario | Description | Expected Outcome |
|----------|-------------|------------------|
| 1 | Fat-loss recomposition | TDEE calculation, deficit, protein targets |
| 2 | Muscle gain | Surplus, high-protein distribution |
| 3 | ED-risk indicators | REFER, no restrictive plan |
| 4 | Pregnancy | REFER, general education only |
| 5 | Nut allergy | Plan excludes nuts, protein maintained |
| 6 | Offline mode | Uses knowledge brain, flags limitation |

See `tests/test-scenarios.md` for full details.

---

## 🔄 Knowledge Updates

### Automated Evidence Crawler

Run the knowledge updater to fetch latest research:

```bash
# Dry run (test without writing)
python tools/knowledge_updater.py --dry-run

# Full update (writes to SECOND-KNOWLEDGE-BRAIN.md)
python tools/knowledge_updater.py

# Specific source only
python tools/knowledge_updater.py --source PubMed

# Verbose logging
python tools/knowledge_updater.py --verbose
```

### Recommended Schedule

- **Weekly**: Run knowledge updater (cron job recommended)
- **Quarterly**: Review and curate entries manually
- **Annually**: Full guideline update check (DRI, Dietary Guidelines)

### Update Sources

- PubMed (nutrition RCTs)
- Cochrane (systematic reviews)
- NIH ODS (fact sheets)
- WHO Nutrition (guidelines)
- EFSA (scientific opinions)
- Academy of Nutrition & Dietetics (position stands)

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Priority Areas

1. **Evidence framework expansion** — Add authoritative sources
2. **Test scenarios** — Additional edge cases and conditions
3. **Internationalization** — Country-specific DRI values and resources
4. **Accessibility** -- Simplified language versions

### Contribution Guidelines

- Follow existing code style and documentation format
- Add evidence citations for any framework changes
- Update test scenarios for new features
- Ensure safety screening is never bypassed
- Include disclaimers in any output

---

## 📜 License

MIT License — See [LICENSE](LICENSE) file.

**Important**: The license includes a health & medical disclaimer that applies to all uses, modifications, and distributions.

---

## 📚 References

### Primary Sources

| Organization | URL | Purpose |
|---------------|-----|---------|
| NIH ODS | ods.od.nih.gov | DRI/RDA values |
| USDA | usda.gov | MyPlate, Dietary Guidelines |
| Cochrane | cochranelibrary.com | Systematic reviews |
| PubMed | pubmed.ncbi.nlm.nih.gov | Research database |
| WHO | who.int | Global nutrition guidelines |
| EFSA | efsa.europa.eu | EU standards |
| ISSN | jissn.com | Sports nutrition positions |

### Key Research

- Mediterranean diet & CVD: Cochrane review, 2019
- Protein intake & resistance training: ISSN position, 2017
- Mifflin-St Jeor validation: Am J Clin Nutr, 1990

---

## 🙏 Acknowledgments

- **Evidence Base**: NIH/USDA, WHO, Cochrane, PubMed
- **Safety Protocols**: National Eating Disorders Association, Academy of Nutrition & Dietetics
- **Community**: Claude Code and AI agent ecosystem

---

## 📞 Support & Questions

### For Users
- Review the comprehensive documentation in `skills/` directory
- Check test scenarios in `tests/test-scenarios.md`
- Consult healthcare professionals for personalized medical advice

### For Contributors
- See [CONTRIBUTING.md](CONTRIBUTING.md)
- Review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- Open an issue for bugs or feature requests

### For Healthcare Professionals
- This tool is designed as educational support, not replacement
- Referral pathways are built into the safety screen
- Suggestions for evidence-based improvements welcome

---

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Last Updated**: 2026-07-01
**Version**: 1.0.0 (Production Ready)
**Status**: ✅ All Phases Complete (0-5)
