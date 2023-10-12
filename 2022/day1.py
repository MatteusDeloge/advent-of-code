
def load_lines():
    clean_lines = list()
    with open(f"input/day1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))
    return clean_lines


def day1_part1():
    lines = load_lines()
    current_elf_cals = 0
    current_elf_id = 1
    max_elf_cals = 0
    for line in lines:
        if line == '':
            if current_elf_cals > max_elf_cals:
                max_elf_cals = current_elf_cals
                print(f"Elf {current_elf_id} done, new max calories of {max_elf_cals}")
            else:
                print(f"Elf {current_elf_id} done")
            current_elf_id += 1
            current_elf_cals = 0
        else:
            current_elf_cals += int(line)
    print(f"Day 1 part 1 solution == {max_elf_cals}")


def day1_part2():
    lines = load_lines()
    elves_cals = list()
    current_elf_cals = 0
    current_elf_id = 1
    for line in lines:
        if line == '':
            elves_cals.append(current_elf_cals)
            current_elf_id += 1
            current_elf_cals = 0
            print(f"Elf {current_elf_id} done")
        else:
            current_elf_cals += int(line)
    top_elves = sorted(elves_cals, reverse=True)[:3]
    total = sum(top_elves)
    print(f"Day 1 part 2 solution == {total}")

