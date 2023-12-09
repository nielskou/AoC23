import re

example = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

seeds_txt, *maps_txt = example.split("\n\n")
# seeds_txt, *maps_txt = open("day5.txt").read().split("\n\n")


seeds = [int(seed) for seed in re.findall(r"\d+", seeds_txt)]

def second(item):
    return item[1]

def parse_map(txt):
    lines = iter(txt.splitlines())
    name = next(lines)
    ranges = sorted(([int(num) for num in re.findall(r"\d+", line)] for line in lines), key=second)
    return name, ranges

maps = [parse_map(txt) for txt in maps_txt]

def fill_map(mapping):
    low = src = span = diff = 0
    for dst, src, span in mapping:
        if src > 0:
            yield low, src -1, diff
        diff = dst - src
        low = src
    yield low, src + span - 1, diff
    yield src + span, 1e18, 0

# for name, mapping in maps:
#     print(name)
#     print(mapping)
#     for item in fill_map(mapping):
#         print(item)
#     print()

def convert(mapping, value):
    for dst, src, span in mapping:
        if value in range(src, src+span):
            return value - src + dst
    return value

def location(seed):
    value = seed
    for name, mapping in maps:
        value = convert(mapping, value)
    return value

def convert_ranges(mapping, rangeset):
    return list(_convert_ranges(mapping, rangeset))

def _convert_ranges(mapping, rangeset):
    for low, high in rangeset:
        for mlow, mhigh, diff in fill_map(mapping):
            lowest = max(low, mlow)
            highest = min(high, mhigh)
            if highest > lowest:
                yield lowest + diff, highest + diff

def location_ranges(seed_ranges):
    ranges = seed_ranges
    for name, mapping in maps:
        ranges = convert_ranges(mapping, ranges)
    return list(ranges)

def pairs(seeds):
    seed = iter(seeds)
    yield next(seed), next(seed)


locations = list(map(location, seeds))
print(seeds)
print(locations)
print(min(locations))

print("part2")
seed_ranges = pairs(seeds)
location_range = location_ranges(seed_ranges)
print(location_range)

if __name__ == '__main__':
    pass

#
# print("Ranges")
# for item in convert_ranges(maps[0][1], [(79,92), (55, 67)]):
#     print(item)