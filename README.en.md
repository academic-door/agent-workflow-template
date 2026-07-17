# GitHub Agent Workflow Template

[中文](README.md) | English

This repository is a template for building a reviewable GitHub workflow with cloud coding agents such as Codex or Claude.

The goal is not to let an agent freely change your main branch. The goal is to make agent work visible, scoped, tested, reviewed, and merged by a human maintainer.

```text
Issue defines the task
→ Agent implements on a branch
→ Pull Request
→ GitHub Actions checks
→ Agent or human review
→ Maintainer confirms risk
→ Merge to main
```

## Who This Is For

Use this template if:

- You want Codex or Claude to collaborate on GitHub repositories.
- You want every agent task to start from a structured Issue.
- You want agents to work on branches instead of directly changing `main`.
- You want CI to check tests and commit email hygiene.
- You want a repeatable process for research tools, websites, data pipelines, or template repositories.

## What This Is Not

- It is not a GitHub contribution graph automation script.
- It does not publish your private repository.
- It does not give an agent access to your GitHub password or local files.
- It does not replace human review for research judgment, data privacy, or release decisions.

## Cloud Agents vs Local Agents

Cloud agents are useful for repository-native work:

- reading GitHub Issues and Pull Requests
- editing repository files
- creating branches and PRs
- running repository tests
- reviewing code changes

Local agents are useful when the work depends on your computer:

- local data
- PDFs and images on disk
- Stata or other desktop software
- private files that should not be uploaded to GitHub

## Quick Start

Copy these files into your repository:

```text
AGENTS.md
.github/ISSUE_TEMPLATE/agent-task.yml
.github/pull_request_template.md
.github/workflows/tests.yml
docs/github-agent-workflow.zh-CN.md
scripts/check_commit_emails.py
tests/test_commit_emails.py
```

Then create an Issue with the Agent Task template and ask your agent to implement it on a branch and open a PR.

## License

This template uses the MIT License by default.

