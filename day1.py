import re
import regex

example = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

example2 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

def calibrate(line):
    digits = re.findall(r"\d", line)
    return int(digits[0] + digits[-1])

names = "one two three four five six seven eight nine".split()
digitmap = {name: str(idx) for idx, name in enumerate(names, 1)}
print(digitmap)
pattern = regex.compile(r"(\d|" + "|".join(names) + ")")

def recalibrate(line):
    digitlikes = pattern.findall(line, overlapped=True)
    digits = [digitmap.get(digit, digit) for digit in digitlikes]
    return int(digits[0] + digits[-1])

# examples
print(sum(map(calibrate, example)))
print(sum(map(recalibrate, example2)))
# input data
print(sum(map(calibrate, open("day1.txt"))))
print(sum(map(recalibrate, open("day1.txt"))))
# oneliners
print(10*sum(int(next(c for c in line if c.isdigit())) for line in open("day1.txt")) + sum(int(next(c for c in reversed(line) if c.isdigit())) for line in open("day1.txt")))
print(10 * sum(min((line.find(digit) % 99, num) for digit, num in {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0':0}.items())[1] for line in open("day1.txt")) + sum(        max((line.rfind(digit), num) for digit, num in {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0':0}.items())[1] for line in open("day1.txt")))
