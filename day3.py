import re

lines = list(open("day3.txt"))
symbols = "#$%&*+-/=@"

# lines = """\
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()


def clamp(low, value, high):
    if value < low:
        return low
    if value > high:
        return high
    return value

n = len(lines[0])
m = len(lines)
def part1():
    total = 0
    for lineno, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            left, right = match.span()
            above = lines[clamp(0, lineno-1, m-1)][clamp(0, left-1, n-1):clamp(0, right+1, n)]
            below = lines[clamp(0, lineno+1, m-1)][clamp(0, left-1, n-1):clamp(0, right+1, n)]

            if any([
                any(char in symbols for char in above),
                any(char in symbols for char in below),
                lines[lineno][clamp(0, left-1, n-1)] in symbols,
                lines[lineno][clamp(0, right, n-1)] in symbols,
            ]):
                total += int(match.group())

    return total


def part2():
    total = 0
    gearbox = {}
    for lineno, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            left, right = match.span()
            for y in range(clamp(0, lineno-1, m), clamp(0, lineno+2, m)):
                x = lines[y].find("*", clamp(0, left-1, n-1), clamp(0, right+1, n))
                if x != -1:
                    gearbox.setdefault((x,y), []).append(int(match.group()))

    for pos, gears in gearbox.items():
        if len(gears) == 2:
            total += int.__mul__(*gears)

    return total


if __name__ == '__main__':
    print(part1())
    print(part2())
