import re
import matplotlib.pyplot as plt


def fold(ls: list[list[int]], instr):
    while (instr != []):
        foldline = instr[0][1]
        if instr[0][0] == 'y':
            for dot in range(len(ls)):
                if ls[dot][1] > foldline:
                    relative = ls[dot][1] - foldline
                    ls[dot][1] -= 2 * relative
        elif instr[0][0] == 'x':
            for dot in range(len(ls)):
                if ls[dot][0] > foldline:
                    relative = ls[dot][0] - foldline
                    ls[dot][0] -= 2 * relative
        del instr[0]
    for dot in range(len(ls)):
        ls[dot] = tuple(ls[dot])

    return set(tuple(ls))


with open("../inputs/day13_input.in", "r") as f:
    ls = []
    instr = []
    for line in f.readlines():
        if line.strip() == "":
            continue
        ls.append(re.split(",|fold along |=", line[:-1]))
        if len(ls[-1]) > 2:
            del ls[-1][0]
        if ls[-1][0] not in ('x', 'y'):
            ls[-1] = list(map(int, ls[-1]))
        else:
            instr.append([ls[-1][0], int(ls[-1][1])])
            del ls[-1]

cplist = ls.copy()
folded = fold(cplist, instr)
xlist = [i[0] for i in folded]
ylist = [i[1] for i in folded]
plt.plot(xlist, ylist, 'o')
plt.gca().invert_yaxis()
plt.show()
