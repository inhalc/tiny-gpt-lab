# week07_train_loop

## 目标

完善 **训练管线**：稳定训更久、保存 checkpoint、记录指标。模型文件仍用 week05/06 的 `gpt.py`。

## 改哪里

- [`gpt_lab/train.py`](../gpt_lab/train.py) — AdamW 参数、grad clip、lr（可按需加 warmup/decay）
- [`configs/dev.yaml`](../configs/dev.yaml) — `max_steps`、`eval_interval`

## 运行

```bash
make train CONFIG=dev STAGE=gpt2
```

权重输出：`checkpoints/dev/latest.pt`

建议把指标摘要记在 `runs/`（本地，可不提交）或 `experiment.md`。

## 完成标准

- 存在 `checkpoints/dev/latest.pt`
- loss 曲线整体下降或能解释平台期
- `experiment.md` 至少 2 组超参对比

## 可选（有 GPU 时）

- 增大 `max_steps`
- 尝试 `gpt2_124m` 短训（注意显存）

## 提交

[`docs/workflow.md`](../docs/workflow.md)
