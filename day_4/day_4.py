import sys

def get_lines(filename: str) -> str:
    with open(filename) as file:
        while (line := file.readline().strip()):
            yield line


def get_overlap_counts():
    part_1 = 0
    part_2 = 0

    for line in get_lines(sys.argv[1]):
        set_1, set_2 = line.split(',')
        set_1_1, set_1_2 = [int(num) for num in set_1.split('-')]
        set_2_1, set_2_2 = [int(num) for num in set_2.split('-')]

        # Part 1 check
        if (set_1_1 <= set_2_1 and set_1_2 >= set_2_2) or (set_2_1 <= set_1_1 and set_2_2 >= set_1_2):
            part_1 += 1

        # Part 2 check - inefficient I know but it's easy to read 
        set_1_range = range(set_1_1, set_1_2 + 1)
        set_2_range = range(set_2_1, set_2_2 + 1)
        if (set_1_1 in set_2_range or 
            set_1_2 in set_2_range or 
            set_2_1 in set_1_range or 
            set_2_2 in set_1_range):
            part_2 += 1
        
    return part_1, part_2


if __name__ == "__main__":
    part_1, part_2 = get_overlap_counts()
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
