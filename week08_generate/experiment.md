# experiment

## 采样 A

命令：

```bash
make sample CONFIG=dev PROMPT="ROMEO:" 
```

- `temperature`:
- `top_k`:
- 生成片段:

## 采样 B（改 temperature）

命令：

```bash
python -m gpt_lab.sample --config configs/dev.yaml --ckpt checkpoints/dev/latest.pt --prompt "ROMEO:" --temperature 1.2
```

- 生成片段:
- 与 A 的差异:

## 观察

-
