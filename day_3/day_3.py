import sys
import copy


priority_map = {chr(num): num-ord('a')+1 for num in range(ord('a'), ord('z')+1)}
priority_map.update({chr(num): num-ord('A')+27 for num in range(ord('A'), ord('Z')+1)})


def get_lines(filename: str, num_lines: int = 1) -> list:
    with open(filename) as file:
        lines = []
        while (line := file.readline().strip()):
            if len(lines) >= num_lines:
                lines.clear()
            lines.append(line)
            if len(lines) == num_lines:
                yield lines


def part_1():
    priority_sum = 0

    for line in get_lines(sys.argv[1]):
        line = line[0]
        half_length = len(line) // 2
        first_half = line[:half_length]
        second_half = line[half_length:]

        intersect_letter = set(first_half).intersection(set(second_half)).pop()
        priority_sum += priority_map[intersect_letter]
    return priority_sum


def part_2():
    priority_sum = 0

    for line_set in get_lines(sys.argv[1], num_lines=3):
        sack_1, sack_2, sack_3 = line_set
        intersection_letter = (set(sack_1) & set(sack_2) & set(sack_3)).pop()
        priority_sum += priority_map[intersection_letter]
    return priority_sum


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
