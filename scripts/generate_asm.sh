BUILD_DIR=$1
DIR=$2
mkdir -p ${BUILD_DIR}/${DIR}
scripts/export_to_bin.py graphics/bubble2x2.udg -o build/graphics/bubble2x2.asm
scripts/export_to_bin.py graphics/robot.udg -o build/graphics/robot.asm
