
w = 2
h = 2
indent = '  '

with open("graphics/robot.udg", mode='rb') as file:
    fileContent = file.read()

    binlst = [bin(c)[2:].rjust(8, '0') for c in fileContent]

with open("build/graphics/robot.asm", "w") as f:
    print("Robot:", file=f)
    for i in range(h):
        for j in range(8):
            row = []
            for k in range(w):
                row.append("%{byte}".format(byte=binlst[i * w * 8 + j + k * 8]))
            print(indent+"DB ", ", ".join(row), file=f)
