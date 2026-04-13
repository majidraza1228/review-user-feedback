# PRD Template — Feature Specification

Use this template for every feature. Fill it in. Don't skip sections.

---

## Header

**Feature Name:** [FILL IN]

**Feature ID/Ticket:** [FILL IN]

**Owner (PM):** [FILL IN]

**Engineer Lead:** [FILL IN]

**QA Lead:** [FILL IN]

**Start Date:** [FILL IN]

**Target Ship Date:** [FILL IN]

**Priority Level:** [FILL IN — P0/P1/P2/P3]

**OKR Alignment:** See `../strategy/okrs.md` — [FILL IN which OKR this feature addresses]

---

## Problem Statement

**What user problem does this solve?**
[FILL IN — describe the user's pain, the frequency, the cost of not solving it. Reference user research if available.]

**Why now?**
[FILL IN — what's changed? Competitive pressure? User feedback spike? Tech debt? Market timing?]

**How did we validate this is real?**
[FILL IN — quote from user interview, support ticket volume, cohort analysis, etc.]

---

## Proposed Solution

**What we're building:**
[FILL IN — describe the feature in user-facing terms, not technical terms. What does the user see/do?]

**How it works (flow):**
[FILL IN — step-by-step. Include wireframe link or ASCII diagram if helpful.]

**Why this approach over alternatives:**
[FILL IN — why not [alternative]? What are the trade-offs?]

**Design doc link:** [FILL IN if available]

---

## User Stories & Acceptance Criteria

Format each story as:

**Story 1: [User type] wants [capability] so that [benefit]**

Acceptance Criteria:
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]

---

**Story 2: [User type] wants [capability] so that [benefit]**

Acceptance Criteria:
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]

---

[Add more stories as needed]

---

## AI/ML Considerations

**Does this feature involve AI/ML?** [FILL IN — yes/no]

If yes:
- **Model/Algorithm:** [FILL IN]
- **Data requirements:** [FILL IN — what training data, how much, how fresh?]
- **Accuracy/confidence threshold:** [FILL IN — what's acceptable performance?]
- **Failure mode:** [FILL IN — what happens if model is wrong? Graceful degrade or hard fail?]
- **Bias risks:** [FILL IN — could this discriminate? Against whom?]
- **Monitoring plan:** [FILL IN — how will we know if model degrades in production?]

See `../../00_foundations/responsible-ai.md` in parent repo for guardrails.

---

## Edge Cases & Failure Modes

**What could break this feature?**

| Edge Case | Behavior | Mitigation |
|-----------|----------|-----------|
| [FILL IN — e.g., user with 0 credits] | [What happens?] | [How do we handle it?] |
| [FILL IN] | [What happens?] | [How do we handle it?] |
| [FILL IN] | [What happens?] | [How do we handle it?] |

**Rollback plan:** [FILL IN — how quickly can we revert this? What data risk if we do?]

**Data consistency risks:** [FILL IN — if feature writes data, what if write fails halfway?]

---

## Success Metrics

Link to `../metrics/framework.md` for your product's North Star metric.

**Primary metric:** [FILL IN — what single metric proves this worked?]
- Target: [FILL IN — expected effect size & timeframe]
- Baseline: [FILL IN — current state before launch]

**Secondary metrics:**
- [FILL IN — adoption, engagement, retention, etc.]
- [FILL IN]
- [FILL IN]

**Guardrail metrics (don't break these):**
- [FILL IN — e.g., don't increase support tickets >10%, don't degrade page load time >50ms]

**How we'll measure:** [FILL IN — existing analytics? New instrumentation? Segment? Amplitude?]

---

## Open Questions

**Questions for PM/Design/Eng before we start:**

- [ ] [FILL IN]
- [ ] [FILL IN]
- [ ] [FILL IN]

**Dependencies & Blockers:**
- [ ] [FILL IN — e.g., "waiting for backend API design from Eng"]
- [ ] [FILL IN]

---

## Technical Spec (Optional, for complex features)

**API changes:** [FILL IN or link to API spec]

**Database schema changes:** [FILL IN or link to migration plan]

**Performance requirements:** [FILL IN — latency SLO, throughput, etc.]

**Security/compliance considerations:** [FILL IN — PII handling? Encryption? Audit trail?]

---

## Launch Checklist

Before shipping:
- [ ] All acceptance criteria met
- [ ] QA signed off on edge cases
- [ ] Metrics instrumentation in place
- [ ] Rollback plan documented & tested
- [ ] Comms copy written (see `../launches/checklist.md`)
- [ ] Support team briefed on new feature
- [ ] Monitor plan set up

See `../launches/checklist.md` for full pre-launch, launch-day, post-launch checklist.

---

## Sign-Off

- [ ] PM approved
- [ ] Engineering approved
- [ ] QA approved
- [ ] Design approved (if applicable)

---

**Last Updated:** [FILL IN DATE]
**Status:** [FILL IN — In Progress / Ready for Dev / In Dev / UAT / Shipped]
