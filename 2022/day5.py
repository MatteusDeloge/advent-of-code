def load_input():
    clean_lines = list()
    with open(f"input/day5.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))

    end_of_crates = False
    stack = {
        "stack_raw": list(),
        "stack_width": 0,
        "moves": list()
    }
    for l in clean_lines:
        if l == '':
            continue
        if l.startswith(' 1'):
            stack['stack_width'] = max([int(x) for x in l.strip().split('   ') if x != ''])
            end_of_crates = True
            continue
        if not end_of_crates:
            filled = [x for x in l.replace("    ", " [] ").split(' ') if x != '']
            stack['stack_raw'].append(filled)
        else:
            stack['moves'].append(l)

    stack['stack'] = list()
    for i in range(stack['stack_width']):
        column = list()
        for row_i in range(len(stack['stack_raw'])-1, -1, -1):
            row = stack['stack_raw'][row_i]
            if len(row) > i:
                element = row[i].replace('[', '').replace(']', '')
                if element != '':
                    column.append(element)
        stack['stack'].append(column)
    return stack


def print_stack(stack):
    printed_stack = ""
    max_size = max([len(x) for x in stack['stack']])
    for row in range(max_size-1, -1, -1):
        for column in stack['stack']:
            if len(column) > row:
                printed_stack += f"[{column[row]}] "
            else:
                printed_stack += f"    "
        printed_stack += "\n"
    printed_stack += f" "
    for i in range(1, len(stack['stack'])+1, 1):
        printed_stack += f"{i}   "
    printed_stack += "\n"
    print(printed_stack)


def day5_part1():
    stack = load_input()
    print_stack(stack)
    for move in stack['moves']:
        print(move)
        move_split = move.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
        amount = int(move_split[0])
        source_col = int(move_split[1])-1
        target_col = int(move_split[2])-1
        for i in range(amount):
            if len(stack['stack'][source_col]) > 0:
                popped = stack['stack'][source_col].pop()
                stack['stack'][target_col].append(popped)
        print_stack(stack)
    solution = ""
    for column in stack['stack']:
        if len(column)>0:
            solution += f"{column[-1]}"
    print(f"Solution == {solution}")


def day5_part2():
    stack = load_input()
    print_stack(stack)
    for move in stack['moves']:
        print(move)
        move_split = move.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
        amount = int(move_split[0])
        source_col = int(move_split[1])-1
        target_col = int(move_split[2])-1
        popped_list = list()
        for i in range(amount):
            if len(stack['stack'][source_col]) > 0:
                popped = stack['stack'][source_col].pop()
                popped_list.insert(0, popped)
        stack['stack'][target_col] += popped_list
        print_stack(stack)
    solution = ""
    for column in stack['stack']:
        if len(column)>0:
            solution += f"{column[-1]}"
    print(f"Solution == {solution}")


day5_part2()
