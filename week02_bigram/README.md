# week02_bigram

## 目标

在 `gpt_lab` 里实现并理解 **字符级 bigram 语言模型**，能训练、看 loss、采样生成。

## 改哪里

- [`gpt_lab/models/bigram.py`](../gpt_lab/models/bigram.py) — `forward` / `sample`（可先读骨架再自己改一版）
- 可选：[`gpt_lab/data.py`](../gpt_lab/data.py) — 理解 `get_batch` 怎么切 `(x, y)`

## 运行

先准备数据（见 [`data/README.md`](../data/README.md)），然后：

```bash
make train CONFIG=dev STAGE=bigram
```

或：

```bash
python -m gpt_lab.train --config configs/dev.yaml --stage bigram
```

## 建议尝试

- 改 `configs/dev.yaml` 里的 `lr`、`max_steps`
- 在 `experiment.md` 记两次运行的 `train_loss` / `val_loss`
- 用 `BigramLM.sample` 或自己写几行脚本打印 200 个字符

## 完成标准

- 命令能跑通，`device=` 合理
- val loss 相对第一步有下降（或能解释为什么没降）
- `experiment.md` / `notes.md` 已更新

## 提交

[`docs/workflow.md`](../docs/workflow.md)
