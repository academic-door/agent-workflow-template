# Codex 执行示例

本文记录一个由 Codex 直接执行的通用仓库任务，展示从 Issue 到合并的最小闭环。

## 流程

```text
Issue → 独立分支 → 提交 → Pull Request → GitHub Actions → Review → 合并
```

Codex 接到 Issue 后，应先确认目标、允许修改的文件和验收标准，再从最新的 `main` 创建独立分支。实现过程中只修改 Issue 允许范围内的文件，并在本地运行仓库检查。完成后，Codex 应将分支真实推送到 GitHub，创建 Pull Request，并在任务结果中返回可访问的 PR URL。

## 验收要点

- GitHub 远端可以查到 Codex 创建的分支和提交。
- Pull Request 的目标分支为 `main`，且没有直接修改 `main`。
- GitHub Actions 的测试、提交邮箱和仓库卫生检查全部通过。
- Pull Request 描述包含变更范围、测试结果、隐私确认和人工 Review 要求。
- 维护者检查 diff、CI 和公开风险后，使用保留提交作者信息的方式合并。

## 隐私边界

示例不包含个人项目名称、真实邮箱、凭据、私有数据或本地绝对路径。实际任务应把敏感材料留在具备相应访问权限的本地环境中，不要上传到 Issue、Pull Request 或 Actions 日志。

## 署名验证

本节由 Codex 实际生成，用于验证 GitHub 对共同作者尾注的归属规则。共同作者地址只有在 GitHub 能将其匹配到一个已注册的用户或机器人身份时，才会出现在 Contributors 列表中；测试结果不应被解释为对任何身份的手工伪造。
