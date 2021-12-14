from collections import defaultdict, Counter


def solve(s, rules, steps):
    for _ in range(steps):
        news = ''.join([f"{l1}{rules[f'{l1}{l2}']}" for l1,
                        l2 in zip(s[0:], s[1:])])
        s = ''.join([news, s[-1]])
    return s


with open("../inputs/day14_input.in") as f:
    rules = defaultdict(str)
    s = f.readline().strip()
    for line in f.readlines():
        if line == '\n':
            continue
        rule = line.strip().split(" -> ")
        rules[rule[0]] = rule[1]

solved = Counter(solve(s, rules, 10))
print(max(solved.values()) - min(solved.values()))
