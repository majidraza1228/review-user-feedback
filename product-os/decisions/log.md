# FeedbackLoop — Decision Log

> Log every non-trivial architectural or product decision here. Format: context → options considered → decision → rationale → trade-offs.

---

## DEC-001: No Authentication in v1

**Date:** 2026-04-07
**Status:** Accepted
**Decision Maker:** PM (Syed) + PM Agent

### Context

The admin dashboard at `/admin` exposes all feedback. Should we add auth?

### Options Considered

| Option | Pros | Cons |
|--------|------|------|
| No auth | Zero setup, demo runs immediately | Anyone with the URL can see all feedback |
| Single-password auth (HTTP Basic) | Simple, adds protection | Adds config step, reduces demo legibility |
| Session-based auth (Flask-Login) | Proper UX | Adds dependency, complexity, migration |

### Decision

**No auth in v1.** The admin route is unprotected.

### Rationale

FeedbackLoop is a demo for local use. The threat model is: developer running it on localhost. Adding auth increases setup friction and obscures the core demo value (feedback collection workflow). Auth can be added in v2 if the project extends beyond local use.

### Trade-offs Accepted

- Anyone with server access can read all feedback
- Not suitable for production deployment without adding auth first
- Documented here so future agents don't "fix" the missing auth without understanding the decision

---

## DEC-002: SQLite over PostgreSQL

**Date:** 2026-04-07
**Status:** Accepted
**Decision Maker:** Engineer Agent + PM Agent

### Context

What database should FeedbackLoop use?

### Options Considered

| Option | Pros | Cons |
|--------|------|------|
| SQLite | Zero ops, single file, no server | Not suitable for concurrent writes at scale |
| PostgreSQL | Production-ready, concurrent | Requires server, Docker, or managed DB |
| MySQL | Familiar to many devs | Same ops overhead as PostgreSQL |

### Decision

**SQLite.** Database is a single `database.db` file, git-ignored.

### Rationale

The primary constraint is "runs with `python app.py`, zero infra." SQLite satisfies this completely. At the scale of a demo (6 products, <100 feedback entries), SQLite has no meaningful limitations. Migration to PostgreSQL would require changing 3 lines in `app.py` if needed later.

### Trade-offs Accepted

- Not suitable for concurrent multi-user writes
- Database is local-only (not shareable without copying the file)
- Acceptable for a demo; documented for future agents considering a hosted version

---

## DEC-003: Vanilla CSS/JS over Tailwind/React

**Date:** 2026-04-07
**Status:** Accepted
**Decision Maker:** PM Agent

### Context

Should the frontend use a CSS framework (Tailwind) or JS framework (React/Vue)?

### Options Considered

| Option | Pros | Cons |
|--------|------|------|
| Tailwind CSS | Rapid styling, consistent design | Requires build step or CDN, adds unfamiliar classes |
| React | Component model, reactive state | Massive complexity for a demo, requires Node.js |
| Vanilla CSS + JS | Zero build step, fully readable | More verbose, no component reuse |

### Decision

**Vanilla CSS + JS.** No framework dependencies beyond Flask.

### Rationale

The repo is meant to be read by developers exploring AI Product OS. A Tailwind class soup or React component tree would obscure the actual PM-workflow story we're trying to tell. Vanilla HTML/CSS/JS is immediately legible to any developer without consulting documentation. The star rating widget (the only interactive element) is implemented in < 30 lines of JS.

### Trade-offs Accepted

- CSS is more verbose than Tailwind equivalent
- No component reuse across templates (Jinja2 includes used instead)
- Acceptable: demo code should prioritize legibility over elegance
