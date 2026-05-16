#!/usr/bin/env sh
# Usage: ./scripts/train.sh dev bigram
CONFIG="${1:-dev}"
STAGE="${2:-gpt}"
python -m gpt_lab.train --config "configs/${CONFIG}.yaml" --stage "${STAGE}"
