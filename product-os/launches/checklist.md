# FeedbackLoop — Launch Checklist

**Target Launch:** 2026-04-28
**Version:** v1.0
**Owner:** PM (Syed)

---

## Pre-Launch

### PM Layer
- [x] All PRDs approved (`prd/`)
- [x] OKRs defined and baselined (`strategy/okrs.md`)
- [x] Decision log current (`decisions/log.md`)
- [x] Metrics framework written (`metrics/framework.md`)
- [ ] Sprint 2 retro complete
- [ ] All `[FILL IN]` placeholders removed from `product-os/`

### Technical
- [x] Schema finalized (`schema.sql`)
- [x] All 4 routes return correct data
- [x] Form validation works (AC1–AC5 from `prd/feedback-submission.md`)
- [ ] Smoke test on clean machine (no prior `pip install`)
- [ ] `python seed.py` tested on empty database
- [ ] Manual test: submit feedback → appears in admin

### Documentation
- [ ] `README.md` written (what it is, how to run)
- [ ] "How the PM workflow works" section in README
- [ ] Build order (PM before code) documented
- [ ] CLAUDE.md accurate and complete

### QA
- [ ] QA Agent validates all acceptance criteria from 3 PRDs
- [ ] Edge cases tested: empty comment, rating out of range, missing product_id
- [ ] Tested in Chrome, Firefox, Safari

---

## Launch Day

- [ ] Final `grep -r "\[FILL IN\]" product-os/` returns 0 matches
- [ ] `python app.py` starts cleanly
- [ ] All 6 products visible on homepage
- [ ] Share repo link

---

## Post-Launch (Week 1)

- [ ] Update `metrics/dashboard.md` with real data
- [ ] Log any new decisions from launch feedback
- [ ] Decide on Sprint 3 scope (CSV export? Auth?)

---

## Known Risks at Launch

| Risk | Mitigation |
|------|-----------|
| No auth on `/admin` | Documented in `decisions/log.md` (DEC-001) |
| SQLite not concurrent | Demo is local-only; not a concern |
| No rate limiting on form | Acceptable for demo; add in v2 if deployed |
