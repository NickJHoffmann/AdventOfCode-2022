import sys
from queue import PriorityQueue


def get_lines(filename: str) -> str:
    with open(filename) as file:
        while (line := file.readline()):
            yield line


def get_max_calories():
    max_calories = PriorityQueue(maxsize=3) 
    current_elf_calories = 0
    for line in get_lines(sys.argv[1]):
        line = line.strip()
        if line:
            current_elf_calories += int(line)
        else:
            if max_calories.full():
                test_num = max_calories.get()
                max_calories.put(max(test_num, current_elf_calories))
            else:
                max_calories.put(current_elf_calories)
            current_elf_calories = 0

    if max_calories.full() and current_elf_calories != 0:
        test_num = max_calories.get()
        max_calories.put(max(test_num, current_elf_calories))
    elif not max_calories.full() and current_elf_calories != 0:
        max_calories.put(current_elf_calories)
    
    calories = []
    while not max_calories.empty():
        calories.append(max_calories.get())
    return calories


if __name__ == "__main__":
    calories = get_max_calories()
    print(f"Part 1: {calories[2]}")
    print(f"Part 2: {sum(calories)}")
