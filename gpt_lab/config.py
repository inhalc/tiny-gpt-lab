from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class TrainConfig:
    name: str
    block_size: int
    batch_size: int
    max_steps: int
    eval_interval: int
    lr: float
    device: str
    n_layer: int
    n_head: int
    n_embd: int
    dropout: float
    data_path: str
    vocab: str

    @property
    def ckpt_dir(self) -> Path:
        return Path("checkpoints") / self.name


def load_config(path: str | Path) -> TrainConfig:
    with open(path, encoding="utf-8") as f:
        raw: dict[str, Any] = yaml.safe_load(f)
    return TrainConfig(**raw)


def resolve_device(requested: str) -> str:
    import torch

    if requested == "auto":
        return "cuda" if torch.cuda.is_available() else "cpu"
    return requested
