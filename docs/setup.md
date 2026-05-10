# setup

## 需要

- VS Code
- Python 3.10+
- Conda
- Git

## Python 环境

```bash
conda create -n tiny-gpt-lab python=3.10 -y
conda activate tiny-gpt-lab
pip install torch
```

## 检查

```bash
python --version
git --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

如果是在 CPU 机器上，`CUDA False` 是正常的。

## Git 身份

```bash
git config --global user.name "your-name"
git config --global user.email "you@example.com"
```
