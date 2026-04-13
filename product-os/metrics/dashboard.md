# FeedbackLoop — Metrics Dashboard

**Week:** 2026-04-14 (Week 1 — Seed Data Baseline)
**Data Source:** SQLite `feedback` table (seed data, 20 entries)
**Note:** All data below is from `seed.py` seed data. Real user data collection begins post-launch.

---

## North Star

| Metric | This Week | Target | Status |
|--------|-----------|--------|--------|
| Actionable Feedback Rate | N/A (pre-launch) | ≥ 20% | — |

---

## Input Metrics

| Metric | This Week | Target | Status |
|--------|-----------|--------|--------|
| Submissions/day | 20 total (seed) | ≥ 3/day | Baseline set |
| Products with feedback | 6/6 | 6/6 | ✅ |
| Form start rate | N/A (pre-launch) | ≥ 50% | — |

---

## Rating Distribution (Seed Data)

| Rating | Count | % |
|--------|-------|---|
| ⭐⭐⭐⭐⭐ (5) | 6 | 30% |
| ⭐⭐⭐⭐ (4) | 8 | 40% |
| ⭐⭐⭐ (3) | 4 | 20% |
| ⭐⭐ (2) | 2 | 10% |
| ⭐ (1) | 0 | 0% |

**Average rating (all products):** 4.0
**Highest rated product:** Notion AI (4.5 avg)
**Lowest rated product:** Cron (3.5 avg)

---

## Guardrails

| Metric | This Week | Threshold | Status |
|--------|-----------|-----------|--------|
| Form error rate | 0% (pre-launch) | < 5% | ✅ |
| Page load time | < 100ms (local SQLite) | < 1s | ✅ |
| Empty comment rate | 0% (seed data has comments) | < 10% | ✅ |

---

## Week 1 Notes

- All 6 products seeded with 3–4 feedback entries each
- Seed data intentionally skewed positive (realistic for tech tools) but not uniformly 5-star
- Real metrics tracking begins when Sprint 3 launches publicly
- Dashboard will be updated weekly post-launch
