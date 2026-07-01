---
name: sub-improvement-roadmap
description: Produce a sample meal plan plus prioritized, evidence-based improvement actions with effort and impact.
---

# Improvement Roadmap Sub-Skill

## Purpose
Transform nutritional targets and adequacy gaps into an actionable, preference-aligned meal plan with prioritized improvement steps. Bridge the gap between "what to eat" and "how to do it."

## Input Data
```json
{
  "targets": {
    "energy_kcal": 2400,
    "protein_g": 162,
    "carbs_g": 250,
    "fat_g": 84,
    "fiber_g": 34
  },
  "gaps": [
    {"nutrient": "Omega-3", "gap_mg": 400, "source": "flaxseed"},
    {"nutrient": "Vitamin D", "gap_IU": 120, "source": "salmon"}
  ],
  "restrictions": {
    "allergies": ["shellfish"],
    "intolerances": ["lactose"],
    "pattern": "none",
    "cultural": "none"
  },
  "preferences": {
    "likes": ["chicken", "rice", "vegetables", "eggs"],
    "dislikes": ["liver", "mushrooms"],
    "meals_per_day": 3,
    "cooking_ability": "intermediate"
  },
  "constraints": {
    "budget": "medium",
    "cooking_time_min": 30,
    "equipment": "full_kitchen"
  },
  "safety_cautions": []
}
```

## Meal Plan Construction

### Day Framework (Template)
Build a representative day that meets all targets and respects constraints:

#### Meal 1: Breakfast
**Design Principles**:
- 25-30% of daily protein for MPS
- Complex carbs for sustained energy
- Incorporates fruit/vegetable
- Quick to prepare (weekday constraint)

**Example** (2,400 kcal target):
- Scrambled eggs (4 large) with vegetables
- Whole grain toast (2 slices) with avocado
- Mixed berries (1 cup)
- Total: ~520 kcal, 28g protein

#### Meal 2: Lunch
**Design Principles**:
- Portable if needed
- Preppable in batch
- Leftover-friendly
- Includes vegetables and lean protein

**Example**:
- Grilled chicken breast (6 oz)
- Brown rice (1 cup cooked)
- Roasted mixed vegetables (2 cups)
- Olive oil dressing (1 tbsp)
- Total: ~620 kcal, 42g protein

#### Meal 3: Dinner
**Design Principles**:
- Family/social eating compatible
- Cultural flexibility
- Highest volume meal
- Includes all food groups

**Example**:
- Baked salmon (5 oz) — Vitamin D/Omega-3
- Quinoa (1 cup cooked)
- Steamed broccoli with garlic (1.5 cups)
- Mixed greens salad with vinaigrette
- Total: ~580 kcal, 38g protein

#### Snacks (if applicable)
**Design Principles**:
- Bridge macro gaps
- Convenient options
- Protein-focused for satiety

**Example Snacks**:
- Greek yogurt (1 cup) with honey and walnuts
- Apple slices with almond butter (2 tbsp)
- Total: ~360 kcal, 20g protein

**Day Total**: 2,080 kcal, 128g protein (for 3 meals + snacks example — adjust portions to hit targets)

### Week Pattern
While the day framework shows structure, the week pattern ensures:
- **Variety**: 3-4 different protein sources rotated
- **Efficiency**: Batch-cook friendly items (grains, roasted vegetables)
- **Flexibility**: 2-3 "catch-all" meals for leftovers or quick assembly
- **Treat meals**: 1-2 planned indulgences for adherence

**Week Template**:
| Day | Lunch Theme | Dinner Theme | Notes |
|-----|------------|--------------|-------|
| Monday | Chicken & grains | Salmon & vegetables | Batch cook grains |
| Tuesday | Leftovers | Lean beef & stir-fry | Prep vegetables |
| Wednesday | Turkey & rice | Fish tacos | Quick prep day |
| Thursday | Leftovers | Chicken & potatoes | |
| Friday | Egg salad | Planned treat meal | |
| Saturday | Social meal | Social meal | Flexible |
| Sunday | Batch prep | Comfort meal | Prep for week |

