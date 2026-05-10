# Tiny GPT Lab

一个面向本科生的小型 GPT/LLM 学习实验室，用“动手做”的方式建立基础研究习惯。

项目地址：https://github.com/inhalc/tiny-gpt-lab

## 从这里开始

当前阶段：**第 1 周 - 启动周**

第 1 周入口：[`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)

现阶段，学生只需要先看这三个文件：

1. [`README.md`](README.md)
2. [`docs/setup.md`](docs/setup.md)
3. [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)

## 本周要做什么

- 配好 Python 和 PyTorch 环境
- 练习基本 GitHub 工作流
- 运行并修改一个简单的 PyTorch 训练循环
- 记录一次小实验
- 通过 Pull Request 提交作业

## 最小工作流

```bash
git clone https://github.com/inhalc/tiny-gpt-lab.git
cd tiny-gpt-lab
git checkout -b week1-yourname

# 修改文件、运行代码、记录观察

git add week01_bootstrap
git commit -m "Complete week 1 bootstrap"
git push -u origin week1-yourname
```

然后在 GitHub 上打开 Pull Request：

- Base branch：`main`
- Compare branch：`week1-yourname`
- PR 标题：`Week 1 - Your Name`
- PR 描述：说明你运行了什么、修改了什么、观察到了什么、还有什么问题

## 最后要提交什么

从下面的模板开始创建你的第 1 周提交：

[`week01_bootstrap/submission_template/`](week01_bootstrap/submission_template/)

你的 Pull Request 应该包含：

- 填写完成的提交说明 `README.md`
- 填写完成的实验记录 `experiment.md`
- 你对 `starter_code/train.py` 做的小修改

## 遇到问题怎么记录

遇到卡住的地方时，写下：

- 你尝试了什么
- 你运行了什么命令
- 你看到了什么错误或结果
- 你猜可能是什么原因
- 你想在 review 里问什么

即使实验没有跑通，也要使用 `experiment.md` 模板记录。失败的运行也是有价值的数据。

## 仓库地图

- [`docs/setup.md`](docs/setup.md)：环境配置
- [`docs/workflow.md`](docs/workflow.md)：GitHub 工作流说明
- [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)：第 1 周任务清单
- [`week01_bootstrap/starter_code/train.py`](week01_bootstrap/starter_code/train.py)：PyTorch 训练循环 starter code
- [`week01_bootstrap/submission_template/`](week01_bootstrap/submission_template/)：学生提交模板
