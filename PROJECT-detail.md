# PROJECT-detail.md — Personalized Nutrition & Meal Plan (Idea 55)

## Executive Summary
A safety-gated harness that profiles a user, screens for medical red flags, and (only if safe) builds an evidence-based meal plan scored against named nutrition frameworks, with an improvement roadmap. Educational, not medical advice.

## Problem Statement
People follow generic or unsafe diets. This skill provides individualized, evidence-graded nutrition planning with mandatory safety screening and clear referral when professional care is needed.

## Target Users & Use Cases
- **Weight management:** "Lose fat, keep muscle" → calorie/protein targets + meal plan.
- **Muscle gain:** "Bulk cleanly" → surplus + protein distribution.
- **Condition-aware:** "I have type 2 diabetes" → screen → refer + general carb-quality guidance (educational).

## Harness Architecture
```
/personalized-nutrition-meal-plan
  → sub-profile-intake     (goal, anthropometrics, conditions)  [gate: inputs complete]
  → sub-safety-screener    (MANDATORY red-flag screen)          [gate: passed OR referred out]
  → [main] research        (current guidelines)                 [gate: cited]
  → sub-scoring-engine     (adequacy + goal-fit)                [gate: each nutrient vs DRI]
  → sub-improvement-roadmap (meal plan + actions)               [gate: effort/impact + disclaimer]
  → [main] synthesize + disclaimer
```

## Full Sub-Skill Catalog
| Sub-skill | Purpose | Inputs | Outputs | Tools | Gate |
|-----------|---------|--------|---------|-------|------|
| sub-profile-intake | Profile user | goal, anthropometrics, prefs | profile | Read | TDEE inputs present |
| sub-safety-screener | Screen red flags | profile, conditions | safe/refer verdict | Read | Runs before any guidance |
| sub-scoring-engine | Score adequacy | plan, DRIs | nutrient score | Read | Each macro/micro vs DRI |
| sub-improvement-roadmap | Plan + improve | scores | meal plan + actions | Write | Disclaimer + effort/impact |

## Skill File Format Specification
Per Claude skill standard; see skills/main.md.

## E2E Execution Flow
1. Intake: goal, age, sex, height, weight, activity, allergies, conditions, preferences. 2. Safety screener: BMI extremes, ED indicators, pregnancy/lactation, chronic disease, drug-nutrient interactions → refer to professional where indicated; never produce restrictive plans for ED-risk users. 3. Research current DRI/guideline values. 4. Compute TDEE (Mifflin-St Jeor), set deficit/surplus, protein g/kg; score plan adequacy vs DRI. 5. Build a sample day/week plan + improvement roadmap. 6. Render with disclaimer.
Error handling: red flag → stop + refer; vegan/allergy → adapt; offline → use brain + flag.

## SECOND-KNOWLEDGE-BRAIN Integration
Sources: PubMed, Cochrane, USDA/NIH DRI, WHO, EFSA. Weekly append, evidence-tier ranked.

## Supporting Tools Spec
`knowledge_updater.py`: queries on nutrition RCTs/guidelines; weekly cron; dedupe by hash.

## Quality Gates
- Safety screen completed before any plan; red flags trigger referral.
- Each macro/micro compared to DRI/RDA with a source.
- Educational disclaimer present.
- Evidence hierarchy applied (systematic review > RCT > observational).
- Offline flagged.

## Test Scenarios (summary)
1. Fat-loss recomposition. 2. Muscle gain. 3. ED-risk indicators (refer, no restrictive plan). 4. Pregnancy (refer + general). 5. Nut allergy adaptation. (Full set in tests/.)

## Key Design Decisions
1. Safety screen is mandatory and first. 2. No restrictive plans for ED-risk users. 3. TDEE via Mifflin-St Jeor. 4. Adequacy scored vs DRI. 5. Always educational + referral framing.
