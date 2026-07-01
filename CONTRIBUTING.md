# Contributing to Personalized Nutrition & Meal Plan

Thank you for your interest in contributing! This document provides guidelines for contributing to the Personalized Nutrition & Meal Plan skill.

---

## 🎯 Project Overview

This is an AI skill that generates personalized nutrition plans with mandatory safety screening. It uses evidence-based frameworks (DRI, Mediterranean, DASH) and prioritizes user safety through medical red-flag detection.

**Key Principle**: Safety first. The safety screener has veto power over the entire harness — no meal plan is generated without passing safety checks.

---

## 🤝 How to Contribute

### Ways to Contribute

| Type | Examples | Impact |
|------|----------|--------|
| **Evidence** | Add authoritative sources, update DRI values | High |
| **Testing** | New test scenarios, edge case coverage | High |
| **Documentation** | Improve clarity, add examples | Medium |
| **Internationalization** | Country-specific DRI, referral resources | Medium |
| **Accessibility** | Simplified language, translations | Medium |

### Getting Started

1. **Fork or clone** the repository
2. **Review documentation**:
   - `skills/main.md` — Understand the harness flow
   - `skills/sub-safety-screener.md` — CRITICAL: Safety protocols
   - `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — Project structure
3. **Identify an area** to improve (see below)
4. **Make changes** following guidelines
5. **Test thoroughly** (see Testing section)
6. **Submit** with clear description of changes

---

## ⚠️ Critical Safety Rules

### NEVER Bypass Safety Screening

**Absolute Requirements**:
- Safety screen must run BEFORE any nutrition plan
- Red flags (ED risk, pregnancy, chronic disease) → REFER, not plan
- No restrictive calorie plans for at-risk populations
- Referral resources must be specific and actionable

**What Never to Do**:
- ❌ Disable or skip safety screening
- ❌ Generate restrictive plans for BMI <16 or ED risk
- ❌ Provide pregnancy weight loss plans
- ❌ Offer medical nutrition therapy (refer to RD instead)
- ❌ Remove disclaimers or referral resources

**What Always to Do**:
- ✅ Run safety screen first (sub-safety-screener.md)
- ✅ REFER on red flags with specific resources
- ✅ Maintain educational (not prescriptive) framing
- ✅ Include disclaimers in all outputs
- ✅ Update referral resources for new conditions/regions

---

## 📝 Contribution Guidelines

### Evidence & Frameworks

**Adding New Evidence**:
1. Source must be authoritative (PubMed, Cochrane, NIH, WHO, etc.)
2. Include full citation with URL
3. Note evidence tier (systematic review > RCT > observational)
4. Update `SECOND-KNOWLEDGE-BRAIN.md` if adding to knowledge base
5. Test against existing scenarios

**Updating Framework Values**:
1. Verify source is current (check official DRI tables)
2. Document change with source and date
3. Update affected calculations in `sub-scoring-engine.md`
4. Add test scenario for validation

**Example**:
```markdown
### Updated Vitamin D RDA (July 2026)
- Previous: 600 IU (2011 DRI)
- Current: 800 IU (2024 DRI update)
- Source: https://ods.od.nih.gov/factfiles/VitaminD-HealthProfessional/
- Impact: All micronutrient scoring now uses 800 IU target
```

### Test Scenarios

**Adding New Scenarios** (in `tests/test-scenarios.md`):
1. Define input profile
2. Specify expected outcome (PASS/REFER, score range)
3. Cover edge cases (rare conditions, boundary values)
4. Include cultural/international variations
5. Verify referral accuracy

**Test Scenario Template**:
```markdown
## Scenario X — [Descriptive Name]
- **Input**: [Profile details]
- **Expected**: [TDEE, targets, score] or [REFER with reason]
- **Pass**: [Criteria for success]
- **Edge Case**: [What makes this scenario unique]
```

### Documentation

**Improving Documentation**:
1. Maintain consistent formatting with existing docs
2. Use clear, non-medical language where possible
3. Include examples for complex concepts
4. Cross-reference related sections
5. Update table of contents if applicable

**Documentation Standards**:
- Title case for headings
- Code blocks for examples
- Tables for comparisons
- Citations for all claims
- Clear section hierarchy

### Internationalization

**Country-Specific Adaptations**:
1. Use local DRI/RDA values (if different from US)
2. Add local referral resources
3. Include cultural food patterns
4. Translate key phrases (optional)
5. Test with local profiles

**Example**:
```markdown
### United Kingdom Adaptation
- DRI Source: UK SACN (not US NIH)
- Referral: British Dietetic Association (dietitians.uk.com)
- Emergency: 999 (not 911)
- Cultural: Include traditional British foods in examples
```

---

## 🧪 Testing Your Changes

### Before Submitting

1. **Run existing test scenarios** — Ensure no regressions
2. **Test your specific change** — Create a test scenario if applicable
3. **Verify safety screen** — Confirm red flags still trigger referral
4. **Check documentation** — Ensure all references are accurate
5. **Review disclaimers** — Confirm present and appropriate

### Test Checklist

- [ ] All 6 existing test scenarios pass
- [ ] New scenario (if added) passes expected criteria
- [ ] Safety screen correctly identifies red flags
- [ ] Referral resources are current and specific
- [ ] Evidence citations are accurate and accessible
- [ ] Documentation is clear and complete
- [ ] No medical advice language (educational framing only)

---

## 📧 Submitting Contributions

### Pull Request Format

**Title**: `Type: Brief description`

**Types**: `Evidence`, `Test`, `Docs`, `International`, `Fix`, `Refactor`

**Body Template**:
```markdown
## Summary
[Brief description of changes]

