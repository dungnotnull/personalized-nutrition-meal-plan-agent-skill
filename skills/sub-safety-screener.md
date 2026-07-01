---
name: sub-safety-screener
description: MANDATORY medical/red-flag screen that runs before any nutrition guidance; refers out when professional care is indicated.
---

# Safety Screener Sub-Skill (MANDATORY)

## Purpose
Protect users from inappropriate nutrition guidance by screening for medical and psychological conditions that require professional care. This sub-skill has **veto power** over the entire harness — a REFER verdict halts all planning and produces only educational content and specific referrals.

## Core Principle
**When in doubt, REFER.** It is always safer to recommend professional consultation than to provide potentially harmful guidance.

## Input: Profile Object
```json
{
  "anthropometrics": {"age", "sex", "height_cm", "weight_kg", "bmi"},
  "medical": {
    "conditions": [],
    "medications": [],
    "supplements": [],
    "pregnancy_status": "",
    "ed_history": ""
  },
  "goal": {"primary", "timeline"},
  "restrictions": {"allergies": []}
}
```

## Red-Flag Categories & Thresholds

### 1. Eating Disorder Risk
**INDICATORS**:
- Self-reported history of anorexia, bulimia, binge eating disorder, EDNOS, ARFID
- Current restrictive eating (<1200 kcal for average adult)
- Expressions of body-image distress ("I hate my body", "I feel fat regardless of weight")
- Obsessive calorie counting, food anxiety, fear of specific foods
- Request for very-low-calorie diet (<800 kcal/day)
- Rapid weight pursuit with unrealistic timeline
- Excessive exercise (>2 hours/day) combined with restriction
- Social withdrawal around food, secretive eating patterns

**VERDICT**: REFER
**RESOURCE**: National Eating Disorders Association (nationaleatingdisorders.org) or local ED specialist
**OUTPUT**: General healthy eating education only. No calorie targets, no meal plans, no weight-specific guidance.

**SCREENING QUESTIONS**:
1. "Have you ever been diagnosed with an eating disorder?"
2. "Do you currently feel anxious about eating certain foods?"
3. "Are you pursuing a specific weight because of how you feel about your body?"
4. "How would you feel if this plan resulted in weight gain?"

### 2. BMI Safety Thresholds
**CRITICAL ZONES**:
- BMI <16: Severe undernutrition → REFER to physician/ED specialist
- BMI 16-16.5: Underweight, potential medical complication → REFER or CAUTION
- BMI 16.5-18.5: Underweight → CAUTION, consider professional referral
- BMI >40: Class III obesity → Consider medical management referral
- BMI >50: Super-obesity → REFER to bariatric specialist

**WEIGHT VELOCITY**:
- Unintentional weight loss >2 kg/month → REFER to physician
- Rapid intentional weight loss >1 kg/week → CAUTION, educate on safe rate

**CALCULATION**: BMI = weight (kg) / height (m)²
- Note: For athletes with high muscle mass, BMI may misclassify. Use waist circumference or body fat percentage if available.

### 3. Pregnancy, Lactation, & Postpartum
**STATES**:
- Currently pregnant → REFER to OB/GYN or prenatal RD
- Lactating/breastfeeding → REFER to lactation consultant or RD
- <6 months postpartum → REFER for postpartum nutrition care
- Planning pregnancy → REFER to preconception counseling

**VERDICT**: REFER for weight-specific guidance
**ALTERNATIVE**: Provide general prenatal nutrition education if user declines referral
**RESOURCES**:
- Academy of Nutrition and Dietetics: eatright.org/prenatal
- American College of Obstetricians and Gynecologists: acog.org

