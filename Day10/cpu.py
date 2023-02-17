from instructions import Instruction, Opcode


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
