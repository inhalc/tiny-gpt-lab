# integration-ui

## 约定

训练产物默认路径：

```text
checkpoints/<config_name>/latest.pt
```

## 方式 A：CLI（已实现）

```bash
python -m gpt_lab.sample \
  --config configs/dev.yaml \
  --ckpt checkpoints/dev/latest.pt \
  --prompt "你的前缀"
```

界面可 `subprocess` 调用上述命令，读 stdout 作为生成文本。

## 方式 B：Python API

```python
from gpt_lab.config import load_config, resolve_device
from gpt_lab.data import load_char_corpus
from gpt_lab.models.gpt import GPT
import torch

cfg = load_config("configs/dev.yaml")
device = resolve_device(cfg.device)
corpus = load_char_corpus(cfg.data_path)
model = GPT(cfg, corpus.vocab_size).to(device)
state = torch.load("checkpoints/dev/latest.pt", map_location=device, weights_only=False)
model.load_state_dict(state["model"])
# ... model.generate(...)
```

## 方式 C：写文件

`sample.py` 可扩展 `--out runs/last_sample.txt`，UI 轮询该文件。

按你现有界面选一种即可，不必三种都做。
