# git / PR

```text
clone -> branch -> edit -> commit -> push -> PR
```

Clone：

```bash
git clone https://github.com/inhalc/tiny-gpt-lab.git
cd tiny-gpt-lab
```

Branch：

```bash
git checkout -b week1-bootstrap
```

Edit：

```bash
mkdir -p week01_bootstrap/workspace
cp week01_bootstrap/submission_template/README.md week01_bootstrap/workspace/README.md
cp week01_bootstrap/submission_template/experiment.md week01_bootstrap/workspace/experiment.md
cp week01_bootstrap/starter_code/train.py week01_bootstrap/workspace/train.py
```

只改：

```text
week01_bootstrap/workspace/
```

Commit：

```bash
git add week01_bootstrap/workspace
git commit -m "week1 bootstrap"
```

Push：

```bash
git push -u origin week1-bootstrap
```

PR：

- base：`main`
- branch：`week1-bootstrap`
- title：`Week 1 Bootstrap`

写：

- 跑了什么
- 改了什么
- 看到什么
- 卡在哪里
