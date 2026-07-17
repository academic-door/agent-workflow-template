# GitHub Agent 协作流程

这份文档说明如何把一个普通 GitHub 仓库改造成适合 Codex、Claude 或其他代码 Agent 协作的仓库。

## 核心思想

Agent 不应该直接改 `main`。它应该像一个谨慎的协作者：

```text
看 Issue
→ 建分支
→ 改代码
→ 跑测试
→ 开 PR
→ 接受 Review
→ 等维护者合并
```

这样做的价值是：

- 每个任务都有上下文。
- 每次修改都有 diff。
- 每个 PR 都能被 CI 检查。
- 你可以让另一个 Agent 做独立 Review。
- 最终发布权仍在维护者手里。

## 第一步：写一个好 Issue

一个适合 Agent 的 Issue 应该包含：

- 背景：为什么要做。
- 允许修改范围：哪些文件可以改。
- 验收标准：怎样算完成。
- 限制：不要做什么。
- 测试建议：希望跑哪些检查。

示例：

```text
标题：
[Agent] 修复中文字体在 PDF 导出时变成方框的问题

背景：
GitHub Actions 的 Ubuntu 环境缺少中文字体，导致 Marp 导出的 PDF 中文显示异常。

允许修改：
- .github/workflows/
- scripts/
- tests/

验收标准：
- [ ] CI 能安装中文字体
- [ ] 中文 Markdown 能成功构建
- [ ] PDF 不出现方框
- [ ] 不包含个人邮箱、密钥、本地路径

限制：
不要改项目品牌，不要公开仓库。
```

## 第二步：让 Agent 接任务

在 Codex 或 Claude 中发出明确指令：

```text
请处理 GitHub 仓库 OWNER/REPO 的 Issue #12。

要求：
1. 从 main 创建分支 agent/issue-12
2. 只修改 Issue 允许的文件
3. 完成测试
4. 推送分支并创建 Pull Request
5. 不要直接修改 main
6. 不要公开仓库
```

仅仅创建 Issue 通常不会自动触发 Agent。你需要在 Codex、Claude 或对应 GitHub 集成里明确让它处理这个 Issue。

## 第三步：看 PR

重点看五件事：

- 修改是否解决 Issue。
- 修改是否超出范围。
- CI 是否通过。
- 是否出现隐私信息。
- 是否需要你做研究判断或发布判断。

## 第四步：让另一个 Agent Review

你可以让另一个 Agent 只做 Review，不做实现：

```text
请 Review OWNER/REPO 的 PR #13。

重点检查：
1. 是否满足 Issue #12 的验收标准
2. 是否有隐私泄露
3. 是否有过度修改
4. 测试是否足够
5. 合并前需要人类确认什么
```

## 第五步：人类合并

维护者最终确认：

- 代码可以合并。
- 研究判断没有问题。
- 公开风险可接受。
- 版本发布节奏合适。

然后再合并到 `main`。

