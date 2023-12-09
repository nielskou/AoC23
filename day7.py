import re
from collections import Counter

example = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

def joker_type(hand):
    groups = Counter(hand)
    jokers = hand.count("J")
    if jokers == 5:
        return 7
    if jokers == 0:
        return type(hand)
    rest = groups - Counter({"J": jokers})
    highest, _ = rest.most_common(1)[0]
    rest[highest] += jokers
    return type(rest)

def type(hand):
    groups = Counter(hand)
    match sorted(groups.values()):
        case[5]:
            return 7
        case [1, 4]:
            return 6
        case [2, 3]:
            return 5
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 3
        case [1, 1, 1, 2]:
            return 2
        case [1,1,1,1,1]:
            return 1

def key(hand):
    return joker_type(hand), *map("J23456789TQKA".index, hand)

# bids = dict(map(str.split, example))
bids = dict(map(str.split, open("day7.txt")))
ranks = sorted(bids, key=key, reverse=False)


# print(bids)
print(sum(int(bids[hand]) * rank for rank, hand in enumerate(ranks, 1)))
if __name__ == '__main__':
    pass
