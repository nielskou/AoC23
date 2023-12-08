import re
from functools import reduce
from math import lcm

example = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".splitlines()

example2 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()

def parse(lines):
    lines = iter(lines)
    sequence = next(lines).strip()
    left = {}
    right = {}
    next(lines)
    for line in lines:
        src, go_left, go_right = re.findall(r"\w+", line.strip())
        left[src] = go_left
        right[src] = go_right

    return sequence, left, right


# sequence, left, right = parse(example2)
sequence, left, right = parse(open("day8.txt"))
go = {"L": left, "R": right}

def part1():
    state = "AAA"
    steps = 0
    for count in range(1, 1_000):
        for turn in sequence:
            state = go[turn][state]
            steps += 1
            if state == "ZZZ":
                return steps

def part2_steps(start):
    state = start
    steps = 0
    for count in range(1, 1_000):
        for turn in sequence:
            state = go[turn][state]
            steps += 1
            if state.endswith("Z"):
                return steps

def part2():
    steps = [part2_steps(start) for start in left if start.endswith("A")]
    return reduce(lcm, steps)


if __name__ == '__main__':

    print(part1())
    print(part2())
