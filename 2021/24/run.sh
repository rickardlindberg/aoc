#!/usr/bin/env bash

set -e

(cd rlmeta && ./make.py)

python ./rlmeta/rlmeta.py \
    --support \
    --compile aoc24.rlmeta \
    --copy main.py > aoc24.py

python aoc24.py
