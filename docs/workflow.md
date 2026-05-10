# Workflow Guide

## 0) Create / Connect GitHub Repository (One-time)
If this repo is local only, GitHub pages will not update until a remote is connected.

```bash
# create a GitHub repo first, then bind local repo
git remote add origin git@github.com:<your-name>/tiny-gpt-lab.git
# or: https://github.com/<your-name>/tiny-gpt-lab.git
git branch -M main
git push -u origin main
```

## Git Workflow
Use feature branches for all work:

```bash
git checkout -b week1-yourname
git add .
git commit -m "finish week1"
git push -u origin week1-yourname
```

## Pull Request (PR) Workflow
- Do **not** push directly to `main`
- Open a PR for every submission
- Use PR comments for discussion and review
- Treat PR review as scientific discussion

## Submission Requirements
Each weekly submission should include:
1. `README.md` (goal, result, observation, questions)
2. `experiment.md` (structured experiment log)
3. Code artifacts (scripts/notebooks/configs)

## Working Principles
- Always record what you changed and why
- Report observations, not just final numbers
- Ask testable questions
- Prefer reproducible steps over ad-hoc actions
