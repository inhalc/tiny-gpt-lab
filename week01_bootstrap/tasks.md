# 第 1 周 - 启动周任务清单

请先阅读：

1. [`../README.md`](../README.md)
2. [`../docs/setup.md`](../docs/setup.md)

第 1 周目标：配好环境，练习 GitHub 工作流，跑通一个简单的 PyTorch 训练循环，并记录你的观察。

---

## 任务清单

### 1. 环境配置

- [ ] 安装 Git
- [ ] 安装 VS Code 或其他代码编辑器
- [ ] 安装 Conda 或其他 Python 环境管理工具
- [ ] 为本实验室创建一个 Python 环境
- [ ] 安装 PyTorch
- [ ] 按照 [`../docs/setup.md`](../docs/setup.md) 完成环境检查

明确产出：

- 在你的提交 `README.md` 中记录 Python 版本、PyTorch 版本，以及 CUDA 是否可用。

### 2. GitHub 工作流练习

- [ ] Clone 本仓库
- [ ] 创建一个名为 `week1-yourname` 的分支
- [ ] 在你的第 1 周提交文件里做一个小修改
- [ ] Commit 你的修改
- [ ] Push 你的分支
- [ ] 向 `main` 打开一个 Pull Request

明确产出：

- 一个从第 1 周分支指向 `main` 的 Pull Request。

### 3. 运行 starter 训练循环

- [ ] 打开 [`starter_code/train.py`](starter_code/train.py)
- [ ] 运行这个脚本
- [ ] 确认 loss 会随着训练过程变化
- [ ] 修改一次 learning rate
- [ ] 再运行一次脚本
- [ ] 对比两次运行结果

明确产出：

- 在 `experiment.md` 中记录你运行的命令、尝试过的 learning rate，以及 loss 发生了什么变化。

### 4. 写实验记录

- [ ] 把 [`submission_template/experiment.md`](submission_template/experiment.md) 复制到你自己的提交文件夹
- [ ] 填写实验目标
- [ ] 填写实验设置
- [ ] 记录至少一个结果
- [ ] 写下一条观察
- [ ] 写下一个问题或下一步计划

明确产出：

- 一个填写完成并包含在 Pull Request 中的 `experiment.md`。

### 5. 准备第 1 周提交

- [ ] 把 [`submission_template/README.md`](submission_template/README.md) 复制到你自己的提交文件夹
- [ ] 填写你的姓名
- [ ] 总结你完成了什么
- [ ] 链接或说明你的实验记录
- [ ] 列出你遇到的问题

明确产出：

- 一个填写完成并包含在 Pull Request 中的提交 `README.md`。

---

## 最终提交检查

打开 Pull Request 之前，确认它包含：

- [ ] 你填写完成的提交 `README.md`
- [ ] 你填写完成的 `experiment.md`
- [ ] 你对 [`starter_code/train.py`](starter_code/train.py) 做的小修改
- [ ] 一段 PR 描述，说明你运行了什么、修改了什么、观察到了什么、还有什么问题

## 讨论问题

请准备讨论：

- 为什么 loss 会下降？
- `backward()` 做了什么？
- 为什么要调用 `zero_grad()`？
- 为什么 `w` 和 `b` 要设置 `requires_grad=True`？
- 如果 learning rate 太大，可能会发生什么？
