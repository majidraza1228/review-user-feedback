# FeedbackLoop — Project CLAUDE.md

> Demo project for AI Product OS. Every code file was written AFTER its PM doc — the repo makes the agentic PM workflow concrete.

## What This Project Is

FeedbackLoop is a product feedback collector built to demonstrate the **AI Product OS** hub model (Option 4) in action.

- The `product-os/` folder is fully filled in — no `[FILL IN]` placeholders
- PM docs (PRDs, OKRs, decisions) were written **before** the corresponding code
- AI agents can read this project cold and understand what to build next

## Product Layer

This project uses AI Product OS. Templates live at `~/ai-products-os/`.
Filled-in product files live in `product-os/` in this repo.

| File | Purpose |
|------|---------|
| `product-os/PRODUCT-CONTEXT.md` | Master brief — read this first |
| `product-os/ai-team.md` | AI agent role assignments |
| `product-os/prd/` | Feature PRDs |
| `product-os/sprints/current.md` | Active sprint |
| `product-os/metrics/dashboard.md` | Live metrics snapshot |
| `product-os/decisions/log.md` | All logged decisions |

Templates (do not edit): `~/ai-products-os/`

## Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Backend | Python 3.11 + Flask | Minimal boilerplate |
| DB | SQLite (`database.db`) | Zero ops, single file |
| Frontend | Jinja2 + Vanilla HTML/CSS/JS | Legible, no build step |

**Run locally:**
```bash
pip install flask
python app.py        # starts on http://localhost:5000
python seed.py       # seeds 6 products + 20 feedback entries
```

## Agent Instructions

1. Read `product-os/PRODUCT-CONTEXT.md` first — it defines the product, team, and constraints
2. Check `product-os/sprints/current.md` for active work
3. Reference `product-os/prd/` before adding any feature
4. Log every non-trivial decision in `product-os/decisions/log.md`
5. Templates live in `~/ai-products-os/` — never copy template content into this repo

## Key Files

```
app.py          ← All Flask routes + DB logic
schema.sql      ← SQLite schema
seed.py         ← Seed data
templates/      ← Jinja2 HTML templates
static/         ← CSS + JS
product-os/     ← PM layer (fully filled in)
```