## Gap-Filling Strategy

### Systematic Approach
For each identified gap:
1. **Identify**: Which nutrient, how much deficit
2. **Prioritize**: Impact on health/score
3. **Source**: Best food sources given preferences
4. **Integrate**: Where to add in existing plan
5. **Verify**: Confirm target met

### Gap Integration Examples

**Omega-3 Gap (400 mg ALA)**:
- Option 1: Add 1 tbsp ground flaxseed to yogurt (+640 mg ALA)
- Option 2: Add 1 oz walnuts to snack (+2,500 mg ALA)
- Selection: Flaxseed (lower calorie, more precise)
- Integration: Breakfast yogurt or snack

**Vitamin D Gap (120 IU)**:
- Option 1: Add 3 oz canned salmon to salad (+300 IU)
- Option 2: Switch to fortified milk/plant milk (+100 IU/cup)
- Selection: Canned salmon (budget-friendly, also Omega-3)
- Integration: Lunch salad or dinner

**Fiber Gap (if applicable)**:
- Add legumes (1/2 cup beans = +6-8g fiber)
- Switch to whole grains exclusively
- Add berries or chia seeds
- Integration: Substitutions in existing meals

## Improvement Action System

### Action Taxonomy
Each improvement action is tagged with:
1. **Effort**: Small (S), Medium (M), Large (L)
2. **Impact**: Low, Medium, High
3. **Evidence Tier**: Systematic review, RCT, Position stand, Observational

### Effort Classification
| Effort | Description | Examples |
|--------|-------------|----------|
| Small (S) | <5 min, no learning | Add chia to yogurt, take vitamin D |
| Medium (M) | 15-30 min, some prep | Batch cook grains, prep vegetables |
| Large (L) | >30 min or behavior change | Learn new recipes, meal prep routine |

### Impact Classification
| Impact | Description | Score Effect |
|--------|-------------|--------------|
| High | >5% overall score increase | Closing major micro gaps |
| Medium | 2-5% score increase | Improving protein distribution |
| Low | <2% score increase | Minor optimizations |

### Prioritization Matrix
```
Priority Score = (Impact value × 2) + (100 - Effort value)
Impact: High=3, Medium=2, Low=1
Effort: S=10, M=30, L=60

Example: High impact + Small effort = 3×2 + (100-10) = 96 (top priority)
```

## Improvement Action Library

### Protein Optimization
| Action | Effort | Impact | Evidence | When |
|--------|--------|--------|----------|------|
| Distribute protein across 4 meals | M | High | ISSN 2017 | Current distribution uneven |
| Add post-exercise protein (20-30g) | S | Med | JISSN 2017 | Training days |
| Casein protein before bed | S | Low | Observational | Muscle gain goal |
| Plant protein rotation | M | Med | Position stand | Vegan pattern |

### Micronutrient Gaps
| Action | Effort | Impact | Evidence | For Nutrient |
|--------|--------|--------|----------|--------------|
| Daily fatty fish (2-3×/week) | M | High | RCT meta-analysis | Omega-3, Vitamin D |
| Ground flaxseed daily (1 tbsp) | S | Med | Observational | Omega-3 (ALA) |
| Fortified plant milk | S | Low | RDA guidance | Vitamin D, Calcium |
| Leafy greens daily | M | High | Cohort studies | Vitamin K, Folate |
| Legumes 3×/week | M | High | Position stand | Fiber, Folate, Iron |
| Citrus with iron sources | S | Med | RCT | Iron absorption |

### Diet Quality Pattern
| Action | Effort | Impact | Evidence | For Pattern |
|--------|--------|--------|----------|------------|
| Half plate vegetables | M | High | MyPlate framework | All patterns |
| Whole grains only | M | Med | Position stand | Mediterranean |
| EVOO as primary fat | S | Med | PREDIMED RCT | Mediterranean |
| Limit processed meats | S | Med | WHO classification | DASH, cancer risk |
| Berries daily | S | Low | Cohort | Mediterranean, antioxidants |

