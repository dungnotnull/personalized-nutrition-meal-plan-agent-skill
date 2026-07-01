# CLAUDE.md — Personalized Nutrition & Meal Plan Skill (Idea 55)

**Skill name:** `personalized-nutrition-meal-plan`
**Tagline:** Goal-based meal plan graded against evidence-based nutrition frameworks — safety-gated.
**Current phase:** Scaffold complete (Phases 0–5).
**Source idea:** 55 — *Build & evaluate a personalized nutrition plan/menu by health goal (weight loss, muscle gain, specific conditions), grounded in world-renowned nutrition methods, with improvement recommendations; continuously crawl papers/docs to stay current.*
**Cluster:** `health-wellness` — **SAFETY-GATED: `sub-safety-screener` runs before any guidance.**

## Problem This Skill Solves
Fad diets ignore individual needs and medical safety. This skill profiles the user, screens for red-flag conditions (eating disorders, pregnancy, chronic disease, allergies), and — only if safe — builds an evidence-based plan scored against named frameworks (DRI/RDA, USDA MyPlate, Mediterranean/DASH, Harris-Benedict/Mifflin-St Jeor TDEE, protein-per-kg targets) with an improvement roadmap. **Educational; not a substitute for a registered dietitian or physician.**

## Harness Flow Summary
1. **Intake** (`sub-profile-intake`) — goal, anthropometrics, activity, preferences, conditions.
2. **Safety screen** (`sub-safety-screener`) — MANDATORY before guidance; refer out on red flags.
3. **Research** (main) — verify current guidelines vs SECOND-KNOWLEDGE-BRAIN.md.
4. **Scoring** (`sub-scoring-engine`) — nutritional adequacy & goal-fit score.
5. **Roadmap** (`sub-improvement-roadmap`) — meal plan + improvement actions.

## Sub-skills
- `sub-profile-intake.md` · `sub-safety-screener.md` · `sub-scoring-engine.md` · `sub-improvement-roadmap.md`

## Tools Required
WebSearch, WebFetch, Read, Write, Bash.

## Knowledge Sources
PubMed, Cochrane, USDA/NIH DRI, WHO nutrition, Academy of Nutrition & Dietetics, EFSA.

## Supporting Python Tools
`tools/knowledge_updater.py` — crawl → SECOND-KNOWLEDGE-BRAIN.md.

## Active Development Tasks
- [x] Scaffold deliverables.
- [ ] Expand condition-specific guardrails.

## Reference Docs
PROJECT-detail.md · PROJECT-DEVELOPMENT-PHASE-TRACKING.md · SECOND-KNOWLEDGE-BRAIN.md
