# FeedbackLoop — Vision

## Vision Statement

Make product feedback collection so frictionless that any solo PM can get structured, actionable input on their products in under 5 minutes — without a SaaS subscription, without ops overhead, without auth complexity.

## Strategic Pillars

### 1. Zero Friction
- One command to run: `python app.py`
- No signup, no config files, no environment variables
- Reviewer leaves feedback in 30 seconds

### 2. Legible by Design
- Code is readable without a framework tutorial
- PM docs map 1:1 to code files
- New agent or developer understands the project in < 10 minutes

### 3. PM Workflow as a Feature
- The repo itself demonstrates the AI Product OS workflow
- Every code file has a corresponding PM doc written first
- Decisions are logged, not assumed

## What This Is Not

- Not a replacement for Canny, Typeform, or UserVoice at scale
- Not a multi-tenant SaaS
- Not a production system (no auth, no rate limiting in v1)

## 12-Month Horizon (if extended)

If this prototype finds traction, extensions in priority order:
1. CSV export of feedback
2. Email notifications on new submissions
3. Simple auth (single password, no user accounts)
4. Tagging / categorization of feedback

All extensions require a new PRD before any code is written.
