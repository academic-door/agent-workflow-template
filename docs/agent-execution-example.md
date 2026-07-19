# Cloud Agent Execution Example

This document records a generic end-to-end example of a cloud coding agent
completing a task in this repository, following the workflow defined in
`AGENTS.md`.

## Workflow Overview

```text
Issue → Branch → Commits → Pull Request → Actions (CI) → Review → Merge
```

## Step by Step

1. **Issue** — The agent starts from a maintainer-written Issue that defines
   the goal, the allowed file scope, and the acceptance criteria. The agent
   must read it before touching any file.
2. **Branch** — The agent creates an isolated branch from `main`
   (e.g. `agent/issue-N`). It never commits to `main` directly.
3. **Commits** — The agent makes the smallest change that satisfies the
   acceptance criteria, restricted to the allowed scope. Commits use noreply
   email addresses and may carry agent co-author trailers for transparent
   attribution.
4. **Pull Request** — The agent opens a PR using the repository PR template,
   links the Issue, declares its agent role, and confirms the scope and
   privacy checklists.
5. **Actions (CI)** — Automated checks run on the PR: unit tests, commit
   email checks, and repository hygiene checks. A failing check blocks the
   merge.
6. **Review** — A human maintainer (optionally assisted by a second reviewing
   agent) inspects the diff, CI results, and privacy boundaries.
7. **Merge** — Only the maintainer merges. The agent never merges its own PR
   unless explicitly asked.

## Privacy Boundaries

This example intentionally contains no personal project names, credentials,
personal email addresses, local absolute paths, or private data, as required
by the repository privacy rules.
