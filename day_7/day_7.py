import sys
from typing import Dict


class Folder:
    def __init__(self, name: str):
        self.name: str = name
        self.parent: Folder = None
        self.subfolders: Dict[str, Folder] = {}
        self.files: Dict[str, int] = {}


def get_lines(filename: str) -> str:
    with open(filename) as file:
        while (line := file.readline().strip()):
            yield line


def build_tree(filename: str) -> Folder:
    root = Folder("/")
    current_folder = root

    for line in get_lines(filename):
        line = line.split()
        if line[0] == '$':  # is a command
            if line[1] == "cd":
                if line[2] == "/":
                    current_folder = root
                elif line[2] == "..":
                    current_folder = current_folder.parent
                else:
                    current_folder = current_folder.subfolders[line[2]]
            elif line[1] == "ls":
                continue
        else:
            if line[0] == "dir":
                new_folder = Folder(line[1])
                new_folder.parent = current_folder
                current_folder.subfolders[line[1]] = new_folder
            else:
                current_folder.files[line[1]] = int(line[0])
    return root


def calculate_folder_sizes(root: Folder, bucket: list) -> int:
    current_folder_size = 0
    for folder in root.subfolders.values():
        current_folder_size += calculate_folder_sizes(folder, bucket)
    
    current_folder_size += sum(root.files.values())

    bucket.append(current_folder_size)

    return current_folder_size


if __name__ == "__main__":
    root = build_tree(sys.argv[1])

    folder_sizes = []
    calculate_folder_sizes(root, folder_sizes)
    folder_sizes.sort()

    part_1 = 0
    for folder_size in folder_sizes:
        if folder_size <= 100_000:
            part_1 += folder_size
        else:
            break
    
    max_size = 70_000_000
    need_free = 30_000_000
    free_space = max_size - folder_sizes[-1]
    need_to_delete = need_free - free_space

    part_2 = 0
    for folder_size in folder_sizes:
        if folder_size >= need_to_delete:
            part_2 = folder_size
            break

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
