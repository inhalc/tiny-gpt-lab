# week08_generate

## 目标

用训练好的 checkpoint **生成文本**，并（可选）对接已有 UI。

## 改哪里

- [`gpt_lab/sample.py`](../gpt_lab/sample.py) — temperature、`top_k`
- 可选：[`integration-ui.md`](integration-ui.md)

## 运行

```bash
make sample CONFIG=dev PROMPT="ROMEO:"
```

调参示例：

```bash
python -m gpt_lab.sample --config configs/dev.yaml \
  --ckpt checkpoints/dev/latest.pt \
  --prompt "HELLO" --temperature 1.0 --top-k 50
```

## 完成标准

- 同一 checkpoint，至少 2 种 `temperature` 的生成结果写入 `experiment.md`
- 能说明采样时逐步发生了什么（从 logits 到下一个 token）

## 项目终点

此时 `gpt_lab` 应具备：**GPT-2 架构 + 训练环 + 采样**。124M 长时间训练为可选项，见 week07 notes。

## 提交

[`docs/workflow.md`](../docs/workflow.md)
