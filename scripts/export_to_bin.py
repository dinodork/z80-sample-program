#!/usr/bin/python3

import getopt
import sys
import os
import errno


def usage():
    print("usage")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "w:h:o:", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    print("args are ")
    print(args)
    w = 2
    h = 2
    indent = '  '

    for udg_file in args:
        with open(udg_file, mode='rb') as file:
            fileContent = file.read()

            binlst = [bin(c)[2:].rjust(8, '0') for c in fileContent]

        asm_path = "build/" + udg_file.replace(".udg", ".asm")
        try:
            os.makedirs(os.path.dirname(asm_path))
        except OSError as exception:

            if exception.errno != errno.EEXIST:
                raise

        asm_file = "build/" + udg_file.replace(".udg", ".asm")
        print("asm_file '" + asm_file + "'")
        with open(asm_file, "w") as f:
            label = os.path.splitext(os.path.basename(udg_file))[0].capitalize()
            print(label + ":", file=f)
            for i in range(h):
                for j in range(8):
                    row = []
                    for k in range(w):
                        row.append("%{byte}".format(
                            byte=binlst[i * w * 8 + j + k * 8]))
                    print(indent+"DB ", ", ".join(row), file=f)


if __name__ == "__main__":
    main()
