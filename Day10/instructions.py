from enum import Enum
from typing import Optional


class Opcode(str, Enum):
    NOOP = "noop"
    ADDX = "addx"


class Instruction:
    def __init__(self, opcode: Opcode, value: Optional[int] = None):
        self.opcode = opcode
        self.value = value

    @classmethod
    def from_string(cls, instruction_string: str):
        """
        Creates an Instruction object from a string
        Example:
         - "addx 5" -> Instruction(Opcode.ADDX, 5)
         - "noop" -> Instruction(Opcode.NOOP, None)
        """
        instruction_string = instruction_string.strip()
        if " " in instruction_string:
            opcode, value = instruction_string.split(" ")
            value = int(value)
        else:
            opcode = instruction_string
            value = None
        return cls(Opcode(opcode), value)


class InstructionSet:
    def __init__(self, instructions: list[Instruction]):
        self.instructions = instructions

    @classmethod
    def from_file(cls, file_path: str):
        with open(file_path, "r") as f:
            instructions = [Instruction.from_string(line) for line in f.readlines()]
        return cls(instructions)
