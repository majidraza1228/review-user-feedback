# FeedbackLoop — AI Team Roster

> AI agents assigned to this project. Role definitions live in `~/ai-products-os/07_ai_team/`.

## Active Agents

| Agent | Model | Primary Responsibility | Current Focus |
|-------|-------|----------------------|---------------|
| PM Agent | Claude Sonnet 4.6 | Strategy, PRDs, sprint planning, decisions | Sprint 2 planning |
| Engineer Agent | Claude Sonnet 4.6 | Code review, implementation guidance, schema design | Flask routes + templates |
| Data Agent | Claude Sonnet 4.6 | Metrics framework, dashboard, feedback analysis | Metrics framework |
| QA Agent | Claude Sonnet 4.6 | Acceptance criteria, edge case validation | Feedback form validation |

## Handoff Protocol

1. PM Agent writes the PRD → Engineer Agent implements
2. QA Agent validates acceptance criteria → PM Agent marks story done
3. Data Agent tracks metrics → PM Agent reviews in weekly review
4. All agents log non-trivial decisions in `decisions/log.md`

## Agent Context Loading Order

When starting a new session on this project:
1. Read `PRODUCT-CONTEXT.md` (this project's brief)
2. Read `sprints/current.md` (what's in flight)
3. Read relevant PRD from `prd/` (what you're building)
4. Check `decisions/log.md` (what's already been decided)
