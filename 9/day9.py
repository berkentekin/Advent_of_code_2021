import numpy as np
from heapq import nlargest
from functools import reduce

"Horrible, embarrassing code."


def main() -> None:
    with open("inputs/day9_input.in", "r") as f:
        heightmap = []
        lows = []
        result_p1 = 0
        result_p2 = []
        for line in f.readlines():
            heightmap.append(list(map(int, list(line.strip()))))
        neighbors = find_neighbors(heightmap)
        for k in neighbors:
            if (neighbors[k][0] < min(neighbors[k][1])):
                result_p1 += neighbors[k][0] + 1
                lows.append(k)
        for p in lows:
            result_p2.append(find_basin(heightmap, p))
        result_p2 = nlargest(3, result_p2)
        print(result_p1)
        print(reduce(lambda x, y: x * y, result_p2))


def find_basin(heightmap, point):
    found_points = set()
    x, y = point
    sizes = []
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def search_direction(i=x, j=y, cache=-1):
        if (heightmap[i][j] != 9 and heightmap[i][j] > cache):
            found_points.add((i, j))
            for dx, dy in directions:
                if i + dx >= 0 and i + dx <= len(heightmap) - 1 and j + dy >= 0 and j + dy <= len(heightmap[i]) - 1:
                    search_direction(i + dx, j + dy, heightmap[i][j])
                else:
                    continue
    search_direction()
    return len(found_points)


def find_neighbors(heightmap):
    neighbordict = {}
    for i in range(len(heightmap)):
        for j, value in enumerate(heightmap[i]):
            curr_neighbors = []
            if i == 0 or i == len(heightmap) - 1 or j == 0 or j == len(heightmap[i])-1:
                if i != 0:
                    curr_neighbors.append(heightmap[i-1][j])
                if j != 0:
                    curr_neighbors.append(heightmap[i][j-1])
                if i != len(heightmap) - 1:
                    curr_neighbors.append(heightmap[i+1][j])
                if j != len(heightmap[i]) - 1:
                    curr_neighbors.append(heightmap[i][j+1])
            else:
                curr_neighbors = [
                    heightmap[i-1][j],
                    heightmap[i][j-1],
                    heightmap[i][j+1],
                    heightmap[i+1][j]
                ]
            neighbordict[(i, j)] = (
                heightmap[i][j], curr_neighbors)

    return neighbordict


if __name__ == '__main__':
    main()
