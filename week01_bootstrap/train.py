import torch

torch.manual_seed(0)

# 模拟数据：y = 2x + 1，再加一点噪声
x = torch.linspace(-3, 3, 100).unsqueeze(1)
noise = 0.3 * torch.randn(100, 1)
y = 2 * x + 1 + noise

# 需要学习的参数
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

lr = 0.1
steps = 200

print(f"start: w={w.item():.4f}, b={b.item():.4f}, lr={lr}")

for step in range(steps):
    pred = w * x + b
    loss = ((pred - y) ** 2).mean()

    loss.backward()

    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

        w.grad.zero_()
        b.grad.zero_()

    if step % 20 == 0 or step == steps - 1:
        print(f"step={step:03d} loss={loss.item():.4f} w={w.item():.4f} b={b.item():.4f}")
