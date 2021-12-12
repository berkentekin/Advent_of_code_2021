from queue import Queue
pathDict = dict()
result = 0
seen_nodes = set()


def solve(pathDict, begin, path=["start"], trip=["start"]):
    global result, seen_nodes
    if (begin == "end"):
        result += 1
        return
    seen_nodes = set(path)
    for e in pathDict[begin]:
        if e not in path:
            trip.append(e)
            if e.islower():
                path.append(e)
            solve(pathDict, e, path, trip)
            if e in path:
                path.remove(e)
            trip.remove(e)


with open("../inputs/day12_input.in", "r") as f:
    for line in f.readlines():
        path = line.strip().split("-")
        if path[0] not in pathDict:
            pathDict[path[0]] = []
        if path[1] not in pathDict:
            pathDict[path[1]] = []
        pathDict[path[0]].append(path[1])
        pathDict[path[1]].append(path[0])
solve(pathDict, "start")
print(result)
