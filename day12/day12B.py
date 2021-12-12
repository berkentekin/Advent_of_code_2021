from queue import Queue
pathDict = dict()
result = 0
seen_nodes = set()
lower = set()
lletter = 0
alltrips = set()
temp = 0

"""This FrankenCode is absolutely horrible. I got very annoyed with
the problem and sort of winged it. OF COURSE I will be taking a
second look at this code. I'll probably use NetworkX if I manage to
learn it."""


def solve(pathDict, begin, usedup=0, path=["start"]):
    global result, seen_nodes, lletter, visit, alltrips
    if (begin == "end"):
        result += 1
        return
    for e in pathDict[begin]:
        if not e.islower():
            solve(pathDict, e, usedup, path)
        elif lletter == e and usedup == 0:
            solve(pathDict, e, 1, path)
        elif e not in path:
            path.append(e)
            solve(pathDict, e, usedup, path)
            path.remove(e)


with open("../inputs/day12_input.in", "r") as f:
    for line in f.readlines():
        path = line.strip().split("-")
        if path[0] not in pathDict:
            pathDict[path[0]] = []
        if path[1] not in pathDict:
            pathDict[path[1]] = []
        pathDict[path[0]].append(path[1])
        pathDict[path[1]].append(path[0])
for x in pathDict:
    if x.islower():
        lower.add(x)
    for y in pathDict[x]:
        if y == "start":
            pathDict[x].remove(y)
        if y.islower():
            lower.add(y)
pathDict.pop("end")
for l in filter(lambda x: x not in ('start', 'end'), lower):
    lletter = l
    result = 0
    solve(pathDict, "start")
    temp += result
lletter = 0
result = 0
solve(pathDict, "start")
print(temp - result * (len(lower) - 3))
