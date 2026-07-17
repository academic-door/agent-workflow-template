# GitHub Agent Workflow Template

中文 | [English](README.en.md)

用于在 GitHub 上建立可审计、可复用的 AI Agent 协作流程。

本模板将任务定义、分支开发、自动检查、代码审查和人工合并组织成统一流程：

```text
Issue 定义目标与验收标准
→ Agent 在独立分支实现
→ Pull Request 提交变更
→ GitHub Actions 自动检查
→ Agent 或人工 Review
→ 维护者确认风险
→ 合并到 main
```

## 适用场景

- 需要让 Codex、Claude Code 等云端 Agent 参与仓库开发。
- 希望所有 AI 变更都经过分支和 Pull Request，而不是直接修改 `main`。
- 需要在任务开始前明确修改范围、验收标准和隐私边界。
- 希望用 GitHub Actions 自动执行测试、文档检查和提交邮箱检查。
- 需要将同一套协作约定复制到多个软件、研究工具、网站、数据管道或模板仓库。

## 核心能力

- **Issue 模板：** 统一记录目标、背景、允许修改的文件、验收标准和隐私要求。
- **Agent 约定：** 通过 `AGENTS.md` 规定工作范围、验证方式和禁止事项。
- **Pull Request 模板：** 要求提交变更摘要、测试结果、风险说明和隐私确认。
- **自动检查：** 对测试、仓库卫生和提交邮箱执行 GitHub Actions 检查。
- **分支保护：** 可要求 CI 通过、至少 1 次批准并解决全部 Review 对话后才能合并。

## 工作边界

云端 Agent 适合处理仓库内的代码、文档、配置、测试和 Pull Request。它通常无法访问本地电脑上的数据、PDF、图片、Stata 环境或未上传的私有文件；这些任务应由本地 Agent 完成。无论使用哪种 Agent，研究结论、数据隐私和发布风险都应由维护者最终确认。

本模板不包含任何个人项目、凭据、邮箱、私有数据或本地路径。复制模板后，请根据目标仓库补充项目自身的构建命令和测试命令。

## 快速应用

将下列文件复制到目标仓库：

```text
AGENTS.md
.github/ISSUE_TEMPLATE/agent-task.yml
.github/pull_request_template.md
.github/workflows/tests.yml
docs/github-agent-workflow.zh-CN.md
scripts/check_commit_emails.py
tests/test_commit_emails.py
```

然后按以下顺序使用：

1. 使用 `Agent Task` 模板创建 Issue，写明目标、范围和验收标准。
2. 在 Codex 或 Claude 中指定仓库和 Issue 编号，要求从 `main` 创建独立分支。
3. 要求 Agent 只修改 Issue 允许范围内的文件，运行测试并创建 Pull Request。
4. 查看 Pull Request 的 diff、Actions 检查结果和 Review 意见。
5. 由维护者确认代码正确性、研究判断、隐私和发布风险后合并。

更完整的配置说明见 [GitHub Agent 协作流程](docs/github-agent-workflow.zh-CN.md)。

## Contributor 记录

GitHub Contributors 通常根据进入默认分支的提交作者归属计算。云端 Codex 的代码审查、Issue 评论或 Actions 运行不会自动产生一个名为 “Codex” 的 Contributor；只有当某个可识别的 GitHub 身份以其关联邮箱提交代码，并且提交进入默认分支时，才可能显示在 Contributors 中。因此，Contributor 图标不是本模板的验收标准，Issue、Pull Request、CI 和 Review 记录才是协作流程的核心产物。

## 许可证

本模板采用 [MIT License](LICENSE)。你可以复制、修改和集成到自己的项目中，并应保留许可证声明。
