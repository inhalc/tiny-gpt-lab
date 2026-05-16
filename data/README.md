# data

## tiny_shakespeare.txt

字符级小语料，用于 week02–week05 本地开发。

若文件不存在，可下载：

```bash
curl -o data/tiny_shakespeare.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
```

Windows PowerShell：

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt" -OutFile "data/tiny_shakespeare.txt"
```

## week06+

BPE 编码与更大数据集见 `week06_gpt2_arch/README.md` 中的 `prepare` 说明。
