# GitHub Agent Workflow Template

[中文](README.md) | English

A reusable, auditable workflow for collaborating with AI coding agents on GitHub.

The template organizes task definition, branch-based implementation, automated checks, review, and human approval into one repeatable process:

```text
Issue defines the goal and acceptance criteria
→ Agent implements on an isolated branch
→ Pull Request proposes the change
→ GitHub Actions run automated checks
→ Agent or human reviews the change
→ Maintainer confirms risk
→ Merge into main
```

## Use Cases

- Involving Codex, Claude Code, or other cloud agents in repository work.
- Requiring every agent change to go through a branch and Pull Request.
- Defining file scope, acceptance criteria, and privacy boundaries before implementation.
- Running tests, repository hygiene checks, and commit-email checks automatically.
- Reusing the same collaboration policy across software, research tools, websites, data pipelines, and templates.

## Included Capabilities

- **Issue template:** records the objective, context, allowed files, acceptance criteria, and privacy requirements.
- **Agent policy:** `AGENTS.md` defines scope, validation, and prohibited actions.
- **Pull Request template:** requests a change summary, test results, risk notes, and privacy confirmation.
- **Automated checks:** GitHub Actions run tests and repository hygiene checks.
- **Branch protection:** can require passing CI, at least one approval, and resolved review conversations before merge.

## Scope and Boundaries

Cloud agents are suited to repository-native code, documentation, configuration, tests, and Pull Requests. They generally cannot access proprietary data, desktop environments, or private files that have not been uploaded; use a tool with the required local access for those tasks. Maintainers remain responsible for business decisions, data privacy, and release risk.

This template contains no personal projects, credentials, private data, or local paths. After copying it, add the build and test commands specific to the target repository.

## Quick Start

Copy these files into the target repository:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/agent-task.yml
.github/pull_request_template.md
.github/workflows/tests.yml
docs/github-agent-workflow.zh-CN.md
scripts/check_commit_emails.py
tests/test_commit_emails.py
```

Then:

1. Create an Issue with the `Agent Task` template.
2. Ask Codex or Claude to create an isolated branch from `main` for that Issue.
3. Require the agent to stay within the allowed scope, run tests, and open a Pull Request.
4. Inspect the diff, Actions results, and review feedback.
5. Merge only after the maintainer confirms correctness, privacy, and release risk.

See [GitHub Agent Workflow](docs/github-agent-workflow.zh-CN.md) for configuration details.

## Contributor Records

GitHub generally attributes Contributors from commits that reach the default branch and have an author identity associated with a GitHub account. A cloud Codex code review, Issue comment, or Actions run does not automatically create a Contributor named “Codex”. The Contributor view is therefore not the acceptance criterion for this template; Issues, Pull Requests, CI, and review records are the primary workflow artifacts.

## License

This template is released under the [MIT License](LICENSE). You may copy, modify, and integrate it into your projects while retaining the license notice.
