# FeedbackLoop — Project CLAUDE.md

> Demo project for AI Product OS. Every code file was written AFTER its PM doc — the repo makes the agentic PM workflow concrete.

## What This Project Is

FeedbackLoop is a product feedback collector built to demonstrate the **AI Product OS** hub model (Option 4) in action.

- The `product-os/` folder is fully filled in — no `[FILL IN]` placeholders
- PM docs (PRDs, OKRs, decisions) were written **before** the corresponding code
- AI agents can read this project cold and understand what to build next

## How This Project Uses AI Product OS

**Hub repo (templates — do not edit per-project):**
`https://github.com/majidraza1228/ai-products-os`

**This project repo (filled-in files only):**
`https://github.com/majidraza1228/review-user-feedback`

The hub provides blank templates and agent role definitions. This project copied the blueprint once from `ai-products-os/08_blueprint/product-os/` and filled everything in. The two repos stay separate — the hub never gets project-specific content.

## Product Layer

Filled-in product files live in `product-os/` in this repo.

| File | Purpose |
|------|---------|
| `product-os/PRODUCT-CONTEXT.md` | Master brief — read this first |
| `product-os/ai-team.md` | AI agent role assignments for this project |
| `product-os/prd/` | Feature PRDs (feedback form, listing, admin) |
| `product-os/sprints/current.md` | Active sprint |
| `product-os/metrics/dashboard.md` | Live metrics snapshot |
| `product-os/decisions/log.md` | All logged decisions |

Templates (do not edit): `https://github.com/majidraza1228/ai-products-os`
Local clone of hub: `~/ai-products-os/`

## Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Backend | Python + Flask | Minimal boilerplate |
| DB | SQLite (`database.db`) | Zero ops, single file |
| Frontend | Jinja2 + Vanilla HTML/CSS/JS | Legible, no build step |

**Run locally:**
```bash
pip install flask
python app.py        # starts on http://localhost:5000
python seed.py       # seeds 6 products + 20 feedback entries
```

## Agent Instructions

1. Read `product-os/PRODUCT-CONTEXT.md` first — defines the product, team, and constraints
2. Check `product-os/sprints/current.md` for active work
3. Reference `product-os/prd/` before adding any feature
4. Log every non-trivial decision in `product-os/decisions/log.md`
5. For blank templates, fetch from: `https://github.com/majidraza1228/ai-products-os/tree/main/08_blueprint/product-os/`
6. Never copy template content into this repo — fill in your own version in `product-os/`

## Key Files

```
app.py          ← All Flask routes + DB logic
schema.sql      ← SQLite schema (auto-initialized on app.py start)
seed.py         ← 6 products + 20 feedback entries
templates/      ← Jinja2 HTML templates
static/         ← CSS (GitHub dark theme) + JS (star rating widget)
product-os/     ← PM layer — fully filled in, zero [FILL IN] blanks
```

## PM Doc → Code Mapping

| PM Document | Code it specifies |
|-------------|------------------|
| `product-os/prd/feedback-submission.md` | `app.py` `POST /api/feedback` + `templates/product.html` form |
| `product-os/prd/product-listing.md` | `app.py` `GET /` + `templates/index.html` |
| `product-os/prd/admin-dashboard.md` | `app.py` `GET /admin` + `templates/admin.html` |
| `product-os/PRODUCT-CONTEXT.md` (constraints) | `schema.sql` (2 tables, SQLite) |
| `product-os/decisions/log.md` DEC-002 | SQLite in `app.py` (not PostgreSQL) |
| `product-os/decisions/log.md` DEC-003 | `static/style.css` (vanilla, not Tailwind) |