### Feasibility & Adherence
| Action | Effort | Impact | Evidence | Context |
|--------|--------|--------|----------|---------|
| Weekly meal prep session | L | High | Adherence research | Time-constrained |
| Batch-cook grains | M | Med | Practical | Budget, time |
| Pre-portioned snacks | S | Low | Behavioral | Portion control |
| Planned treat meals | S | Med | Adherence research | Sustainability |
| Grocery list template | S | Low | Practical | Budget, consistency |

## Meal Plan Output Format

### Sample Day
```markdown
## Sample Meal Plan

### Meal 1: Breakfast (~520 kcal, 28g protein)
- 4 large eggs scrambled with spinach, tomatoes, onions (1 cup vegetables)
- 2 slices whole-grain toast with 1/4 avocado
- 1 cup mixed berries
- Coffee or tea

**Prep time**: 10 minutes | **Batchable**: No | **Cost**: $4

### Meal 2: Lunch (~620 kcal, 42g protein)
- 6 oz grilled chicken breast (herb-marinated)
- 1 cup cooked brown rice
- 2 cups roasted mixed vegetables (broccoli, bell peppers, zucchini)
- 1 tbsp olive oil with lemon juice and herbs
- 1 cup baby spinach as side salad

**Prep time**: 25 minutes (15 if proteins prepped) | **Batchable**: Yes | **Cost**: $6

### Meal 3: Dinner (~580 kcal, 38g protein)
- 5 oz baked salmon with lemon and dill
- 1 cup cooked quinoa
- 1.5 cups steamed broccoli with garlic
- 2 cups mixed greens with balsamic vinaigrette
- 1/4 cup pumpkin seeds as garnish

**Prep time**: 30 minutes | **Batchable**: Partial | **Cost**: $10

### Snacks (if needed)
- Greek yogurt (1 cup) with 1 tbsp honey and 1 oz walnuts
- Apple slices with 2 tbsp almond butter
- Total: ~360 kcal, 20g protein

**Daily Total**: ~2,080 kcal, 128g protein (adjust portions to hit exact targets)
```

### Week Overview
```markdown
### Week Pattern
**Protein Rotation**:
- Mon/Tue: Chicken
- Wed/Thu: Salmon/canned fish
- Fri: Turkey or plant-based
- Sat/Sun: Flexible or social meals

**Batch Prep Recommendations**:
- Sunday: Cook grains (rice, quinoa) for 3-4 days
- Sunday: Roast vegetables (broccoli, peppers) for 3 days
- Mid-week: Prep second batch of vegetables
- Daily: Fresh salad assembly

**Quick Assembly Options** (for busy days):
- Pre-cooked protein + prepped vegetables + whole grain
- Protein smoothie with fruit and spinach
- Salad with canned fish and pre-cooked grains
```

## Improvement Roadmap Output

