def load_lines():
    clean_lines = list()
    with open(f"input/day7.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            clean_lines.append(line.replace("\n", ""))
    return clean_lines


def dir_to_path(dir_list):
    return ''.join(dir_list)


def extended_dir(curr_path: str, new_dir: str):
    return f"{curr_path}{new_dir}/"


files_map = {
    '/': {}
}
files_map2 = {}
directory_sizes = {}

current_dir = ['/']
lines = load_lines()
for line in lines:
    current_path = dir_to_path(current_dir)
    if line.startswith('$'):
        command = line[2:]
        if command.startswith('cd'):
            if '..' in command:
                current_dir.pop()
                if len(current_dir) == 0:
                    current_dir = ['/']
            elif 'cd /' in command:
                current_dir = ['/']
            else:
                current_dir.append(command[3:] + '/')
        elif command.startswith('ls'):
            continue
        else:
            print(f'unknown command: {command}')
    elif line.startswith('dir'):
        this_dir = line[4:]
        if extended_dir(current_path, this_dir) not in files_map:
            files_map[extended_dir(current_path, this_dir)] = {}
        print('directory')
    else:
        splitted = line.split(' ')
        filesize = int(splitted[0])
        filename = splitted[1]
        files_map[current_path][filename] = filesize
        files_map2[f"{current_path}{filename}"] = filesize
        print(f'Processed file {filename} of size {filesize}')

directory_sizes = {}
for index, filepath in enumerate(files_map2):
    filesize = files_map2[filepath]
    dirs = [x for x in filepath.split('/')[:-1] if x != '']
    dirs.insert(0, '/')
    for depth in range(len(dirs)):
        path_partial = '/'.join(dirs[:depth+1]).replace('//', '/')
        if path_partial not in directory_sizes:
            directory_sizes[path_partial] = filesize
        else:
            directory_sizes[path_partial] += filesize

total = 0
for index, dirpath in enumerate(directory_sizes):
    dirsize = directory_sizes[dirpath]
    if dirsize < 100000:
        total += dirsize
print(f"Total part 1 == {total}")

target_size = 30000000 - (70000000 - directory_sizes['/'])

sorted_dir_sizes = sorted(directory_sizes.items(), key=lambda x: x[1])
for dir_elem in sorted_dir_sizes:
    dirsize = dir_elem[1]
    if dirsize > target_size:
        print(f"Result part 2 == {dirsize}")
        break

