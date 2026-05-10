# setup

## 需要

- VS Code
- Python 3.10+
- Conda
- Git
- NVIDIA GPU 和 CUDA 驱动（如果要跑 GPU）

## Python 环境

```bash
conda create -n tiny-gpt-lab python=3.10 -y
conda activate tiny-gpt-lab
```

CPU 机器：

```bash
pip install torch
```

NVIDIA GPU 机器：

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu124
```

如果 CUDA 版本不匹配，按 PyTorch 官方安装页重新选择对应的 CUDA wheel：

```text
https://pytorch.org/get-started/locally/
```

## 检查

```bash
python --version
git --version
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

GPU 机器上继续检查：

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'no cuda')"
```

`torch.cuda.is_available()` 的含义：

- `True`：PyTorch 可以使用 CUDA
- `False`：当前环境不能使用 CUDA

CPU 机器上 `False` 正常。GPU 机器上如果是 `False`，先看：

- `nvidia-smi` 是否能看到 GPU
- PyTorch 是否安装了 CUDA 版本
- 当前终端是否在 `tiny-gpt-lab` 环境里

## Git 身份

```bash
git config --global user.name "your-name"
git config --global user.email "you@example.com"
```
