# git / PR

## 分支

```bash
git checkout -b week2-bigram
```

已经在对应分支上就不用再执行。

## 查看状态

```bash
git status
```

## 提交 commit

```bash
git add gpt_lab week02_bigram
git commit -m "week2 bigram baseline"
```

## 推送

第一次推这个分支：

```bash
git push -u origin week2-bigram
```

后面继续推：

```bash
git push
```

## PR

- base: `main`
- branch: `week2-bigram`
- title: `Week 2 Bigram`

PR 里写：

- 跑了什么命令
- 改了什么代码（`gpt_lab/` 里哪些文件）
- 观察到什么现象
- 有没有卡住的问题
