# week05_mini_gpt

## 目标

把 attention 拼进 **Transformer**，在 `gpt_lab/models/gpt.py` 里跑通 mini GPT 训练与采样。

## 改哪里

- [`gpt_lab/models/gpt.py`](../gpt_lab/models/gpt.py) — `Block`、`GPT`（可在现有骨架上改）
- [`configs/dev.yaml`](../configs/dev.yaml) — `n_layer`、`n_head`、`n_embd`

## 运行

```bash
make train CONFIG=dev STAGE=gpt
make sample CONFIG=dev PROMPT="ROMEO:"
```

## 完成标准

- 训练 loss 有下降趋势
- `make sample` 能打出字符（未训很久时乱一点正常）
- checkpoint 出现在 `checkpoints/dev/latest.pt`

## 说明

从本周起，**后面几周都在同一个 `gpt.py` 上演进**，不要新建 `week06/model.py` 复制粘贴。

## 提交

[`docs/workflow.md`](../docs/workflow.md)
