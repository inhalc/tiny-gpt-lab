import torch

# fake data: y = 2x + 1
x = torch.randn(100, 1)
y = 2 * x + 1

# parameters to learn
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

lr = 0.1

for step in range(100):
    pred = w * x + b
    loss = ((pred - y) ** 2).mean()

    loss.backward()

    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

        w.grad.zero_()
        b.grad.zero_()

    print(step, loss.item())
