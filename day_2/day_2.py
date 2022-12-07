import sys

class Option:
    def __init__(self, value):
        self.value = value
        self.beats = None
        self.loses = None



def get_lines(filename: str) -> str:
    with open(filename) as file:
        while (line := file.readline().strip()):
            yield line


def part_1():
    points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    win_map = {
        "Y": "A",
        "Z": "B",
        "X": "C"
    }

    equivalence_map = {
        "C": "Z",
        "A": "X",
        "B": "Y"
    }

    score = 0
    for line in get_lines(sys.argv[1]):
        a, b = line.split()
        if equivalence_map[a] == b:
            score += (points[b] + 3)
        elif win_map[b] == a:
            score += (points[b] + 6)
        else:
            score += points[b]
    return score


def part_2():
    rock = Option(1)
    paper = Option(2)
    scissors = Option(3)

    rock.beats = scissors
    rock.loses = paper

    paper.beats = rock
    paper.loses = scissors

    scissors.beats = paper
    scissors.loses = rock

    options = {
        'A': rock,
        'B': paper,
        'C': scissors
    }

    score = 0
    for line in get_lines(sys.argv[1]):
        opponent, move = line.split()

        
        if move == 'X':     # Lose
            score += options[opponent].beats.value
        elif move == 'Y':   # Draw
            score += options[opponent].value + 3
        else:               # Win
            score += options[opponent].loses.value + 6
    return score
    

if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
