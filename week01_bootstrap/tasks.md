# Week 1 Bootstrap

工作目录：

```text
week01_bootstrap/workspace/
```

最终留下：

- `workspace/README.md`
- `workspace/experiment.md`
- `workspace/train.py`

不改：

- `main`
- `starter_code/`

## 0. 准备

```bash
git checkout -b week1-bootstrap
mkdir -p week01_bootstrap/workspace
cp week01_bootstrap/submission_template/README.md week01_bootstrap/workspace/README.md
cp week01_bootstrap/submission_template/experiment.md week01_bootstrap/workspace/experiment.md
cp week01_bootstrap/starter_code/train.py week01_bootstrap/workspace/train.py
```

## 1. 环境

```bash
python --version
git --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

记录到：

- `workspace/README.md`

记：

- Python 版本
- PyTorch 版本
- CUDA 是 `True` 还是 `False`

`CUDA False` 不一定有问题，看是不是在 GPU 机器上跑。

## 2. 跑 train.py

```bash
python week01_bootstrap/workspace/train.py
```

记录到：

- `workspace/experiment.md`

记：

- 命令
- learning rate
- loss 变化
- 观察

## 3. 改 learning rate

只改：

```text
week01_bootstrap/workspace/train.py
```

不要改：

```text
week01_bootstrap/starter_code/train.py
```

把参数更新里的 `0.1` 改成另一个值，例如：

- `0.01`
- `1.0`

再跑：

```bash
python week01_bootstrap/workspace/train.py
```

记录到：

- `workspace/experiment.md`

至少写两次：

- 原始 learning rate
- 修改后的 learning rate

## 4. 补工作记录

填写：

- `workspace/README.md`

写：

- 完成了什么
- 改了什么
- 看到什么
- 卡在哪里
- 周五想讨论什么

## 5. 提交

```bash
git add week01_bootstrap/workspace
git commit -m "week1 bootstrap"
git push -u origin week1-bootstrap
```

PR：

- base：`main`
- branch：`week1-bootstrap`
- title：`Week 1 Bootstrap`

PR 里写：

- 跑了什么
- 改了什么
- 观察到什么
- 卡在哪里

## 周五讨论

- loss 为什么会下降
- `backward()` 做了什么
- 为什么要 `zero_grad()`
- 为什么 `w` / `b` 要 `requires_grad=True`
- learning rate 变大或变小时，loss 怎么变
