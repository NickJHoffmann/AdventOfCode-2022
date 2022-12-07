def get_lines(filename: str) -> str:
    with open(filename) as file:
        while (line := file.readline()):
            yield line
