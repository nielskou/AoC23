import re
import sys
from functools import reduce
def mash(init, char):
    return (init + ord(char)) * 17 % 256

def HASH(value):
    chars = map(ord, value)
    result = 0
    for char in chars:
        result += char
        result *= 17
        result %= 256
    return result

def HASH(value):
    return reduce(mash, value, 0)

example = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")

def part1(strings):
    return sum(map(HASH, strings))

print(part1(example))

inits = open("day15.txt").read().strip().split(",")

print(part1(inits))

pattern = re.compile(r"(\w+)([-=])(\d?)")

def part2(values):
    boxes = [dict() for _ in range(256)]
    for value in values:
        label, action, focal = pattern.match(value).groups()
        box = HASH(label)
        match action:
            case "-":
                if label in boxes[box]:
                    del boxes[box][label]
            case "=":
                boxes[box][label] = int(focal)
    result = sum(nbox * nlens * focal for nbox, box in enumerate(boxes, 1)
                 for nlens, (label, focal) in enumerate(box.items(), 1))
    return result

print(part2(example))
print(part2(inits))
