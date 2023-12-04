def win(line):
    line = line.split(":")[-1]
    left, right = map(str.split, line.split("|"))
    return sum(number in left for number in right)


matches = {game: win(line) for game, line in enumerate(open("day4.txt"))}
cards = dict.fromkeys(matches, 1)
for game, match in matches.items():
    for copy in range(game + 1, game + match + 1):
        cards[copy] += cards[game]
print(sum(2 ** match // 2 for match in matches.values()))
print(sum(cards.values()))

if __name__ == '__main__':
    pass
