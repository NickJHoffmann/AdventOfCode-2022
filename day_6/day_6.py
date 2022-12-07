import sys

def find_index(line: str, marker_length: int):
    for i in range(len(line) - marker_length):
        if len(set(line[i:i+marker_length])) == marker_length:
            return i + marker_length

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        line = file.readline().strip()
    message_start_index = find_index(line, 4)
    message_start_marker = find_index(line, 14)
    print(f"Part 1: {message_start_index}")
    print(f"Part 1: {message_start_marker}")
