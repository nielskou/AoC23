from itertools import tee

def pairs(iterable):
    one, two = tee(iterable)
    next(two)
    return zip(one, two)

def predict(seq):
    if not any(seq):
        return 0
    diffs = [y - x for x, y in pairs(seq)]
    return seq[-1] + predict(diffs)

lines = [[int(x) for x in line.split()] for line in open("day9.txt")]
print(sum(map(predict, lines)))
for line in lines:
    line.reverse()  # the magic of OOP
print(sum(map(predict, lines)))


l = [[int(i) for i in s.split()] for s in open('input')]
