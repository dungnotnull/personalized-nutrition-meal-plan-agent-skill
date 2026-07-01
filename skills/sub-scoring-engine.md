---
name: sub-scoring-engine
description: Compute energy needs and score nutritional adequacy of a plan against DRI/RDA and diet-quality patterns.
---

# Scoring Engine Sub-Skill

## Purpose
Quantify how well a nutrition plan meets the user's energy and nutrient needs using evidence-based calculations and framework comparisons. Output enables data-driven meal plan optimization.

## Input: Post-Safety-PASS Profile
```json
{
  "anthropometrics": {"age", "sex", "height_cm", "weight_kg"},
  "goal": {"primary", "timeline"},
  "activity": {"multiplier", "types"},
  "restrictions": {"allergies", "pattern"},
  "preferences": {"likes", "dislikes", "meals_per_day"}
}
```

## Calculations

### 1. Basal Metabolic Rate (BMR)
**Mifflin-St Jeor Equation** (preferred for accuracy):

**For Men**:
```
BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) + 5
```

**For Women**:
```
BMR = (10 × weight_kg) + (6.25 × height_cm) - (5 × age) - 161
```

**Example Calculation** (30M, 85kg, 180cm):
```
BMR = (10 × 85) + (6.25 × 180) - (5 × 30) + 5
BMR = 850 + 1125 - 150 + 5 = 1,830 kcal/day
```

**Alternative: Harris-Benedict (Revised 1984)** (if Mifflin unavailable):
```
Men: BMR = 88.4 + (13.4 × kg) + (4.8 × cm) - (5.68 × age)
Women: BMR = 447.6 + (9.25 × kg) + (3.10 × cm) - (4.33 × age)
```

**Quality Note**: Mifflin-St Jeor validated within 10% of indirect calorimetry for most adults. May underestimate in very lean individuals and overestimate in obese.

### 2. Total Daily Energy (TDEE)
**Activity Multipliers**:
| Level | Multiplier | Description | Example |
|-------|------------|-------------|----------|
| Sedentary | 1.2 | Desk job, no exercise | Office worker |
| Light | 1.375 | Light exercise 1-3 days | Walking 30 min, 3×/week |
| Moderate | 1.55 | Moderate exercise 3-5 days | Gym 45 min, 4×/week |
| Active | 1.725 | Hard exercise 6-7 days | Training 1 hr daily |
| Elite | 1.9 | Very hard, physical job, 2×/day | Athlete, construction |

**Calculation**: TDEE = BMR × Activity Multiplier

**Example** (BMR 1,830, Moderate activity 1.55):
```
TDEE = 1,830 × 1.55 = 2,837 kcal/day
```

### 3. Energy Target by Goal
**Goal Adjustments**:
| Goal | Adjustment | Calculation | Rationale |
|------|------------|-------------|-----------|
| Weight Loss | -10% to -20% | TDEE × 0.80-0.90 | Sustainable deficit |
| Aggressive Loss | -25% max | TDEE × 0.75 | Only under professional supervision |
| Muscle Gain | +5% to +15% | TDEE × 1.05-1.15 | Supports growth without excess fat |
| Maintenance | 0% | TDEE | Maintain current weight |
| Health Management | Variable | Per condition | Disease-specific targets |

**Safe Floor**:
- Minimum intake ≥ BMR × 1.2 for sedentary
- Never below 1,200 kcal for average adult (female) or 1,500 kcal (male)
- Adjust downward for very short individuals, upward for tall

**Example** (Weight loss, TDEE 2,837):
```
Target range: 2,837 × 0.80 to 2,837 × 0.90
Target: 2,270 - 2,553 kcal/day
Selected: 2,400 kcal/day (~15% deficit)
```

### 4. Protein Target
**ISSN Position Stand Guidelines**:

| Goal | Target | Timing |
|------|--------|--------|
| Maintenance | 1.2-1.6 g/kg | Even distribution |
| Muscle Gain | 1.6-2.2 g/kg | 4+ doses, post-exercise |
| Fat Loss | 1.8-2.4 g/kg | Higher to preserve lean mass |
| Endurance Athlete | 1.4-1.6 g/kg | Recovery focus |
| Elderly | 1.2-1.5 g/kg | Sarcopenia prevention |

**Example Calculation** (85kg, muscle gain):
```
Target: 1.6-2.2 g/kg × 85kg = 136-187 g/day
Selected: 160 g/day (~1.9 g/kg)
```

**Distribution**: 4+ meals, 0.4-0.55 g/kg per meal for optimal MPS (muscle protein synthesis)

### 5. Carbohydrate & Fat Targets
**Carbohydrate**:
- Minimum: 130 g/day (brain glucose requirement, RDA)
- General: 45-65% of calories (DRI guideline)
- Athletes: 3-7 g/kg depending on training volume
- Low-carb: >50 g/day to prevent ketoacidosis risk (unless therapeutic keto)

