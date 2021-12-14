from collections import defaultdict


def solve(s, rules, steps):
    counts = defaultdict(int)
    letter_counts = defaultdict(int)
    for l1, l2 in zip(s[0:], s[1:]):
        counts[f'{l1}{l2}'] += 1
    for l in s:
        letter_counts[l] += 1
    for _ in range(steps):
        countscp = counts.copy()
        for key in countscp:
            counts[key] -= countscp[key]
            letter_counts[rules[key]] += countscp[key]
            counts[f'{key[0]}{rules[key]}'] += countscp[key]
            counts[f'{rules[key]}{key[1]}'] += countscp[key]

    return letter_counts


with open("../inputs/day14_input.in") as f:
    rules = defaultdict(str)
    s = f.readline().strip()
    for line in f.readlines():
        if line == '\n':
            continue
        rule = line.strip().split(" -> ")
        rules[rule[0]] = rule[1]
solved = solve(s, rules, 40)
print(max(solved.values()) - min(solved.values()))
