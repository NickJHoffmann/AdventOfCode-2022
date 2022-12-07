import sys
from queue import LifoQueue
from typing import Dict


def get_lines(file) -> str:
    while (line := file.readline().strip()):
        yield line


def get_initial_stacks(file) -> dict:
    stack_builders = {str(num): LifoQueue() for num in range(1, 10)}
    while line := file.readline().strip('\n'):
        for i in range(1, len(line), 4):
            if line[i] != ' ' and line[i-1] == '[':
                stack_num = str((i + 3) // 4)
                stack_builders[stack_num].put(line[i])
    
    stacks = {}
    for stack_num, queue in stack_builders.items():
        if queue.empty(): break
        stacks[stack_num] = LifoQueue()
        while not queue.empty():
            stacks[stack_num].put(queue.get())
    return stacks


def move_crates(stacks: dict, num_to_move: int, from_stack: str, to_stack: str, keep_order=False) -> None:
    if keep_order:
        temp_stack = LifoQueue()
        for _ in range(num_to_move):
            temp_stack.put(stacks[from_stack].get())
        while not temp_stack.empty():
            stacks[to_stack].put(temp_stack.get())
    else:
        for _ in range(num_to_move):
            crate = stacks[from_stack].get()
            stacks[to_stack].put(crate)


def part_1():
    with open(sys.argv[1]) as file:
        stacks = get_initial_stacks(file)
        
        for line in get_lines(file):
            instructions = line.split()
            num_to_move = int(instructions[1])
            from_stack = instructions[3]
            to_stack = instructions[5]
            move_crates(stacks, num_to_move, from_stack, to_stack)
    
    output = ""
    for stack in stacks.values():
        output += stack.get()
    return output


def part_2():
    with open(sys.argv[1]) as file:
        stacks = get_initial_stacks(file)
        
        for line in get_lines(file):
            instructions = line.split()
            num_to_move = int(instructions[1])
            from_stack = instructions[3]
            to_stack = instructions[5]
            move_crates(stacks, num_to_move, from_stack, to_stack, keep_order=True)
    
    output = ""
    for stack in stacks.values():
        output += stack.get()
    return output


if __name__ == "__main__":
    print(f"Part 1: {part_1()}")
    print(f"Part 2: {part_2()}")