## Type
- [ ] Evidence (new sources, updated values)
- [ ] Test (new scenarios, edge cases)
- [ ] Documentation (clarity, examples)
- [ ] International (country-specific adaptations)
- [ ] Bug fix
- [ ] Refactoring

## Changes Made
- [ ] File(s) modified
- [ ] Test scenarios updated
- [ ] Documentation updated

## Testing
- [ ] All existing tests pass
- [ ] New test scenario added (if applicable)
- [ ] Safety screen verified
- [ ] Referral resources checked

## Evidence Sources
[List any new evidence sources with URLs]

## Additional Notes
[Any context helpful for reviewers]
```

### Review Process

1. **Automated checks**: Documentation completeness, test passage
2. **Safety review**: Verify safety screening intact
3. **Evidence review**: Verify sources are authoritative
4. **Merge**: Approval from maintainers

---

## 🚫 What We Don't Accept

| Type | Reason | Alternative |
|------|--------|-------------|
| Bypassing safety | User safety risk | Never acceptable |
| Medical advice | Legal/ethical issue | Educational framing only |
| Non-authoritative sources | Evidence quality | Use PubMed/Cochrane/NIH |
| Removal of disclaimers | Legal requirement | Always maintain |
| Uncredited content | Intellectual property | Cite sources |
| Discriminatory content | Inclusivity principle | Respectful language |

---

## 💡 Ideas for Contributions

### High Priority

1. **Evidence expansion**:
   - [ ] Add 2025-2026 DRI updates when released
   - [ ] Include Canadian/European/Australian DRI equivalents
   - [ ] Add condition-specific guidance references (diabetes, CKD)

2. **Test scenarios**:
   - [ ] Adolescent scenarios (age 13-18)
   - [ ] Elderly scenarios (65+ with sarcopenia)
   - [ ] Bariatric surgery post-op scenarios
   - [ ] Cultural diet patterns (Asian, Latin American, African)

3. **Referral resources**:
   - [ ] Expand international referral database
   - [ ] Add telehealth nutrition options
   - [ ] Include insurance navigation resources

### Medium Priority

1. **Documentation**:
   - [ ] Create simplified language version
   - [ ] Add visual diagrams for workflow
   - [ ] Include FAQ section

2. **Accessibility**:
   - [ ] Plain language summary
   - [ ] Translation of key phrases
   - [ ] Audio/video format tutorials

### Low Priority

1. **Tooling**:
   - [ ] Automated test runner for scenarios
   - [ ] Knowledge base visualization
   - [ ] CI/CD for documentation validation

---

## 📜 Code of Conduct

Please refer to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community standards.

**Key Principles**:
- Respectful collaboration
- Evidence-based discussions
- User safety paramount
- Inclusive language

---

## ❓ Getting Help

### Questions?

1. **Check documentation** — Most answers in `skills/*.md`
2. **Search issues** — Similar questions may already be answered
3. **Open issue** — Describe question clearly with context
4. **Contact maintainers** — For urgent matters only

### Resources

- **Project documentation**: `PROJECT-detail.md`
- **Development tracking**: `PROJECT-DEVELOPMENT-PHASE-TRACKING.md`
- **Test scenarios**: `tests/test-scenarios.md`
- **Safety protocols**: `skills/sub-safety-screener.md`

---

## 🙏 Recognition

Contributors will be recognized in the project documentation. Notable contributions (significant evidence additions, critical safety improvements) will be acknowledged in release notes.

---

**Thank you for contributing to safer, evidence-based nutrition guidance!**

Last Updated: 2026-07-01