### 4. Chronic Disease Management
**CONDITIONS REQUIRING REFERRAL**:
- Diabetes Type 1: Carbohydrate counting, insulin coordination → REFER to certified diabetes educator (CDE)
- Diabetes Type 2: May provide general guidance but REFER for medication coordination
- Chronic Kidney Disease (Stages 3-5): Protein, sodium, potassium restrictions → REFER to renal RD
- Cardiovascular Disease: Heart failure, recent MI, cardiac rehab → REFER to cardiac rehab RD
- Liver Disease (Cirrhosis, hepatitis): Protein restrictions, sodium → REFER to hepatology RD
- GI Disorders: IBD, celiac (newly diagnosed), gastroparesis → REFER to GI RD
- Cancer (active treatment): Malnutrition risk, treatment interactions → REFER to oncology RD
- HIV/AIDS: Medication interactions, wasting → REFER to specialized RD
- Thyroid disorders: If uncontrolled → REFER to endocrinologist

**CONDITIONS ALLOWING GENERAL GUIDANCE** (with caution):
- Controlled hypertension (BP <140/90 on medication)
- Controlled hyperlipidemia
- Prediabetes (no medication)
- Stable thyroid on replacement

### 5. Medication-Nutrient Interactions
**HIGH-RISK INTERACTIONS** → REFER:
- **Warfarin (Coumadin)**: Vitamin K intake affects INR → REFER to anticoagulation clinic
- **MAOIs**: Tyramine-rich foods risk hypertensive crisis → REFER
- **Lithium**: Sodium intake affects levels → REFER
- **Immunosuppressants**: Grapefruit and other interactions → REFER
- **Chemotherapy**: Multiple food-drug interactions → REFER to oncology pharmacist

**MODERATE INTERACTIONS** → CAUTION:
- **Metformin**: B12 absorption may be reduced → Note in plan
- **Orlistat**: Fat-soluble vitamin malabsorption → Suggest multivitamin
- **Antibiotics**: Dairy interactions (tetracyclines, quinolones) → Note timing

**SCREENING APPROACH**:
1. Ask: "Are you taking any prescription medications regularly?"
2. Ask: "Any over-the-counter medications or supplements?"
3. Check known interactions for each medication
4. If high-risk interaction found → REFER

### 6. Severe Allergies & Intolerances
**REFER FOR CLINICAL MANAGEMENT**:
- Anaphylactic food allergies (nuts, shellfish, etc.) → REFER to allergist
- Eosinophilic esophagitis → REFER to GI specialist
- FPIES (Food Protein-Induced Enterocolitis) → REFER to allergist/GI
- Multiple severe allergies → REFER to allergist + RD

**CAN MANAGE IN-PLAN** (with precautions):
- IgE-mediated allergies (avoidance known)
- Lactose intolerance (substitution strategies)
- FODMAP intolerance (if dietitian-provided plan available)
- Gluten intolerance (non-celiac): Substitution strategies

### 7. Age-Related Considerations
**ADOLESCENTS (13-18)**:
- CAUTION for weight loss (may affect growth/development)
- REFER to pediatrician/RD if BMI <5th percentile or >95th
- Focus on growth-supporting nutrition, not restriction

**OLDER ADULTS (65+)**:
- CAUTION for weight loss (sarcopenia risk)
- REFER if unintentional weight loss
- Focus on protein sufficiency, muscle preservation

### 8. Surgical History
**REFER IF**:
- <3 months post-bariatric surgery → REFER to bariatric RD
- <3 months post-major abdominal surgery → REFER for surgical nutrition
- Planned surgery upcoming → REFER for pre-op optimization

### 9. Mental Health Comorbidities
**REFER IF**:
- Active depression with appetite changes
- Active anxiety with food aversion
- PTSD with eating disruption
- Substance use disorder affecting nutrition

## Screening Process

### Phase 1: Automated Red-Flag Detection
```python
def auto_screen(profile):
    red_flags = []
    
    # BMI check
    bmi = profile['anthropometrics']['bmi']
    if bmi < 16:
        red_flags.append("CRITICAL: BMI <16 indicates severe undernutrition")
    elif bmi < 18.5:
        red_flags.append("CAUTION: BMI <18.5 indicates underweight")
    
    # Pregnancy check
    if profile['medical']['pregnancy_status'] in ['pregnant', 'lactating', 'postpartum']:
        red_flags.append(f"REFER: {profile['medical']['pregnancy_status']} requires specialist care")
    
    # Chronic disease check
    high_risk_conditions = ['diabetes_t1', 'ckd_stage_3plus', 'liver_disease', 'cancer_active']
    for condition in profile['medical']['conditions']:
        if condition.lower() in high_risk_conditions:
            red_flags.append(f"REFER: {condition} requires specialist management")
    
    # Medication interaction check
    high_risk_meds = ['warfarin', 'maoi', 'lithium', 'immunosuppressant']
    for med in profile['medical']['medications']:
        if med.lower() in high_risk_meds:
            red_flags.append(f"REFER: {med} has critical nutrient interactions")
    
    return red_flags
```

