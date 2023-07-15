#!/bin/bash

set -eou pipefail

BUILD_DIR=$1
DIR=$2

mkdir -p ${BUILD_DIR}/${DIR}
scripts/export_to_bin.py graphics/bubble2x2.udg -o build/graphics/bubble2x2.asm
scripts/export_to_bin.py -W1 graphics/npm_large.fnt -o build/graphics/npm_large.asm

scripts/export_to_bin.py graphics/player_left.udg   -o build/graphics/player.asm -f3
scripts/export_to_bin.py graphics/player_center.udg -a build/graphics/player.asm -f1
scripts/export_to_bin.py graphics/player_right.udg  -a build/graphics/player.asm -f3
