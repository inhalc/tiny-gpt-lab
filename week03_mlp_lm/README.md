# week03_mlp_lm

## 目标

用 **带上下文的 MLP** 做语言模型，对比 week02 bigram 的 val loss。

## 改哪里

- [`gpt_lab/models/mlp_lm.py`](../gpt_lab/models/mlp_lm.py)
- [`configs/dev.yaml`](../configs/dev.yaml) — `block_size`、`n_embd`

## 运行

```bash
make train CONFIG=dev STAGE=mlp
```

## 完成标准

- 同数据配置下，**val loss 低于**你在 week02 记录的最好结果（或说明差异原因）
- 更新本目录 `experiment.md`

## 提交

[`docs/workflow.md`](../docs/workflow.md)