**Fat**:
- Minimum: 20-35% of calories (AMDR)
- Essential fatty acids: Linoleic acid 17 g/day (M), 12 g/day (F); Alpha-linolenic 1.6 g/day (M), 1.1 g/day (F)
- Saturated fat: <10% of calories (DGA recommendation)

**Example** (2,400 kcal target):
```
Protein: 160 g × 4 kcal/g = 640 kcal (27%)
Carbohydrate: 250 g × 4 kcal/g = 1,000 kcal (42%)
Fat: 85 g × 9 kcal/g = 765 kcal (31%)
Total: 2,405 kcal
```

## Micronutrient Targets (Key Nutrients)

### DRI/RDA Reference Values (Adults)
| Nutrient | RDA (M) | RDA (F) | UL | Common Gaps |
|----------|---------|---------|-----|-------------|
| Vitamin D | 15 µg (600 IU) | 15 µg (600 IU) | 100 µg | Widespread insufficiency |
| Calcium | 1,000 mg | 1,200 mg (51+) | 2,500 mg | Dairy avoidance |
| Iron | 8 mg | 18 mg (19-50), 8 mg (51+) | 45 mg | Menstruating women |
| Vitamin B12 | 2.4 µg | 2.4 µg | Not established | Vegan/vegetarian |
| Folate | 400 µg DFE | 400 µg DFE | 1,000 µg | Pregnancy critical |
| Sodium | <1,500 mg (ideal) | <1,500 mg (ideal) | 2,300 mg | Processed foods |
| Potassium | 3,400 mg | 2,600 mg | Not established | Fruits/vegetables |
| Fiber | 14 g/1,000 kcal | 14 g/1,000 kcal | - | Whole plant foods |
| Omega-3 (ALA) | 1.6 g | 1.1 g | - | Fatty fish, flax |

**Note**: Values are approximate. Consult current DRI tables for age-specific recommendations.

## Scoring Dimensions

### Dimension 1: Energy Alignment (Weight: 20%)
**Scoring Criteria**:
| Score | Criterion |
|-------|-----------|
| 100% | Target within ±5% of calculated need |
| 80% | Target within ±10% |
| 60% | Target within ±15% |
| 40% | Target within ±20% |
| 20% | Target beyond ±20% |
| 0% | Below safe floor or excessive surplus |

**Calculation**: Score based on how close the meal plan energy is to the target range.

### Dimension 2: Macronutrient Adequacy (Weight: 25%)
**Sub-dimensions** (each 8.33%):
1. **Protein**: Target g/kg achieved within ±10%
2. **Carbohydrate**: Within AMDR (45-65% of calories) and ≥ minimum
3. **Fat**: Within AMDR (20-35% of calories) and ≥ EFA minimum

**Scoring**: Each macro scored 0-100%, averaged for dimension score.

### Dimension 3: Micronutrient Adequacy (Weight: 20%)
**Key Nutrients Assessed** (each 2.5%):
- Vitamin D, Calcium, Iron, Vitamin B12, Folate, Potassium, Fiber, Omega-3

**Scoring**:
- 100%: ≥90% of DRI
- 75%: 75-89% of DRI
- 50%: 50-74% of DRI
- 25%: <50% of DRI
- 0%: <25% of DRI or above UL

**Average of all nutrients for dimension score.**

### Dimension 4: Diet-Quality Pattern (Weight: 20%)
**Framework Alignment** (each 10%):

**Mediterranean Diet Score** (Trichopoulou criteria):
- High: MUFA:SFA ratio, vegetables, legumes, fruits/nuts, grains
- Moderate: alcohol, fish/seafood
- Low: red/processed meat, dairy

**DASH Diet Score**:
- High: fruits, vegetables, whole grains, low-fat dairy
- Low: sodium, sweets, red/processed meats

**USDA MyPlate Alignment**:
- Half plate fruits/vegetables
- Half grains whole grains
- Varied protein sources
- Dairy or fortified alternative

**Scoring**: Percentage of criteria met per framework, average of three frameworks.

### Dimension 5: Feasibility & Preference Fit (Weight: 15%)
**Sub-dimensions**:
1. **Allergy/Restriction Compliance** (5%): Plan excludes all triggers
2. **Preference Alignment** (5%): incorporates likes, avoids dislikes
3. **Practical Feasibility** (5%): matches cooking ability, time, budget

**Scoring**: Binary or percentage-based per sub-dimension.

## Overall Score Calculation
```
Overall Score = (Energy × 0.20) + (Macro × 0.25) + (Micro × 0.20) + 
                (Pattern × 0.20) + (Feasibility × 0.15)
```

**Score Interpretation**:
- 90-100%: Excellent alignment
- 75-89%: Good with minor gaps
- 60-74%: Adequate with notable gaps
- 40-59%: Needs improvement
- <40%: Poor alignment

## Output Format

