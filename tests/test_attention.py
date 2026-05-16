import torch

from gpt_lab.models.attention import CausalSelfAttention


def test_causal_self_attention_shape():
    B, T, C, H = 2, 8, 32, 4
    x = torch.randn(B, T, C)
    attn = CausalSelfAttention(C, H)
    y = attn(x)
    assert y.shape == (B, T, C)


def test_causal_mask_future_is_zero():
    B, T, C, H = 1, 4, 16, 4
    torch.manual_seed(0)
    x = torch.randn(B, T, C)
    attn = CausalSelfAttention(C, H)
    attn.eval()
    y1 = attn(x)
    x_corrupt = x.clone()
    x_corrupt[:, -1, :] = 999.0
    y2 = attn(x_corrupt)
    assert torch.allclose(y1[:, :-1, :], y2[:, :-1, :], atol=1e-5)
