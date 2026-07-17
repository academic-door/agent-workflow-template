# GitHub Agent Workflow Template

中文 | [English](README.en.md)

这是一个用于建立 GitHub 云端 Agent 协作流程的模板仓库。

它解决的问题不是“让 AI 随便帮你改代码”，而是把 Codex、Claude Code、GitHub Actions 和人工确认放进一条可审计的工程流程：

```text
Issue 定义目标
→ Agent 创建分支并实现
→ Pull Request
→ GitHub Actions 自动检查
→ 另一个 Agent 或人类 Review
→ 维护者确认风险
→ 合并 main
```

## 适合谁

这个模板适合这些场景：

- 你有多个 GitHub 仓库，希望让 Codex 或 Claude 在云端协作。
- 你希望 AI 改代码时不要直接动 `main`，而是走分支和 PR。
- 你想把“任务目标、允许修改范围、验收标准、隐私限制”写清楚。
- 你希望 GitHub Actions 自动检查测试、文档和提交邮箱。
- 你准备把流程复制到科研项目、工具库、网站、数据管道或模板仓库中。

它尤其适合像 `zju-awesome-marp`、`econpaper2beamer`、`nber-working-papers-cn` 这类持续维护的小型项目：任务不一定每天很大，但每次修改都应该有记录、有检查、有 Review。

## 它不是什么

- 它不是刷 GitHub 绿点的脚本。
- 它不会自动把私有仓库变公开。
- 它不会替你判断研究结论是否正确。
- 它不会让 Agent 获得你的 GitHub 密码或本地电脑文件。
- 它不能防止别人复制开源代码；许可证决定别人能如何使用。

## 云端 Agent 和本地 Agent 的区别

云端 Agent 适合：

- 读写 GitHub 仓库。
- 按 Issue 修改代码。
- 创建分支、提交 commit、开 PR。
- 运行仓库内测试。
- 帮你做代码审查。

本地 Agent 适合：

- 访问你电脑上的数据、图片、PDF、Stata 文件或本地项目。
- 调用本地软件和私有环境。
- 处理不能上传到 GitHub 的材料。

一个健康的做法是：云端 Agent 处理仓库内可公开或可托管的工程任务，本地 Agent 处理本机环境和私有数据。

## 快速开始

1. 复制本模板中的这些文件到你的目标仓库：

```text
AGENTS.md
.github/ISSUE_TEMPLATE/agent-task.yml
.github/pull_request_template.md
.github/workflows/tests.yml
docs/github-agent-workflow.zh-CN.md
scripts/check_commit_emails.py
tests/test_commit_emails.py
```

2. 在目标仓库创建 Issue，使用 `Agent Task` 模板。

3. 在 Codex 或 Claude 中发出任务，例如：

```text
请处理 GitHub 仓库 OWNER/REPO 的 Issue #12。

要求：
1. 从 main 创建分支 agent/issue-12
2. 只修改 Issue 允许范围内的文件
3. 完成测试
4. 推送分支并创建 Pull Request
5. 不要直接修改 main
6. 不要公开仓库
```

4. 等 Agent 创建 PR 后，检查：

- PR 描述是否完整。
- GitHub Actions 是否通过。
- 修改是否超出 Issue 范围。
- 是否包含真实邮箱、Token、本地路径或私有数据。
- 研究判断、公开风险、发布节奏是否由你确认。

5. 确认无误后再合并。

## 推荐权限

最小权限原则：

- 只给 Agent 访问需要协作的仓库。
- 优先选择 selected repositories，不要默认授权所有仓库。
- 对重要仓库使用 branch protection。
- 要求 PR 通过 CI 后才能合并。
- 私有研究数据不要放进 GitHub Issue、PR 或 Actions 日志。

## Contributor 显示说明

Codex 或 Claude 出现在 Contributors 里，通常表示它们作为 commit author 的提交进入了默认分支。

这只能说明“它参与提交过代码”，不代表：

- 代码一定正确。
- Agent 一直有权限。
- 它理解了所有研究判断。
- 你可以跳过人工审核。

真正重要的是 PR、diff、CI 和 Review 记录。

## 许可证

本模板默认使用 MIT License。MIT 适合工具模板，因为别人可以自由复制、修改和用于自己的仓库。

如果你不希望别人复制核心实现，就不要把核心实现放进开源仓库，或者改用更限制性的许可证。