### TDEE & Targets
```markdown
## Energy & Protein Targets

### Basal Metabolic Rate
- Formula: Mifflin-St Jeor
- Calculation: (10 × 85) + (6.25 × 180) - (5 × 30) + 5 = 1,830 kcal/day
- Source: *Am J Clin Nutr, 1990*

### Total Daily Energy
- Activity: Moderate (multiplier 1.55)
- TDEE: 1,830 × 1.55 = 2,837 kcal/day

### Energy Target
- Goal: Weight loss (15% deficit)
- Target Range: 2,270 - 2,553 kcal/day
- Selected: 2,400 kcal/day

### Protein Target
- Target: 1.6-2.2 g/kg (ISSN position stand)
- Calculation: 1.9 g/kg × 85 kg = 162 g/day
- Distribution: 4 meals × ~40 g
- Source: *JISSN, 2017*

### Macronutrient Distribution
| Macro | Grams | Calories | % Total |
|-------|-------|----------|---------|
| Protein | 162 | 648 | 27% |
| Carbohydrate | 250 | 1,000 | 42% |
| Fat | 84 | 756 | 31% |
| **Total** | | | **2,404 kcal** |
```

### Adequacy Scorecard
```markdown
## Nutritional Adequacy Scorecard

### Macronutrients
| Nutrient | Target | Plan | % | Score |
|----------|--------|------|---|-------|
| Protein (g/kg) | 1.6-2.2 | 1.9 | 100% | 100 |
| Carbohydrate (% kcal) | 45-65% | 42% | 93% | 93 |
| Fat (% kcal) | 20-35% | 31% | 100% | 100 |
| Fiber (g/1000 kcal) | 14 | 18 | 128% | 100 |
| **Macro Average** | | | | **98%** |

### Key Micronutrients
| Nutrient | DRI | Plan | % | Score |
|----------|-----|------|---|-------|
| Vitamin D | 600 IU | 480 IU | 80% | 75 |
| Calcium | 1,000 mg | 1,200 mg | 120% | 100 |
| Iron | 8 mg | 14 mg | 175% | 100 |
| Vitamin B12 | 2.4 µg | 3.0 µg | 125% | 100 |
| Folate | 400 µg DFE | 450 µg DFE | 112% | 100 |
| Potassium | 3,400 mg | 3,100 mg | 91% | 75 |
| Omega-3 (ALA) | 1.6 g | 1.2 g | 75% | 50 |
| **Micro Average** | | | | **86%** |

### Diet Quality Pattern Alignment
| Framework | Score | Notes |
|-----------|-------|-------|
| Mediterranean | 85% | High vegetables, grains; moderate fish |
| DASH | 80% | Low sodium achieved; dairy adequate |
| MyPlate | 90% | Half plate fruits/vegetables |
| **Pattern Average** | | **85%** |

### Feasibility & Preference Fit
| Dimension | Score | Notes |
|-----------|-------|-------|
| Allergy Compliance | 100% | Shellfish excluded as required |
| Preference Alignment | 80% | 7 of 9 preferences incorporated |
| Practical Feasibility | 90% | Matches cooking ability and time |
| **Feasibility Average** | | **90%** |

### Overall Nutrition Score
**88.4%** — Good alignment with minor gaps (Omega-3, Vitamin D)

#### Dimension Breakdown
- Energy Alignment: 100% (20% weight) → 20.0 points
- Macronutrient Adequacy: 98% (25% weight) → 24.5 points
- Micronutrient Adequacy: 86% (20% weight) → 17.2 points
- Diet Quality Pattern: 85% (20% weight) → 17.0 points
- Feasibility & Fit: 90% (15% weight) → 13.5 points
- **Total**: 92.2 points (unweighted) → **88.4%** (weighted)
```

## Gap Analysis
For any nutrient <90% of target, identify specific food sources:

```markdown
### Identified Gaps
| Nutrient | Gap | Food Sources | Serving |
|----------|-----|--------------|---------|
| Omega-3 | 0.4 g ALA | Flaxseed, walnuts, chia | 1 tbsp flaxseed |
| Vitamin D | 120 IU | Fatty fish, fortified milk | 3 oz salmon |
```

## Quality Gates
- [x] BMR calculated using Mifflin-St Jeor with formula shown
- [x] TDEE uses appropriate activity multiplier
- [x] Energy target respects safe floor (≥ BMR × 1.2 minimum)
- [x] Protein target per evidence-based guidelines (ISSN/position stand)
- [x] All macronutrients compared to DRI/AMDR with values
- [x] Each micronutrient compared to DRI with percentage
- [x] Diet-quality pattern scored against named frameworks
- [x] Overall score calculated with documented weights
- [x] Gap analysis provides specific food solutions
- [x] All targets reference evidence sources

## Handoff to Roadmap
"Scoring complete. Overall nutrition score: 88.4%. Gaps identified in Omega-3 and Vitamin D. Proceeding to improvement roadmap."

Then invoke `sub-improvement-roadmap` with targets, scorecard, and gap analysis.
