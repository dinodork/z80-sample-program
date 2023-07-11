#!/usr/bin/python3

import sys
import os
import errno
import argparse
from math import floor


def main():

    parser = argparse.ArgumentParser(
        description="Exports .fnt or .udg data to Z80 assembler.")

    parser.add_argument("infile", type=argparse.FileType('rb'),
                        default=sys.stdin)
    parser.add_argument("-o", "--outfile", type=argparse.FileType('w'),
                        default=sys.stdout)
    parser.add_argument(
        "-W", "--width", help="Width in bytes of all sprites.", type=int, default=2)
    parser.add_argument(
        "-H", "--height", help="Height in octets of all sprites.", type=int,   default=2)
    parser.add_argument(
        "-i", "--indent", help="Number of spaces to indent.", type=int, default=2)
    parser.add_argument(
        "-f", "--frames",
        help="Number of frames in the sprite, or characters in a font.",
        type=int, default=1
    )

    args = parser.parse_args()

    label = os.path.splitext(os.path.basename(args.infile.name))[
        0].capitalize()

    n_frames = floor(os.path.getsize(args.infile.name) /
                     (args.width * 8 * args.height))

    for frameno in range(1, n_frames):
        print(label + "_" + str(frameno) + ":", file=args.outfile)
        for chunkno in range(args.height):
            chunk = args.infile.read(8 * args.width)
            if len(chunk) < 8 * args.width:
                print("Warning: file ends in the middle of a sprite",
                      file=sys.stderr)
                exit(0)
            for i in range(0, 8):
                print(" " * args.indent + "DB " +
                      " ", file=args.outfile, end='')
                print(", ".join(["%" + bin(chunk[byte * 8 + i])[2:].rjust(8,
                      '0') for byte in range(args.width)]), file=args.outfile)
        print(file=args.outfile)
        frameno += 1


if __name__ == "__main__":
    main()
