from __future__ import annotations

from stack import StackGroup


class Instruction:
    def __init__(self, number_of_times: int, start_pos: int, end_pos: int):
        self.number_of_times = number_of_times
        self.start_pos = start_pos
        self.end_pos = end_pos


class InstructionSet:
    """
    Grouping of Instructions.
    First Instruction in the Array is the first instruction to call
    """

    def __init__(self, instructions: list[Instruction]):
        self.instructions = instructions

    @classmethod
    def from_file(cls, file_path):
        instructions: list[Instruction] = []
        at_instructions = False
        with open(file_path, 'r') as f:
            for line in f:
                if not at_instructions and line != "\n":
                    continue
                if line == "\n":
                    at_instructions = True
                    continue
                split_lines = line.split()
                num = split_lines[1]
                _from = split_lines[3]
                _to = split_lines[5]
                instructions.append(Instruction(int(num), int(_from) - 1, int(_to) - 1))
        return cls(instructions)

    def apply(self, stack_group: StackGroup):
        for instruction in self.instructions:
            stack_group.apply_instruction(instruction)
