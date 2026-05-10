# GitHub 工作流说明

## 0. 创建或连接 GitHub 仓库（只需要做一次）

如果项目只在本地，GitHub 页面不会自动更新。需要先把本地仓库连接到 GitHub remote。

```bash
# 先在 GitHub 上创建仓库，再把本地仓库连接过去
git remote add origin git@github.com:<your-name>/tiny-gpt-lab.git
# 或者使用 HTTPS: https://github.com/<your-name>/tiny-gpt-lab.git
git branch -M main
git push -u origin main
```

## Git 基本工作流

每次作业都使用自己的 branch，不要直接在 `main` 上改：

```bash
git checkout -b week1-yourname
git add .
git commit -m "finish week1"
git push -u origin week1-yourname
```

## Pull Request (PR) 工作流

- 不要直接 push 到 `main`
- 每次提交作业都打开一个 PR
- 在 PR comments 里讨论问题、解释观察、接受 review
- 把 PR review 当作一次小型科研讨论

## 提交要求

每周提交应包含：

1. `README.md`：说明目标、结果、观察和问题
2. `experiment.md`：结构化实验记录
3. 代码文件：例如 scripts、notebooks 或 configs

## 工作原则

- 记录你改了什么，以及为什么改
- 不只报告最终数字，也要报告观察过程
- 提出可以被测试的问题
- 优先写下可复现步骤，而不是只说“我试了一下”
