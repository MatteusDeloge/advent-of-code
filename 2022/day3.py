import string


def load_lines():
    clean_lines = list()
    with open(f"input/day3.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))
    return clean_lines


# rucksacks = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw"
# ]
rucksacks = load_lines()

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
score_map = {}
s = 1

for l in letters:
    score_map[l] = s
    s += 1

total_priority = 0

for r in rucksacks:
    items = [*r]
    size = int(len(items) / 2)
    comp_1 = items[:size]
    comp_2 = items[size:]
    intersection = list(set([x for x in comp_1 if x in comp_2]))
    priority = 0
    for i in intersection:
        priority += score_map[i]
    total_priority += priority
print(f"Day 3 part 1 total score == {total_priority}")

index = 0
total_priority = 0

while index < len(rucksacks):
    items_1 = [*rucksacks[index]]
    items_2 = [*rucksacks[index+1]]
    items_3 = [*rucksacks[index+2]]
    intersection = list(set([x for x in items_1 if x in items_2 and x in items_3]))
    priority = 0
    for i in intersection:
        priority += score_map[i]
    total_priority += priority
    index += 3

print(f"Day 3 part 2 total score == {total_priority}")
