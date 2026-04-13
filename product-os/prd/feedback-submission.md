# PRD: Feedback Submission

**Feature:** Star rating + comment form on product detail page
**Status:** Approved
**Author:** PM Agent
**Date:** 2026-04-07
**Implements:** `app.py` route `POST /api/feedback`, `templates/product.html`

---

## Problem

Reviewers visiting a product page have no way to record their experience. Without a submission mechanism, the product catalog is read-only and useless for feedback collection.

## Solution

A star rating widget (1–5) plus a comment textarea on each product detail page. Submission hits `POST /api/feedback`, stores to SQLite, and refreshes the review list in-page.

## Users

- **Primary:** Reviewer — wants to rate + comment in < 30 seconds
- **Secondary:** PM — wants to see all feedback in admin view

## User Stories

1. **As a reviewer**, I want to select a star rating and type a comment so that I can record my experience with a product without creating an account.
2. **As a PM**, I want every submission to be stored immediately so that I can see feedback in the admin dashboard without manual steps.

## Acceptance Criteria

| # | Criteria | Pass/Fail |
|---|----------|-----------|
| AC1 | Star rating widget renders 5 interactive stars; selected state is visually distinct | — |
| AC2 | Comment textarea is required; form does not submit if empty | — |
| AC3 | Rating is required (1–5); form does not submit if unselected | — |
| AC4 | Successful submission inserts a row into `feedback` table and returns HTTP 200 + JSON `{success: true, id: <int>}` | — |
| AC5 | After submission, new review appears in the reviews list on the product page without full page reload | — |

## Edge Cases

| Case | Handling |
|------|---------|
| Rating out of range (< 1 or > 5) | Return HTTP 400 `{error: "rating must be between 1 and 5"}` |
| Empty comment | Return HTTP 400 `{error: "comment is required"}` |
| Missing `product_id` | Return HTTP 400 `{error: "product_id is required"}` |
| `product_id` not in DB | Return HTTP 404 `{error: "product not found"}` |
| SQL injection in comment | Parameterized queries via `sqlite3` — not vulnerable |

## API Contract

**Endpoint:** `POST /api/feedback`
**Content-Type:** `application/json`

Request:
```json
{
  "product_id": 1,
  "rating": 4,
  "comment": "Really solid keyboard shortcuts.",
  "reviewer_name": "Alex"
}
```

Success response (HTTP 200):
```json
{"success": true, "id": 42}
```

Error response (HTTP 400):
```json
{"error": "comment is required"}
```

## Success Metric

30% of product page visitors submit at least one piece of feedback per session (measured via `feedback` table inserts vs. `product_id` page views, approximated from seed data ratios).

## Out of Scope (v1)

- Email notifications on submission
- Spam protection / rate limiting
- Reviewer accounts or session tracking
- Editing or deleting submissions
