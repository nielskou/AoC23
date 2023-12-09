import re, math
data = """\
Time:        59     79     65     75
Distance:   597   1234   1032   1328""".splitlines()

times, distances = [[int(item) for item in re.findall(r"\d+", line)] for line in data]

def solve(time, distance):
    return sum(hold * (time - hold) > distance for hold in range(time))

print(math.prod(map(solve, times, distances)))

if __name__ == '__main__':
    pass
