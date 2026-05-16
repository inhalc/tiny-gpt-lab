"""Week03: MLP language model with context window.

TODO: 尝试改 hidden 宽度、层数，观察 val loss。
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class MLPLM(nn.Module):
    def __init__(self, vocab_size: int, block_size: int, n_embd: int = 64):
        super().__init__()
        self.block_size = block_size
        self.token_emb = nn.Embedding(vocab_size, n_embd)
        self.mlp = nn.Sequential(
            nn.Linear(block_size * n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, vocab_size),
        )

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        B, T = idx.shape
        if T > self.block_size:
            idx = idx[:, -self.block_size :]
            T = self.block_size
        emb = self.token_emb(idx)
        flat = emb.view(B, T * emb.size(-1))
        if T < self.block_size:
            pad = torch.zeros(B, (self.block_size - T) * emb.size(-1), device=idx.device)
            flat = torch.cat([pad, flat], dim=1)
        logits = self.mlp(flat)
        return logits.unsqueeze(1).expand(B, T, -1)

    def loss(self, idx: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        logits = self.forward(idx)
        B, T, C = logits.shape
        return F.cross_entropy(logits.view(B * T, C), targets.view(B * T))
