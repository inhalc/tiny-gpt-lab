import torch

x = torch.randn(100, 1)
y = 2 * x + 1

w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

for step in range(100):
    pred = w * x + b
    loss = ((pred - y) ** 2).mean()
    loss.backward()

    with torch.no_grad():
        w -= 0.1 * w.grad
        b -= 0.1 * b.grad
        w.grad.zero_()
        b.grad.zero_()

    print(step, loss.item())
