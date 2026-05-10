# bootstrap

工作目录：

```text
week01_bootstrap/workspace/
```

这里先留下：

- `workspace/README.md`
- `workspace/experiment.md`
- `workspace/train.py`

不改：

- `main`
- `starter_code/`

## 环境先跑通

看：

- [`../docs/setup.md`](../docs/setup.md)

记到：

- `workspace/README.md`

## 先直接跑

```bash
python week01_bootstrap/workspace/train.py
```

记到：

- `workspace/experiment.md`

## 改一下 learning rate

改：

```text
week01_bootstrap/workspace/train.py
```

不要改：

```text
week01_bootstrap/starter_code/train.py
```

至少跑两次：

- 原始 learning rate
- 修改后的 learning rate

记到：

- `workspace/experiment.md`

## 记一下过程

填：

- `workspace/README.md`

写：

- 做了什么
- 改了什么
- 看到什么
- 卡在哪里
- 后面想一起看的问题

## push 上来

看：

- [`../docs/workflow.md`](../docs/workflow.md)

PR 里带上：

- `workspace/README.md`
- `workspace/experiment.md`
- `workspace/train.py`

有问题直接记下来，push 之后一起看。

改 learning rate 的时候顺便看：

- loss 会不会下降
- loss 会不会震荡
- learning rate 变大或变小时，loss 怎么变
