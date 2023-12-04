def part1(line):
    line = line.split(":")[-1]
    left, right = map(str.split, line.split("|"))
    matches = sum(number in left for number in right)
    return 2 ** matches // 2


def part2(line):
    line = line.split(":")[-1]
    left, right = map(str.split, line.split("|"))
    matches = sum(number in left for number in right)
    return matches


matches = {game: part2(line) for game, line in enumerate(open("day4.txt"), 1)}
print(matches)
cards = dict.fromkeys(matches, 1)

n = 1
for game, match in matches.items():
    for i in range(1, match + 1):
        cards[game + i] += cards[game]
    # print({card: cnt for card, cnt in cards.items() if card <= game})
    # if game > 10:
    #     break

if __name__ == '__main__':
    print(sum(map(part1, open("day4.txt"))))
    print(sum(cards.values()))
