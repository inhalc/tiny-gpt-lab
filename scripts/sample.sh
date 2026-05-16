#!/usr/bin/env sh
# Usage: ./scripts/sample.sh dev "Hello"
CONFIG="${1:-dev}"
PROMPT="${2:-Hello}"
python -m gpt_lab.sample \
  --config "configs/${CONFIG}.yaml" \
  --ckpt "checkpoints/${CONFIG}/latest.pt" \
  --prompt "${PROMPT}"
