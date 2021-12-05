import re


def main():
    with open("5_input.txt", "r") as f:
        line_map = {}
        caught = set()
        for line in f.readlines():
            if line == '\n':
                continue
            x1, y1, x2, y2 = list(map(int, re.split(',| -> ', line)))
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    if x1 not in line_map:
                        line_map[x1] = set()
                    elif y in line_map[x1]:
                        caught.add((x1, y))
                        continue
                    line_map[x1].add(y)
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    if x not in line_map:
                        line_map[x] = set()
                    elif y1 in line_map[x]:
                        caught.add((x, y1))
                        continue
                    line_map[x].add(y1)
            else:
                "Part B start"
                m = (y2 - y1) / (x2 - x1)
                if m > 0:
                    y = min(y1, y2)
                    for x in range(min(x1, x2), max(x1, x2)+1):
                        if x not in line_map:
                            line_map[x] = set()
                        elif y in line_map[x]:
                            caught.add((x, y))
                            y += 1
                            continue
                        line_map[x].add(y)
                        y += 1
                else:
                    y = max(y1, y2)
                    for x in range(min(x1, x2), max(x1, x2)+1):
                        if x not in line_map:
                            line_map[x] = set()
                        elif y in line_map[x]:
                            caught.add((x, y))
                            y -= 1
                            continue
                        line_map[x].add(y)
                        y -= 1
        print(len(caught))


if __name__ == "__main__":
    main()
