
def load_lines():
    clean_lines = list()
    with open(f"input/day2.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))
    return clean_lines


ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

type_mapping = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS,
}
score_mapping = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}


def score_result(type_o: str, type_me: str):
    if type_o == type_me:
        match_score = 3
    elif ((type_o == ROCK and type_me == SCISSORS)
          or (type_o == PAPER and type_me == ROCK)
          or (type_o == SCISSORS and type_me == PAPER)):
        match_score = 0
    else:
        match_score = 6
    return match_score


def score_match(opponent: str, me: str):
    type_o = type_mapping[opponent]
    type_me = type_mapping[me]

    shape_score = score_mapping[type_me]
    match_score = score_result(type_o, type_me)

    return shape_score + match_score


lines = load_lines()
PART = 2

if PART == 2:
    new_lines = list()
    match_score_mapping = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    win_map = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }
    lose_map = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    }
    for line in lines:
        splitted = line.split(' ')
        opponent = splitted[0]
        me = splitted[1]
        type_o = type_mapping[opponent]
        type_me = type_mapping[me]
        wanted_match_score = match_score_mapping[me]
        current_match_score = score_result(type_o, type_me)
        if wanted_match_score == current_match_score:
            new_lines.append(line)
        else:
            if wanted_match_score == 3:
                new_lines.append(f"{opponent} {opponent}")
            elif wanted_match_score == 6:
                new_lines.append(f"{opponent} {win_map[opponent]}")
            else:
                new_lines.append(f"{opponent} {lose_map[opponent]}")
    lines = new_lines


total_score = 0
for line in lines:
    splitted = line.split(' ')
    opponent = splitted[0]
    me = splitted[1]
    score = score_match(opponent, me)
    total_score += score


print(f"Day 2 part {PART} result == {total_score}")