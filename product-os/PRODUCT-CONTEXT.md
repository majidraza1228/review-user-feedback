# FeedbackLoop — Product Context

> Read this first. This is the master brief for all AI agents working on this project.

## Product Overview

| Field | Value |
|-------|-------|
| **Product Name** | FeedbackLoop |
| **One-liner** | Simple product feedback collector for solo PMs and small teams |
| **Phase** | Build (Sprint 2 active) |
| **Started** | 2026-04-07 |
| **Target Launch** | 2026-04-28 |
| **Repo** | `~/review-user-feedback/` |

## Problem

Solo PMs and indie developers have no lightweight way to collect structured feedback on multiple products in one place. Existing tools (Typeform, Canny) are overbuilt for early-stage use.

## Solution

A dead-simple web app: list your products, collect 1–5 star ratings + comments, view all feedback in an admin table. No auth, no config — clone and run.

## Users

| User | Need |
|------|------|
| Solo PM / indie dev | Collect feedback on 1–6 products without a SaaS subscription |
| Reviewer / tester | Leave a quick rating + comment on a product |
| AI agents (meta) | Read this context to understand what to build next |

## Team

| Role | Agent/Human |
|------|-------------|
| PM | Human (Syed) |
| PM Agent | Claude (strategy, PRDs, decisions) |
| Engineer Agent | Claude (code review, implementation guidance) |
| Data Agent | Claude (metrics framework, dashboard) |
| QA Agent | Claude (acceptance criteria validation) |

## Tech Stack

| Layer | Choice |
|-------|--------|
| Backend | Python 3.11 + Flask |
| Database | SQLite (`database.db`, git-ignored) |
| Frontend | Jinja2 + Vanilla HTML/CSS/JS |
| Dependency | `flask>=3.0` only |

## Constraints

- Zero infrastructure — runs on `python app.py`
- No JavaScript frameworks — keep the code legible
- No auth in v1 — documented trade-off, not an oversight (see `decisions/log.md`)
- Must be cloneable and runnable in < 5 minutes

## Current State

- Sprint 1 complete: repo scaffolded, all PM docs written, schema defined
- Sprint 2 active: building product listing, feedback form, admin view
- Sprint 3 planned: launch prep, README, retro

## Success Criteria

- Developer can clone repo, run `python app.py`, and submit feedback in < 5 minutes
- All `product-os/` files are filled in — zero `[FILL IN]` placeholders
- PM workflow (docs → code) is legible to a developer reading the repo cold

## Hub Reference

| Resource | Location |
|----------|---------|
| Hub repo (templates) | https://github.com/majidraza1228/ai-products-os |
| Local hub clone | `~/ai-products-os/` |
| Blueprint to copy | `~/ai-products-os/08_blueprint/product-os/` |
| This project repo | https://github.com/majidraza1228/review-user-feedback |

Never duplicate template content here. Fill in `product-os/` files only.
