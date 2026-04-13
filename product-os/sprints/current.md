# Sprint 2 — Build

**Dates:** 2026-04-14 → 2026-04-21
**Status:** Active
**Goal:** Ship all three pages (product listing, product detail, admin) with real DB data

---

## Sprint Goal

> "By end of Sprint 2, a developer can clone the repo, run `python app.py && python seed.py`, and submit feedback through the UI."

## Stories

| Story | Points | Owner | Status |
|-------|--------|-------|--------|
| Write `templates/base.html` (dark theme shell) | 2 | Engineer Agent | ✅ Done |
| Write `static/style.css` (GitHub dark palette) | 2 | Engineer Agent | ✅ Done |
| Write `templates/index.html` (product card grid) | 3 | Engineer Agent | ✅ Done |
| Write `templates/product.html` (detail + form + reviews) | 3 | Engineer Agent | ✅ Done |
| Write `templates/admin.html` (feedback table) | 2 | Engineer Agent | ✅ Done |
| Write `static/main.js` (star rating widget) | 2 | Engineer Agent | ✅ Done |
| Wire `GET /` route to real DB data | 2 | Engineer Agent | In Progress |
| Wire `GET /product/<id>` to real DB data | 2 | Engineer Agent | In Progress |
| Wire `GET /admin` to real DB data | 1 | Engineer Agent | In Progress |
| Implement `POST /api/feedback` with validation | 3 | Engineer Agent | In Progress |
| Write `seed.py` (6 products + 20 entries) | 2 | Engineer Agent | In Progress |
| Full flow test: submit → list → admin | 2 | QA Agent | Not Started |

**Total points:** 26
**Done:** 14
**In Progress:** 10
**Not Started:** 2

## Acceptance Gate

Sprint 2 is done when:
- [ ] `python app.py` starts without errors
- [ ] `python seed.py` inserts 6 products + 20 feedback entries
- [ ] All 4 routes return correct data
- [ ] Feedback submission form works end-to-end
- [ ] QA Agent validates all acceptance criteria from the 3 PRDs

## Blockers

None currently.

## Next Sprint Preview (Sprint 3)

- Write `README.md` (dev onboarding + PM workflow explanation)
- Write `retros/sprint-1-retro.md`
- Fill in `metrics/dashboard.md` (week 1 dummy data)
- Fill in `launches/checklist.md`
- Final PM layer audit: zero `[FILL IN]` check