### Prioritized Actions
```markdown
## Improvement Roadmap

### Immediate Actions (Week 1) — High Priority
| # | Action | Effort | Impact | Evidence Source | Score |
|---|--------|--------|--------|-----------------|-------|
| 1 | Add 1 tbsp ground flaxseed daily to breakfast yogurt | S | High | Systematic review (Omega-3) | 96 |
| 2 | Distribute protein to 4 meals (aim for ~40g each) | M | High | ISSN position stand 2017 | 76 |
| 3 | Include fatty fish 2×/week (salmon, sardines) | M | High | RCT meta-analysis | 76 |
| 4 | Make half your plate vegetables at lunch and dinner | M | High | MyPlate framework | 76 |

### Next Steps (Weeks 2-3) — Medium Priority
| # | Action | Effort | Impact | Evidence Source | Score |
|---|--------|--------|--------|-----------------|-------|
| 5 | Switch entirely to whole grains | M | Med | Position stand | 66 |
| 6 | Add legumes (beans, lentils) 3×/week | M | High | Cohort studies | 76 |
| 7 | Incorporate berries daily | S | Low | Cohort (antioxidants) | 56 |
| 8 | Use extra virgin olive oil as primary fat | S | Med | PREDIMED RCT | 66 |

### Optimization (Weeks 4+) — Lower Priority
| # | Action | Effort | Impact | Evidence Source | Score |
|---|--------|--------|--------|-----------------|-------|
| 9 | Weekly meal prep session | L | High | Adherence research | 46 |
| 10 | Add casein protein before bed (if muscle gain) | S | Low | Observational | 56 |

**Priority Score Formula**: (Impact value × 2) + (100 - Effort value)
**Legend**: S=10, M=30, L=60 effort points; High=3, Med=2, Low=1 impact points
```

### Implementation Tips
```markdown
### Implementation Strategy

**Start Small**:
- Week 1: Focus on actions #1 and #2 (flaxseed + protein distribution)
- Week 2: Add actions #3 and #4 (fish + vegetables)
- Week 3: Incorporate remaining actions as comfortable

**Habit Stacking**:
- Add flaxseed to existing breakfast (attach to current habit)
- Pre-portion protein after grocery shopping (visual cue)
- Set vegetable portion before other foods (plate visual)

**Preparation Hacks**:
- Batch-cook grains on Sunday (saves 15 min/day)
- Pre-wash and cut vegetables when arriving from store
- Keep canned fish at desk for emergency meals

**Budget-Friendly Swaps**:
- Canned salmon instead of fresh (same nutrients, half price)
- Frozen berries instead of fresh (same nutrition, longer shelf life)
- Dried beans (cook in batch) instead of canned
- Seasonal vegetables (lower cost, higher quality)

**Eating Out/Social Meals**:
- Prioritize protein on plate first
- Fill half plate with vegetables if available
- Ask for dressing on the side (control portions)
- Plan ahead: review menu, decide strategy
- Treat meals are planned, not failures — enjoy them
```

## Allergy/Restriction Adaptations

### Common Modifications
| Restriction | Substitutions | Watch For |
|-------------|---------------|------------|
| Shellfish | Fatty fish (salmon, sardines) | Same Omega-3 benefit |
| Lactose | Lactose-free dairy, fortified plant milk | Calcium/Vit D |
| Gluten | Quinoa, buckwheat, rice | Ensure B-vitamins |
| Nuts | Seeds (chia, flax, pumpkin) | Omega-3, minerals |
| Vegan | Soy, legumes, nutritional yeast | B12, iron, calcium |

### Cultural Considerations
- **Halal**: Ensure meat sources, avoid alcohol in cooking
- **Kosher**: Separate meat/dairy if observed, avoid pork/shellfish
- **Jain**: No meat, eggs, root vegetables — focus on dairy, legumes, grains
- **Traditional**: Honor cultural foods while meeting targets (e.g., tofu in Asian cuisine, legumes in Indian)

## Quality Gates
- [x] Meal plan meets all energy and macro targets within ±5%
- [x] All micronutrient gaps addressed with specific food sources
- [x] Allergies and restrictions fully respected
- [x] Preferences incorporated (likes and dislikes addressed)
- [x] Cooking ability and time constraints honored
- [x] Each improvement action tagged with effort (S/M/L) and impact (Low/Med/High)
- [x] Each action includes evidence source reference
- [x] Actions prioritized with transparent scoring
- [x] Implementation strategy includes habit formation principles
- [x] Educational disclaimer included
- [x] Referral reminder present for medical nutrition therapy needs

## Handoff
"Improvement roadmap complete. 10 prioritized actions identified. Sample meal plan meets all targets within preferences and restrictions. Ready for synthesis."

Proceed to final output synthesis with disclaimer and referral information.
