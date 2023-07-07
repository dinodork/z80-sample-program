#!/usr/bin/python3

import sys
import os
import errno
import argparse


def main():

    parser = argparse.ArgumentParser(
        description="Exports .fnt or .udg data to Z80 assembler.")

    parser.add_argument("infiles", nargs='*', type=argparse.FileType('rb'),
                        default=sys.stdin)
    parser.add_argument(
        "-W", "--width", help="Width in bytes of all sprites.", default=2)
    parser.add_argument(
        "-H", "--height", help="Height in bytes of all sprites.", default=2)
    parser.add_argument(
        "-i", "--indent", help="Number of spaces to indent.", type=int, default=2)

    args = parser.parse_args()

    for infile in args.infiles:
        fileContent = infile.read()
        binlst = [bin(c)[2:].rjust(8, '0') for c in fileContent]
        asm_path = "build/" + infile.name.replace(".udg", ".asm")
        try:
            os.makedirs(os.path.dirname(asm_path))
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        with open(asm_path, "w") as f:
            label = os.path.splitext(os.path.basename(asm_path))[
                0].capitalize()
            print(label + ":", file=f)
            for i in range(args.height):
                for j in range(8):
                    row = []
                    for k in range(args.width):
                        row.append("%{byte}".format(
                            byte=binlst[i * args.width * 8 + j + k * 8]))
                    print(" " * args.indent + "DB ", ", ".join(row), file=f)


if __name__ == "__main__":
    main()
