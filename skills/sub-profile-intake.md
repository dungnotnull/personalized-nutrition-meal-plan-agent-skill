---
name: sub-profile-intake
description: Capture anthropometrics, goal, activity, conditions, allergies, and preferences for nutrition planning.
---

# Profile Intake Sub-Skill

## Purpose
Collect comprehensive user data necessary to:
1. Calculate TDEE and set appropriate energy targets
2. Screen for medical red flags before guidance
3. Design a feasible, preference-aligned meal plan
4. Identify contraindications and special considerations

## Input Collection Framework

### Essential Anthropometrics (Required for TDEE)
| Field | Type | Valid Range | Purpose |
|-------|------|-------------|---------|
| Age | years | 13-120 | BMR calculation, DRI lookup |
| Sex | M/F/Intersex | - | BMR formula selection |
| Height | cm | 100-250 | BMR calculation |
| Weight | kg | 30-300 | BMR calculation |
| Activity Level | category | Sedentary→Elite | TDEE multiplier |

### Goal Definition
| Field | Options | Clarification |
|-------|---------|---------------|
| Primary Goal | Weight Loss, Muscle Gain, Maintenance, Health Management, Athletic Performance | Clarify if multiple |
| Timeline | weeks/months/open-ended | Expectation setting |
| Past Attempts | description | Learn from history |
| Confidence | 1-10 scale | Gauge readiness |

### Activity & Exercise Profile
| Field | Options | Multiplier |
|-------|---------|------------|
| Primary Activity | Sedentary (<30 min), Light (1-3 days), Moderate (3-5 days), Active (6-7 days), Elite (2×/day) | 1.2, 1.375, 1.55, 1.725, 1.9 |
| Exercise Types | Resistance, Cardio, Sports, Yoga/Pilates, Mixed | Protein targeting |
| Duration | avg minutes/day | Refine TDEE |
| Intensity | Low, Moderate, High, Vigorous | Refine TDEE |

### Medical History (Critical for Safety Screen)
| Field | Description | Red Flag |
|-------|-------------|-----------|
| Current Conditions | Diabetes (T1/T2), CKD, CVD, Liver disease, GI disorders, Thyroid, Cancer | Refer if active |
| Past Conditions | History of ED, obesity surgery, major surgeries | Context |
| Current Medications | List with timing if known | Interaction check |
| Supplements | List with doses | Interaction check |
| Family History | CVD, diabetes, obesity, ED | Context |

### Special Populations
| Status | Options | Action |
|--------|---------|--------|
| Pregnancy Status | Not pregnant, Currently pregnant, Lactating, Postpartum (<6mo), Planning pregnancy | Refer if pregnant/lactating |
| Age Group | Adolescent (13-18), Adult (19-64), Older Adult (65+) | DRI adjustment |
| Life Stage | Student, Working, Retired, Postpartum, Other | Feasibility |

### Dietary Restrictions & Allergies
| Category | Examples | Action |
|----------|----------|--------|
| Allergies | Nuts, shellfish, dairy, soy, wheat, eggs, fish | Exclude completely |
| Intolerances | Lactose, FODMAPs, gluten, histamine | Minimize/substitute |
| Dietary Pattern | Vegan, Vegetarian, Pescatarian, Paleo, Keto, Mediterranean | Respect in planning |
| Cultural/Religious | Halal, Kosher, Jain, Traditional | Respect in planning |
| Texture/Mechanical | Dysphagia, dental issues, no raw | Modify texture |

### Food Preferences & Aversions
| Field | Description | Purpose |
|-------|-------------|---------|
| Preferred Foods | List 5-10 foods enjoyed | Increase adherence |
| Aversion Foods | List foods strongly disliked | Avoid or substitute |
| Meal Structure | 3 meals/day, 5-6 small, IF 16:8, grazing | Plan framework |
| Cooking Ability | No cook, Basic, Intermediate, Advanced | Recipe complexity |
| Time Available | minutes/day for cooking | Convenience trade-off |

### Practical Constraints
| Constraint | Options | Impact |
|------------|---------|--------|
| Budget | Low (<$100/wk), Medium ($100-200), High (>$200) | Food choices |
| Access | Limited, Average, Excellent (specialty stores) | Variety |
| Equipment | Microwave only, Basic kitchen, Full kitchen | Cooking methods |
| Support | Solo, Partner, Family | Portion scaling |

### Behavioral Factors
| Factor | Description | Purpose |
|-----------|-------------|---------|
| Eating Environment | Home, work, school, on-the-go | Planning practicality |
| Social Eating | Rare, Sometimes, Frequent | Restaurant strategy |
| Stress Eating | None, Sometimes, Often | Emotional triggers |
| Night Eating | None, Sometimes, Often | Circadian patterns |
| Past Success | What has worked before | Replicate patterns |
| Past Barriers | What caused failure | Anticipate obstacles |

## Intake Process

### Phase 1: Essential Data Collection
1. **Greeting & Purpose**: Explain that personalized nutrition planning requires some basic information.
2. **Anthropometrics**: Collect age, sex, height, weight. Use metric system internally.
3. **Activity Level**: Use the five-level scale with clear descriptions.
4. **Primary Goal**: Single primary goal; note secondary goals.

**Quality Check**: All TDEE inputs present and within valid ranges. If out of range, confirm correctness or note concern.

