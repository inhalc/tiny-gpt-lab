CONFIG ?= dev
STAGE ?= gpt
PROMPT ?= Hello

.PHONY: smoke train sample test

smoke:
	python week01_bootstrap/train.py

train:
	python -m gpt_lab.train --config configs/$(CONFIG).yaml --stage $(STAGE)

sample:
	python -m gpt_lab.sample --config configs/$(CONFIG).yaml --ckpt checkpoints/$(CONFIG)/latest.pt --prompt "$(PROMPT)"

test:
	pytest tests/ -q
