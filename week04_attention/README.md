# week04_attention

## 目标

理解并实现 **因果 self-attention**（带 mask），通过单元测试。

## 改哪里

- [`gpt_lab/models/attention.py`](../gpt_lab/models/attention.py) — 重点 `CausalSelfAttention`
- 对照 [`tests/test_attention.py`](../tests/test_attention.py)

## 运行

```bash
make test
```

或：

```bash
pytest tests/test_attention.py -q
```

## 背景（自包含）

- 对每个位置 \(t\)，用 \(Q,K,V\) 算注意力，但 **不能看见未来 token**（`tril` mask）。
- 多头 = 把通道拆成多组独立 attention，再拼回去。

## 完成标准

- `pytest` 全绿
- 在 `notes.md` 用一两句话解释 mask 的作用

## 提交

[`docs/workflow.md`](../docs/workflow.md)