### Phase 2: Safety-Critical Information
1. **Medical Conditions**: List current and past conditions.
2. **Medications**: All current prescriptions and OTC.
3. **Special Status**: Explicitly ask about pregnancy, lactation, planning pregnancy.
4. **Eating Behaviors**: History of disordered eating, binging, restrictive behaviors.

**Quality Check**: All safety-screen inputs captured. If user hesitant, frame as "for your safety."

### Phase 3: Preferences & Constraints
1. **Allergies & Restrictions**: Complete list with severity if known.
2. **Food Preferences**: Likes and strong dislikes.
3. **Dietary Pattern**: If follows named pattern, note specifics.
4. **Practical Constraints**: Budget, cooking ability, time, equipment.

**Quality Check**: Feasibility assessment possible from constraints.

### Phase 4: Behavioral Context
1. **Eating Patterns**: Meal timing, frequency, social eating.
2. **Past Experience**: What worked, what didn't, why.
3. **Current Challenges**: Perceived barriers to success.

**Quality Check**: Sufficient data for adherence strategy.

## Validation Rules

### Anthropometric Validation
```python
# Pseudo-code for validation
def validate_anthropometrics(age, sex, height, weight):
    if age < 13:
        flag = "Age <13: Pediatric specialist recommended"
    elif age > 120:
        flag = "Age >120: Confirm accuracy"
    
    if sex not in ['M', 'F', 'Intersex']:
        flag = "Sex needed for BMR calculation"
    
    if height < 100 or height > 250:
        flag = "Height outside typical range: Confirm units (cm)"
    
    if weight < 30 or weight > 300:
        flag = "Weight outside typical range: Confirm units (kg)"
    
    return flag or "PASS"
```

### Activity Level Validation
- Sedentary: Desk job, no intentional exercise → 1.2
- Light: Light exercise 1-3 days/week → 1.375
- Moderate: Moderate exercise 3-5 days/week → 1.55
- Active: Hard exercise 6-7 days/week → 1.725
- Elite: Very hard exercise, physical job, training 2×/day → 1.9

### Completeness Check
Before proceeding to safety screen, ensure:
- [x] Age, sex, height, weight present and valid
- [x] Activity level clearly defined
- [x] Primary goal identified
- [x] Medical conditions captured (even if "none")
- [x] Medications captured (even if "none")
- [x] Pregnancy status explicitly asked and answered
- [x] Allergies and restrictions listed
- [x] At least basic preference data

## Output Format

### Profile Object
```json
{
  "anthropometrics": {
    "age": 30,
    "sex": "M",
    "height_cm": 180,
    "weight_kg": 85,
    "bmi": 26.2
  },
  "goal": {
    "primary": "weight_loss",
    "secondary": ["muscle_retention"],
    "timeline_weeks": 12
  },
  "activity": {
    "level": "moderate",
    "multiplier": 1.55,
    "types": ["resistance", "cardio"],
    "days_per_week": 4
  },
  "medical": {
    "conditions": ["hypertension", "controlled"],
    "medications": ["lisinopril 10mg"],
    "supplements": ["vitamin_d"],
    "pregnancy_status": "not_pregnant",
    "ed_history": null
  },
  "restrictions": {
    "allergies": ["shellfish"],
    "intolerances": ["lactose"],
    "pattern": "none",
    "cultural": "none"
  },
  "preferences": {
    "likes": ["chicken", "rice", "vegetables"],
    "dislikes": ["liver", "mushrooms"],
    "meals_per_day": 3,
    "cooking_ability": "intermediate"
  },
  "constraints": {
    "budget": "medium",
    "cooking_time_min": 30,
    "equipment": "full_kitchen"
  },
  "behavioral": {
    "eating_environment": "home_and_work",
    "social_eating": "sometimes",
    "past_barriers": ["evening_snacking", "weekend_overindulgence"]
  }
}
```

## Edge Cases & Special Handling

### User Doesn't Know Anthropometrics
If missing measurements:
1. Offer estimation methods (height from wall mark, weight from recent doctor visit)
2. Use self-reported with confidence noted
3. Proceed with caveat about reduced accuracy
4. Recommend confirming measurements for optimal results

### User Reluctant to Share Medical History
Frame as "important for your safety":
1. Explain that certain conditions require different approaches
2. Offer general options if specifics unavailable
3. Note that professional referral may be needed without full picture
4. Never pressure — respect privacy boundaries

### Multiple Conflicting Goals
If user wants to lose fat and gain muscle simultaneously:
1. Acknowledge common scenario (body recomposition)
2. Set expectation: slower progress than single goal
3. Prioritize based on leanness (leaner → focus on fat loss first)
4. Plan for small calorie deficit with high protein

### Unrealistic Timeline
If timeline is too aggressive for the goal:
1. Provide realistic timeframe based on evidence
2. Explain risks of aggressive approach (muscle loss, adherence failure)
3. Offer alternative timeline with better expected outcomes
4. Let user choose informed approach

## Quality Gates
- [x] All essential anthropometrics collected and validated
- [x] Activity level clearly mapped to TDEE multiplier
- [x] Medical conditions and medications captured for safety screening
- [x] Pregnancy/lactation status explicitly determined
- [x] All allergies and restrictions documented with severity
- [x] Sufficient preference data for feasible planning
- [x] Practical constraints identified for adherence strategy
- [x] Profile object structured for downstream processing

## Handoff to Safety Screen
Upon completion, output: "Profile intake complete. Proceeding to mandatory safety screen."

Then invoke `sub-safety-screener` with the profile object.
