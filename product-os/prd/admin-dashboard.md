# PRD: Admin Dashboard

**Feature:** All-feedback table at `/admin`
**Status:** Approved
**Author:** PM Agent
**Date:** 2026-04-07
**Implements:** `app.py` route `GET /admin`, `templates/admin.html`

---

## Problem

The PM needs to see all feedback across all products in one place. Visiting each product page individually doesn't scale, even with 6 products.

## Solution

A single table at `/admin` showing every feedback entry: product name, reviewer name, rating (as stars), comment, and timestamp. Sorted newest first.

## Acceptance Criteria

| # | Criteria |
|---|----------|
| AC1 | All rows in `feedback` table are shown, joined with product name |
| AC2 | Columns: Product, Reviewer, Rating (★ symbols), Comment, Submitted |
| AC3 | Sorted by `created_at DESC` (newest first) |
| AC4 | No authentication required (documented trade-off in `decisions/log.md`) |
| AC5 | Empty state: if no feedback exists, show "No feedback yet. Seed the database with `python seed.py`." |

## Out of Scope (v1)

- Auth / access control
- Filtering by product or rating
- Exporting to CSV
- Deleting entries
