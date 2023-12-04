

def load_lines():
    clean_lines = list()
    with open(f"input/day2.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))
    return clean_lines


conditions = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# games_valid = 0
# games = load_lines()
#
# for game in games:
#     splitted = game.split(':')
#     game_id = int(splitted[0].replace('Game ', ''))
#     sets = splitted[1].split(';')
#     invalid_game = False
#     for s in sets:
#         if invalid_game:
#             break
#         game_state = {
#             'red': 0,
#             'green': 0,
#             'blue': 0
#         }
#         cubes = s.strip().split(', ')
#         for cube in cubes:
#             config = cube.split(' ')
#             game_state[config[1]] += int(config[0])
#         if game_state['red'] > conditions['red'] or game_state['green'] > conditions['green'] or game_state['blue'] > conditions['blue']:
#             red_state = 'OK' if game_state['red'] <= conditions['red'] else f"++{game_state['red']-conditions['red']}"
#             green_state = 'OK' if game_state['green'] <= conditions['green'] else f"++{game_state['green']-conditions['green']}"
#             blue_state = 'OK' if game_state['blue'] <= conditions['blue'] else f"++{game_state['blue']-conditions['blue']}"
#             print(f"Game {game_id} is INVALID -> RED {red_state}, BLUE {blue_state}, GREEN {green_state}")
#             invalid_game = True
#     if not invalid_game:
#         games_valid += game_id
#
# print(f"Sum of valid game ids == {games_valid}")

total_power = 0

games = load_lines()
for game in games:
    splitted = game.split(':')
    game_id = int(splitted[0].replace('Game ', ''))
    sets = splitted[1].split(';')
    invalid_game = False
    game_power_state = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for s in sets:
        if invalid_game:
            break
        game_state = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        cubes = s.strip().split(', ')
        for cube in cubes:
            config = cube.split(' ')
            game_state[config[1]] += int(config[0])
        game_power_state['red'] = max(game_power_state['red'], game_state['red'])
        game_power_state['green'] = max(game_power_state['green'], game_state['green'])
        game_power_state['blue'] = max(game_power_state['blue'], game_state['blue'])

    power = game_power_state['red'] * game_power_state['green'] * game_power_state['blue']
    total_power += power

print(f"Total power == {total_power}")

