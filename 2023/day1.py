import copy


def load_lines():
    clean_lines = list()
    with open(f"input/day1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))
    return clean_lines


def replace_numbers(text: str):
    result = ""
    window = ""
    for c in list(text):
        window += c
        window_translated = copy.deepcopy(window)
        window_translated = window_translated.replace('one', '1')
        window_translated = window_translated.replace('two', '2')
        window_translated = window_translated.replace('three', '3')
        window_translated = window_translated.replace('four', '4')
        window_translated = window_translated.replace('five', '5')
        window_translated = window_translated.replace('six', '6')
        window_translated = window_translated.replace('seven', '7')
        window_translated = window_translated.replace('eight', '8')
        window_translated = window_translated.replace('nine', '9')
        if window != window_translated:
            result = f"{result}{window_translated}"
            window = ""
    result += window
    # text = text.replace('one', '1')
    # text = text.replace('two', '2')
    # text = text.replace('three', '3')
    # text = text.replace('four', '4')
    # text = text.replace('five', '5')
    # text = text.replace('six', '6')
    # text = text.replace('seven', '7')
    # text = text.replace('eight', '8')
    # text = text.replace('nine', '9')
    return result


total = 0
lines = load_lines()
for line in lines:
    original = copy.deepcopy(line)
    line = replace_numbers(line)
    chars = list(line)
    numbers = []
    for char in chars:
        try:
            number = int(char)
            numbers.append(number)
        except:
            pass
    if len(numbers) >= 2:
        subtotal = int(f"{numbers[0]}{numbers[-1]}")
    else:
        subtotal = int(f"{numbers[0]}")
        print(f"{original} --> {line} --> {str(numbers)} --> {subtotal}")
    total += subtotal
    pass

print(total)
