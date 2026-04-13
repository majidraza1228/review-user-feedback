# FeedbackLoop — Competitive Analysis

**Date:** 2026-04-07
**Analyst:** PM Agent
**Confidence:** Medium

---

## Landscape

| Tool | Type | Strength | Weakness | Relevance |
|------|------|----------|----------|-----------|
| **Canny** | SaaS | Feature voting, roadmap integration | Expensive ($400/mo), overkill for solo PMs | High — closest analog |
| **Typeform** | SaaS | Beautiful forms, flexible | Not product-specific, no admin view | Medium |
| **UserVoice** | SaaS | Enterprise feature management | Very expensive, complex | Low |
| **Google Forms** | Free SaaS | Zero setup | No product catalog, no ratings, ugly | Medium |
| **Hotjar** | SaaS | Session recording + surveys | Priced per volume, overkill | Low |
| **GitHub Issues** | Free | Already in dev workflow | No ratings, no UX for non-devs | Low |

---

## Our Differentiators

1. **Zero cost** — runs locally, no subscription
2. **Zero ops** — single `python app.py` command
3. **PM workflow built in** — `product-os/` is part of the repo, not a separate tool
4. **Legible code** — intended to be read, not just run

---

## Where We Lose

- No real-time notifications
- No auth (by design for v1)
- No CSV/export
- No multi-user collaboration

---

## Conclusion

FeedbackLoop is not competing with Canny — it's competing with **"I'll just use a Google Form."** The win condition is: structured feedback with a product catalog, runnable in 5 minutes, zero SaaS dependency.
