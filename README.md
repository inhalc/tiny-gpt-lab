# tiny-gpt-lab

先看：

- [`docs/setup.md`](docs/setup.md)
- [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)

本周：

- 配环境
- 跑通 `train.py`
- 改一次 learning rate
- 观察 loss
- 开 PR

工作目录：

```text
week01_bootstrap/workspace/
```

不要直接改：

- `main`
- `week01_bootstrap/starter_code/`

准备：

```bash
git clone https://github.com/inhalc/tiny-gpt-lab.git
cd tiny-gpt-lab
git checkout -b week1-bootstrap

mkdir -p week01_bootstrap/workspace
cp week01_bootstrap/submission_template/README.md week01_bootstrap/workspace/README.md
cp week01_bootstrap/submission_template/experiment.md week01_bootstrap/workspace/experiment.md
cp week01_bootstrap/starter_code/train.py week01_bootstrap/workspace/train.py
```

运行：

```bash
python week01_bootstrap/workspace/train.py
```

提交：

```bash
git add week01_bootstrap/workspace
git commit -m "week1 bootstrap"
git push -u origin week1-bootstrap
```

PR：

- base：`main`
- branch：`week1-bootstrap`
- title：`Week 1 Bootstrap`
- 写清楚：跑了什么、改了什么、看到什么、卡在哪里
