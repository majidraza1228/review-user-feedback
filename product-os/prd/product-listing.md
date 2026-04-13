# PRD: Product Listing

**Feature:** Homepage product card grid
**Status:** Approved
**Author:** PM Agent
**Date:** 2026-04-07
**Implements:** `app.py` route `GET /`, `templates/index.html`

---

## Problem

Without a product catalog, reviewers have no entry point to the app. They need to see which products are available for review and how each is performing.

## Solution

A card grid on the homepage showing all products with their average star rating, review count, category, and a "Leave a Review" CTA.

## Acceptance Criteria

| # | Criteria |
|---|----------|
| AC1 | All products in the `products` table are rendered as cards |
| AC2 | Each card shows: product name, category, average rating (1 decimal), review count, "Leave a Review" button |
| AC3 | Average rating and review count are computed from the `feedback` table, not hard-coded |
| AC4 | If a product has 0 reviews, show "No reviews yet" instead of a rating |
| AC5 | "Leave a Review" links to `/product/<id>` |
| AC6 | Page loads in < 1 second with 6 products and 20 feedback entries (local SQLite) |

## Out of Scope (v1)

- Sorting or filtering products
- Search
- Pagination
- Adding products via UI (products are seeded via `seed.py`)
