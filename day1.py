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


print(sum(map(calibrate, example)))
print(sum(map(recalibrate, example2)))
print(sum(map(calibrate, open("day1.txt"))))
print(sum(map(recalibrate, open("day1.txt"))))

if __name__ == '__main__':
    pass
