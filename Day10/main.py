from enum import Enum
from typing import Optional


# Python String Enum for all possible opcodes
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


class CPU:
    def __init__(self):
        self.screen = []
        self.history = {}
        self.x: int = 1
        self.clock = 0

    def run_instructions(self, instructions: list[Instruction]):
        for instruction in instructions:
            self.run_instruction(instruction)

    def run_instruction(self, instruction: Instruction):
        if instruction.opcode == Opcode.NOOP:
            self.increment_clock()
            pass
        elif instruction.opcode == Opcode.ADDX:
            self.increment_clock()
            self.increment_clock()
            self.x += instruction.value
        else:
            raise ValueError(f"Invalid opcode: {instruction.opcode}")

    def increment_clock(self):
        self.draw_screen()
        self.history[self.clock + 1] = self.x
        self.clock += 1

    def draw_screen(self):
        """
        Draw to the self.screen list
        Logic:
            - Always Draw at the end of the list
            - If the Index we are drawing at is self.x or self.x + 1, or self.x + 2, draw a '#' character
            - Otherwise, draw a '.' character
        """
        draw_pos = len(self.screen) % 40
        if draw_pos == self.x - 1 or draw_pos == self.x or draw_pos == self.x + 1:
            self.screen.append("#")
        else:
            self.screen.append(".")

    def print_screen(self):
        """
        Print the screen to the console, with each line being 40 characters long
        """
        for i in range(0, len(self.screen), 40):
            print("".join(self.screen[i : i + 40]))


def main():
    INPUT_PATH = "input.txt"
    VALS_TO_RETRIEVE = [20, 60, 100, 140, 180, 220]

    instruction_set = InstructionSet.from_file(INPUT_PATH)
    cpu = CPU()

    cpu.run_instructions(instruction_set.instructions)
    cpu.history[cpu.clock + 1] = cpu.x

    signal_strength = sum([cpu.history[i] * i for i in VALS_TO_RETRIEVE])
    print("###################################")
    print(f"Signal strength: {signal_strength}")
    print("###################################")
    print("")
    print("Render of the screen:")
    print("")
    cpu.print_screen()


if __name__ == "__main__":
    main()
