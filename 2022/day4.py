def load_lines():
    clean_lines = list()
    with open(f"input/day4.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))
    return clean_lines


pairs = load_lines()
overlap_count = 0
for pair in pairs:
    pair_split = pair.split(',')
    pair1 = [int(x) for x in pair_split[0].split('-')]
    pair2 = [int(x) for x in pair_split[1].split('-')]
    if ((pair1[0] >= pair2[0] and pair1[1] <= pair2[1])
            or (pair2[0] >= pair1[0] and pair2[1] <= pair1[1])):
        overlap_count += 1

print(f"Day 4 part 1 total overlap count == {overlap_count}")


pairs = load_lines()
overlap_count = 0
for pair in pairs:
    pair_split = pair.split(',')
    pair1 = [int(x) for x in pair_split[0].split('-')]
    pair2 = [int(x) for x in pair_split[1].split('-')]
    if ((pair1[0] >= pair2[0] and pair1[1] <= pair2[1])
            or (pair2[0] >= pair1[0] and pair2[1] <= pair1[1])):
        overlap_count += 1
    elif (((pair1[0] <= pair2[0] <= pair1[1])
            or (pair2[0] <= pair1[0] <= pair2[1]))
            or ((pair1[0] <= pair2[1] <= pair1[1])
            or (pair2[0] <= pair1[1] <= pair2[1]))):
        overlap_count += 1

print(f"Day 4 part 2 total overlap count == {overlap_count}")
