# FeedbackLoop

A dead-simple product feedback collector built with Flask + SQLite. Designed to demonstrate the [AI Product OS](https://github.com/anthropics/ai-products-os) agentic PM workflow in practice.

## What it is

FeedbackLoop lets you:
- **Browse products** — card grid with average ratings
- **Leave reviews** — 1–5 star rating + comment, no account required
- **View all feedback** — admin table, newest first

It's intentionally minimal: one Python file, one CSS file, one JS file. The interesting part is the `product-os/` folder.

## How to run

```bash
git clone <repo-url>
cd review-user-feedback

pip install flask
python app.py        # starts on http://localhost:5000

# In another terminal:
python seed.py       # seeds 6 products + 20 feedback entries
```

Visit `http://localhost:5000`.

## Repo structure

```
review-user-feedback/
├── app.py              ← All Flask routes + DB logic
├── schema.sql          ← SQLite schema (auto-initialized)
├── seed.py             ← Seeds 6 products + 20 reviews
├── requirements.txt
├── templates/          ← Jinja2 HTML templates
├── static/             ← CSS (GitHub dark theme) + JS (star widget)
└── product-os/         ← PM layer — the actual demo
    ├── PRODUCT-CONTEXT.md      ← Read this first
    ├── strategy/               ← Vision, OKRs, competitive analysis
    ├── prd/                    ← PRDs for each feature
    ├── sprints/                ← Sprint plans (1 complete, 1 active)
    ├── decisions/              ← Decision log (3 entries)
    ├── metrics/                ← Framework + dashboard
    ├── launches/               ← Launch checklist
    └── retros/                 ← Sprint 1 retrospective
```

## How the PM workflow works

Every code file in this repo was written **after** its corresponding PM document:

| Code | PM Doc written first |
|------|---------------------|
| `app.py` `POST /api/feedback` | `product-os/prd/feedback-submission.md` |
| `templates/index.html` | `product-os/prd/product-listing.md` |
| `templates/admin.html` | `product-os/prd/admin-dashboard.md` |
| `schema.sql` | `product-os/PRODUCT-CONTEXT.md` (constraints section) |

**Build order (Sprint 1 → Sprint 2):**

1. Fill in `product-os/PRODUCT-CONTEXT.md` — define the product, team, constraints
2. Write `strategy/okrs.md` — set measurable goals before writing any code
3. Write `decisions/log.md` — document SQLite, no-auth, vanilla JS decisions up front
4. Write PRDs (`prd/`) — define acceptance criteria before implementation
5. Write `schema.sql` — data model follows from PRDs
6. Write `app.py` — routes follow from acceptance criteria
7. Write templates — UI follows from user stories

This sequence is enforced by discipline, not tooling. The sprint files (`sprints/`) show which stories were in which sprint.

## AI Product OS connection

This repo uses the [AI Product OS](https://github.com/anthropics/ai-products-os) hub model (Option 4):

- Templates live in `~/ai-products-os/` — never copied into this repo
- `product-os/` contains only filled-in files specific to this project
- `CLAUDE.md` tells AI agents where to find context and how to work in this repo

To use AI Product OS in your own project:
```bash
cp -r ~/ai-products-os/08_blueprint/product-os/ ~/your-project/product-os/
# Then fill in product-os/PRODUCT-CONTEXT.md
```

## Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Product listing (card grid) |
| GET | `/product/<id>` | Product detail + feedback form |
| GET | `/admin` | All feedback (no auth) |
| POST | `/api/feedback` | Submit feedback (JSON) |

## API

```bash
curl -X POST http://localhost:5000/api/feedback \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "rating": 5, "comment": "Great product!", "reviewer_name": "Alex"}'
# → {"success": true, "id": 21}
```
