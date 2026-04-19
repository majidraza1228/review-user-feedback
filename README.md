# FeedbackLoop

A dead-simple product feedback collector built with Flask + SQLite.
This repo is a **fully working demo** of the [AI Product OS](https://github.com/majidraza1228/ai-products-os) agentic PM workflow — every code file was written after its PM document.

---

## How it connects to AI Product OS

```
https://github.com/majidraza1228/ai-products-os   ← Hub: blank templates, agent definitions
https://github.com/majidraza1228/review-user-feedback  ← This repo: filled-in PM docs + working code
```

**AI Product OS** is the hub — it holds blank reusable templates (PRDs, OKRs, sprint plans, metrics frameworks) and AI agent role definitions. You never edit those templates per-project.

**FeedbackLoop** (this repo) is a project that uses that hub. The `product-os/` folder was copied once from the blueprint and then fully filled in for this specific product. No blanks remain.

The relationship in one sentence: **AI Product OS provides the structure; FeedbackLoop proves it works.**

---

## How to set up your own project using AI Product OS

```bash
# Step 1 — Clone the hub locally
git clone https://github.com/majidraza1228/ai-products-os ~/ai-products-os

# Step 2 — Create your project repo
mkdir ~/your-project && cd ~/your-project
git init

# Step 3 — Copy the blueprint into your project (one time only)
cp -r ~/ai-products-os/08_blueprint/product-os/ ~/your-project/product-os/

# Step 4 — Fill in the master brief (this is your starting point)
# Edit: your-project/product-os/PRODUCT-CONTEXT.md

# Step 5 — Add a CLAUDE.md that points agents to the hub
# See CLAUDE.md in this repo as a reference
```

The hub (`~/ai-products-os/`) is never modified per-project. Templates stay blank and generic. Only your `product-os/` folder gets filled in.

---

## How the PM workflow works (docs before code)

Every file in this repo was created in this order:

```
Sprint 1 — PM layer first, zero code
────────────────────────────────────────────────────────
product-os/PRODUCT-CONTEXT.md    ← define product, team, constraints
product-os/strategy/vision.md    ← why this product exists
product-os/strategy/okrs.md      ← measurable goals for Q2 2026
product-os/strategy/competitive-analysis.md
product-os/decisions/log.md      ← 3 decisions logged before coding:
                                    DEC-001 no auth
                                    DEC-002 SQLite over PostgreSQL
                                    DEC-003 vanilla CSS/JS over Tailwind/React
product-os/prd/feedback-submission.md   ← acceptance criteria written
product-os/prd/product-listing.md       ←   before any route exists
product-os/prd/admin-dashboard.md
product-os/metrics/framework.md  ← North Star defined before code
schema.sql                        ← data model follows from PRDs

Sprint 2 — Code, informed by PM docs
────────────────────────────────────────────────────────
app.py           ← routes implement the PRD acceptance criteria
templates/       ← UI implements the user stories
static/          ← styling and star widget
seed.py          ← test data to validate the flow
```

The PM docs are not decoration. Each PRD has:
- A problem statement
- User stories
- Numbered acceptance criteria
- Edge cases + error handling spec
- An API contract (for `feedback-submission.md`)

The code implements those specs exactly. Read `product-os/prd/feedback-submission.md` then `app.py` route `POST /api/feedback` — the mapping is 1:1.

---

## What's in product-os/

```
product-os/
├── PRODUCT-CONTEXT.md          ← Master brief — read this first
├── ai-team.md                  ← 4 AI agent role assignments
├── strategy/
│   ├── vision.md               ← Why FeedbackLoop exists
│   ├── okrs.md                 ← Q2 2026 OKRs with current status
│   └── competitive-analysis.md ← vs Canny, Typeform, Google Forms
├── prd/
│   ├── TEMPLATE.md             ← Blank PRD template from hub (reference)
│   ├── feedback-submission.md  ← Core PRD: star form + API
│   ├── product-listing.md      ← Homepage card grid
│   └── admin-dashboard.md      ← All-feedback table
├── sprints/
│   ├── TEMPLATE.md             ← Blank sprint template from hub
│   ├── sprint-apr-14-26.md     ← Sprint 1 (complete, 25 points)
│   └── current.md              ← Sprint 2 (active)
├── decisions/
│   ├── log.md                  ← DEC-001, DEC-002, DEC-003
│   └── weekly-review.md        ← Week of 2026-04-14
├── metrics/
│   ├── framework.md            ← North Star → Input → Output → Guardrails
│   └── dashboard.md            ← Week 1 baseline (seed data)
├── launches/
│   └── checklist.md            ← Pre-launch, launch day, post-launch
└── retros/
    ├── TEMPLATE.md             ← Blank retro template from hub
    └── sprint-1-retro.md       ← Sprint 1 retrospective
```

The `TEMPLATE.md` files are copied from the hub unchanged — they show what the blank template looks like before being filled in.

---

## Running the app

```bash
git clone https://github.com/majidraza1228/review-user-feedback
cd review-user-feedback

pip install flask
python app.py        # http://localhost:5000

# Second terminal:
python seed.py       # seeds 6 products + 20 reviews
```

---

## App pages

| Route | Page | What it shows |
|-------|------|---------------|
| `GET /` | Product listing | 6 product cards, avg rating, review count |
| `GET /product/<id>` | Product detail | Description, star form, submitted reviews |
| `GET /admin` | Admin dashboard | All feedback across all products, newest first |
| `POST /api/feedback` | JSON API | Accepts rating + comment, validates, stores |

---

## Architecture diagram (Mermaid)

```mermaid
flowchart TD
    A[Browser] -->|GET /| B[index()]
    A -->|GET /product/<id>| C[product(product_id)]
    A -->|GET /admin| D[admin()]
    A -->|POST /api/feedback JSON| E[submit_feedback()]

    subgraph Flask App [Flask app.py]
      B --> T1[render index.html]
      C --> T2[render product.html]
      D --> T3[render admin.html]
      E --> J1[return JSON success/error]
    end

    subgraph Frontend [Templates + Static]
      T1 --> H1[base.html + index.html]
      T2 --> H2[base.html + product.html]
      T3 --> H3[base.html + admin.html]
      H2 --> S1[static/main.js<br/>star widget + fetch]
      H1 --> S2[static/style.css]
      H2 --> S2
      H3 --> S2
    end

    subgraph DB [SQLite database.db]
      P[(products)]
      F[(feedback)]
    end

    B -->|SELECT products + AVG/COUNT feedback| P
    B -->|LEFT JOIN feedback| F
    C -->|SELECT product by id| P
    C -->|SELECT feedback by product_id| F
    D -->|JOIN feedback + products| F
    D -->|JOIN feedback + products| P
    E -->|validate + INSERT feedback| F
    E -->|check product exists| P

    Z[seed.py] -->|INSERT 6 products| P
    Z -->|INSERT 20 feedback rows| F
```

---

## API

```bash
# Submit a review
curl -X POST http://localhost:5000/api/feedback \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "rating": 5, "comment": "Great product!", "reviewer_name": "Alex"}'

# Success
{"success": true, "id": 21}

# Validation errors
{"error": "rating must be between 1 and 5"}
{"error": "comment is required"}
{"error": "product not found"}
```

---

## Seeded products

| ID | Product | Category |
|----|---------|---------|
| 1 | Notion AI | Productivity |
| 2 | Linear | Project Management |
| 3 | Raycast | Developer Tools |
| 4 | Superhuman | Email |
| 5 | Cron | Calendar |
| 6 | Loom | Communication |

---

## Hub vs project — what lives where

| File type | Lives in | Why |
|-----------|---------|-----|
| Blank PRD template | `ai-products-os/08_blueprint/product-os/prd/TEMPLATE.md` | Hub stays generic |
| Filled-in PRD | `review-user-feedback/product-os/prd/feedback-submission.md` | Project-specific |
| Agent role definitions | `ai-products-os/07_ai_team/` | Reused across all projects |
| Decision log | `review-user-feedback/product-os/decisions/log.md` | Project-specific |
| Metrics framework template | `ai-products-os/08_blueprint/product-os/metrics/framework.md` | Hub stays generic |
| Filled-in metrics | `review-user-feedback/product-os/metrics/framework.md` | Project-specific |

The hub is cloned once to `~/ai-products-os/` and shared across all your projects. Each project copies the blueprint once and fills it in independently.

---

## Tech stack

| Layer | Choice | Reason |
|-------|--------|--------|
| Backend | Python + Flask | Minimal boilerplate, one file |
| Database | SQLite | Zero ops, single file (`database.db`) |
| Frontend | Jinja2 + Vanilla HTML/CSS/JS | No build step, fully legible |
| Dependency | `flask>=3.0` only | Clone and run in < 5 min |
