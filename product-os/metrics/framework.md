# FeedbackLoop — Metrics Framework

**Version:** 1.0
**Date:** 2026-04-07
**Author:** Data Agent
**Hierarchy:** North Star → Input Metrics → Output Metrics → Guardrails

---

## North Star Metric

**Actionable Feedback Rate**
Definition: % of feedback submissions that lead to a logged decision in `decisions/log.md`
Why this: A submission that changes nothing is noise. We want feedback that drives decisions.
Target: ≥ 20% of submissions logged as a decision input within 2 weeks of submission

---

## Input Metrics (leading indicators)

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| Submissions/day | Rows inserted into `feedback` per day | ≥ 3/day during active use | Daily |
| Product pages visited | Unique product detail page loads per session | ≥ 2 products/session | Per session |
| Form start rate | % of product page loads where user clicks a star | ≥ 50% | Daily |

---

## Output Metrics (lagging indicators)

| Metric | Definition | Target | Frequency |
|--------|-----------|--------|-----------|
| Submission completion rate | Form starts that result in a submitted review | ≥ 60% | Weekly |
| Average rating distribution | Distribution of 1–5 ratings across products | No single rating > 60% | Weekly |
| Feedback coverage | % of products with ≥ 1 review | 100% within first session | Post-seed |

---

## Guardrail Metrics (do-not-exceed thresholds)

| Metric | Threshold | Action if Breached |
|--------|-----------|-------------------|
| Form error rate | < 5% of submissions return HTTP 400 | Investigate validation logic |
| Page load time | < 1 second for product listing with 6 products | Optimize DB query or add index |
| Empty comment rate | < 10% of attempts blocked by empty-comment validation | Reconsider UX copy |

---

## Measurement Approach

All metrics are approximated from the SQLite `feedback` table. No analytics infrastructure in v1.

```sql
-- Submissions per day
SELECT DATE(created_at), COUNT(*) FROM feedback GROUP BY DATE(created_at);

-- Rating distribution
SELECT rating, COUNT(*) FROM feedback GROUP BY rating;

-- Coverage: products with at least 1 review
SELECT COUNT(DISTINCT product_id) FROM feedback;
```

## Anti-Metrics (things we explicitly do not optimize for)

- **Total submissions** — a PM submitting 50 test reviews inflates this; it's not real signal
- **Session duration** — we want fast feedback, not engagement
- **Return visits** — FeedbackLoop is a tool, not a destination
