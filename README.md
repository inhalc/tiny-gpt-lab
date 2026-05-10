# Tiny GPT Lab

A small learning-by-doing lab for understanding GPT-style model work from the ground up.

Project URL: https://github.com/inhalc/tiny-gpt-lab

## Start Here

Current focus: **Week 1 - Bootstrap**

Week 1 entry point: [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)

For now, students only need to read these three files:

1. [`README.md`](README.md)
2. [`docs/setup.md`](docs/setup.md)
3. [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md)

## What You Will Do This Week

- Set up your Python and PyTorch environment
- Practice the basic GitHub workflow
- Run and edit a simple PyTorch training loop
- Record one small experiment
- Submit your work through a pull request

## Minimal Workflow

```bash
git clone https://github.com/inhalc/tiny-gpt-lab.git
cd tiny-gpt-lab
git checkout -b week1-yourname

# edit files, run code, and write your notes

git add week01_bootstrap
git commit -m "Complete week 1 bootstrap"
git push -u origin week1-yourname
```

Then open a pull request on GitHub:

- Base branch: `main`
- Compare branch: `week1-yourname`
- PR title: `Week 1 - Your Name`
- PR description: summarize what you ran, changed, observed, and questioned

## What To Submit

Create your own Week 1 submission from the templates in:

[`week01_bootstrap/submission_template/`](week01_bootstrap/submission_template/)

Your pull request should include:

- A completed submission `README.md`
- A completed `experiment.md`
- Any small changes you made to `starter_code/train.py`

## How To Record Problems

When you get stuck, write down:

- What you tried
- What command you ran
- What error or result you saw
- What you think might be happening
- What you want to ask in review

Use the `experiment.md` template even if the experiment did not work. Failed runs are still useful data.

## Repository Map

- [`docs/setup.md`](docs/setup.md): environment setup
- [`docs/workflow.md`](docs/workflow.md): GitHub workflow notes
- [`week01_bootstrap/tasks.md`](week01_bootstrap/tasks.md): Week 1 checklist
- [`week01_bootstrap/starter_code/train.py`](week01_bootstrap/starter_code/train.py): starter PyTorch training loop
- [`week01_bootstrap/submission_template/`](week01_bootstrap/submission_template/): templates for student submissions