### Phase 2: Behavioral Screening
If user requests very-low-calorie plan:
- "Plans below 1200 calories per day are not safe without medical supervision. Are you working with a healthcare provider for this?"

If user expresses body-image distress:
- "It sounds like you're experiencing some difficult feelings about your body. This is very common and there are specialists who can help. Would you like resources for eating disorder support?"

### Phase 3: Gray-Area Judgment
For cases that don't clearly trigger REFER but raise concern:
- Default to conservative guidance
- Strongly recommend professional consultation
- Provide general healthy eating education only
- Document the caution in output

## Output Format

### PASS Verdict
```markdown
## Safety Screening: PASS

The profile has been reviewed and no immediate red flags requiring referral were identified. 

**Cautions (if any)**: [Any conditions requiring special attention in planning]

**Planning Approved**: Proceeding to TDEE calculation and meal planning with appropriate considerations.
```

### REFER Verdict
```markdown
## Safety Screening: REFER OUT

Based on the information provided, professional medical or nutritional care is recommended before implementing any specific nutrition plan.

**Reason for Referral**: [Specific red flag identified]

**Recommended Specialist**: [RD, physician, specialist type]

**How to Find Care**:
- Academy of Nutrition and Dietetics: eatright.org/find-an-expert
- Insurance provider directory
- Primary care physician for referral

**While Awaiting Professional Care**:
[General healthy eating principles appropriate to the situation]

**Emergency Resources**:
- National Eating Disorders Helpline: 1-800-931-2237
- Crisis line: 988 (US) or local emergency number

**No restrictive meal plan will be generated** in accordance with safety protocols.
```

## Referral Resources Database

### United States
| Need | Resource | Contact |
|------|----------|---------|
| Eating disorders | National Eating Disorders Association | nationaleatingdisorders.org, 1-800-931-2237 |
| Registered dietitian | Academy of Nutrition & Dietetics | eatright.org/find-an-expert |
| Diabetes | American Diabetes Association | diabetes.org |
| Kidney disease | National Kidney Foundation | kidney.org |
| Heart disease | American Heart Association | heart.org |
| Cancer | American Cancer Society | cancer.org |
| General medical | Insurance directory | [Insurance website] |
| Crisis | Suicide & Crisis Lifeline | 988 (US) |

### International
| Country | Dietitian Finder | Emergency |
|---------|-----------------|-----------|
| Canada | Dietitians of Canada | dietitians.ca | 911 |
| UK | British Dietetic Association | bda.uk.com | 999 |
| Australia | Dietitians Australia | dietitiansaustralia.org.au | 000 |
| Other | Check national nutrition association | Local emergency |

## Quality Gates
- [x] Every red-flag category explicitly checked
- [x] BMI calculated and compared to safety thresholds
- [x] Pregnancy/lactation status explicitly determined
- [x] Chronic diseases screened for high-risk conditions
- [x] Medications checked for nutrient interactions
- [x] Eating disorder indicators assessed
- [x] Age-appropriate considerations applied
- [x] REFER verdict halts harness (no restrictive plan generated)
- [x] PASS verdict includes all cautions for downstream planning
- [x] Referral resources provided specific to the red flag
- [x] Emergency resources included for crisis situations
- [x] General healthy eating education provided for REFER cases

## Handoff

If PASS: "Safety screen passed with [cautions if any]. Proceeding to evidence research."

If REFER: "Safety screen triggered referral. Halting meal planning. [Provide referral resources and general education]."

The harness does not proceed to scoring/roadmap on REFER.
