# week06_gpt2_arch

## 目标

把 week05 的 `gpt.py` **对齐 GPT-2 结构规范**（层数、命名、BPE 数据管线），并能用 `gpt2_124m` 配置初始化模型。

## 改哪里

- [`gpt_lab/models/gpt.py`](../gpt_lab/models/gpt.py) — 在同一文件重构，禁止复制到新目录
- [`gpt_lab/data.py`](../gpt_lab/data.py) — `vocab: bpe` 时用 `tiktoken`（可先读 stub）
- [`configs/gpt2_124m.yaml`](../configs/gpt2_124m.yaml)

## 运行

dev 冒烟：

```bash
make train CONFIG=dev STAGE=gpt2
```

仅初始化 124M 结构（步数很少即可）：

```bash
make train CONFIG=gpt2_124m STAGE=gpt2
```

## GPT-2 small (124M) 参考

| 字段 | 值 |
|------|-----|
| n_layer | 12 |
| n_head | 12 |
| n_embd | 768 |
| vocab | 50257 (BPE) |
| block_size | 1024 |

## 完成标准

- `dev` 配置能 forward + backward
- `gpt2_124m` 能打印 ~124M 参数量（不必训完）
- `experiment.md` 记录一次 shape / 参数量检查

## 提交

[`docs/workflow.md`](../docs/workflow.md)
