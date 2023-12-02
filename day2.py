from collections import Counter
import re

example = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

def parse(line):
    game_part, hands_part = line.split(": ")
    game = int(re.search(r"\d+", game_part).group())
    hands = hands_part.split("; ")
    return game, *map(parse_hand, hands)

def parse_hand(hand):
    colors = hand.split(", ")
    return Counter(dict(map(parse_color, colors)))

def parse_color(hand):
    num, color = re.search(r"(\d+) (red|green|blue)", hand).groups()
    return color, int(num)

def part1_check(hands):
    """12 red cubes, 13 green cubes, and 14 blue cubes"""
    return all(hand <= Counter({"red": 12, "green": 13, "blue": 14}) for hand in hands)

def part1_line(line):
    game_id, *hands = parse(line)
    return game_id if part1_check(hands) else 0

def smallest(hands):
    red = green = blue = 0
    for hand in hands:
        red = max(red, hand.get("red", 0))
        green = max(green, hand.get("green", 0))
        blue = max(blue, hand.get("blue", 0))
    return red * blue * green


def part2_line(line):
    game_id, *hands = parse(line)
    return smallest(hands)

if __name__ == '__main__':
    # print(sum(map(part1_line, example)))
    print(sum(map(part1_line, open("day2.txt"))))
    print(sum(map(part2_line, open("day2.txt"))))
