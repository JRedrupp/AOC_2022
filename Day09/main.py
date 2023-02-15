from __future__ import annotations

import os
from typing import Optional

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Rope:
    """
    The Rope class will contain:
    1. The Head Position of the Rope -> (x, y)
    2. The Tail Position of the Rope -> (x, y)
    3. The History of Tail Positions of the rope -> [(x, y), (x, y), (x, y), ...]

    Methods:
    1. Move the rope in a direction -> None
    2. Positions Tail Visited -> int
    """

    def __init__(
        self, rope_pos: Optional[list[tuple[int, int]]] = None, rope_length: int = 2
    ) -> None:
        self.rope_pos = rope_pos if rope_pos else [(0, 0) for _ in range(rope_length)]
        self.tail_history = [self.rope_pos[-1]]

    def move(self, direction: str, number_times: int) -> None:
        """
        Move the Head of the rope in a direction for a number of times. If tail is no longer next to the Head, then move the tail towards the head.
        """
        for _ in range(number_times):
            x, y = self.rope_pos[0]
            if direction == "U":
                self.rope_pos[0] = (x, y + 1)
            elif direction == "D":
                self.rope_pos[0] = (x, y - 1)
            elif direction == "L":
                self.rope_pos[0] = (x - 1, y)
            elif direction == "R":
                self.rope_pos[0] = (x + 1, y)

            self.move_rest_of_rope()
            self.tail_history.append(self.rope_pos[-1])

    def move_rest_of_rope(self) -> None:
        """
        Move the rest of the rope based upon the position in the i-1 position.
        """
        for i in range(len(self.rope_pos) - 1):

            if self.next_to(self.rope_pos[i], self.rope_pos[i + 1]):
                return

            # Get the Vector from the tail to the head
            x1, y1 = self.rope_pos[i + 1]
            x2, y2 = self.rope_pos[i]
            x_vector, y_vector = x2 - x1, y2 - y1

            # Get the direction of the vector
            x_vector = 1 if x_vector > 0 else -1 if x_vector < 0 else 0
            y_vector = 1 if y_vector > 0 else -1 if y_vector < 0 else 0

            # Move the tail in the direction of the vector
            x, y = self.rope_pos[i + 1]
            self.rope_pos[i + 1] = (x + x_vector, y + y_vector)

    def next_to(self, pos1: tuple[int, int], pos2: tuple[int, int]) -> bool:
        """
        Check if two positions are next to each other.
        """
        x1, y1 = pos1
        x2, y2 = pos2

        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            return True
        elif abs(x1 - x2) <= 1 and abs(y1 - y2) == 0:
            return True
        elif abs(x1 - x2) == 0 and abs(y1 - y2) <= 1:
            return True
        else:
            return False

    def positions_tail_visited(self) -> int:
        """
        Return the number of unique positions the tail has visited.
        """
        return len(set(self.tail_history))


class Instruction:
    def __init__(self, direction: str, number_times: int) -> None:
        self.direction = direction
        self.number_times = number_times


class InstructionSet:
    def __init__(self, instructions: list[Instruction]) -> None:
        self.instructions = instructions

    @classmethod
    def from_file(cls, file_path: str) -> InstructionSet:
        """
        With an example input file, import into the InstructionSet class.
        Example input file:
        L 1
        R 1
        D 1
        R 2
        """
        with open(file_path, "r") as f:
            lines = f.readlines()

        instructions = []
        for line in lines:
            direction, number_times = line.split(" ")
            instructions.append(Instruction(direction, int(number_times)))

        return cls(instructions)


def main():
    INPUT_FILE = "input.txt"

    instruction_set = InstructionSet.from_file(INPUT_FILE)

    ### Part 1 ###
    rope = Rope(rope_length=2)
    for instruction in instruction_set.instructions:
        rope.move(instruction.direction, instruction.number_times)

    # Print the number of positions the tail has visited
    print(
        f"P1 - Number of positions the tail has visited: {rope.positions_tail_visited()}"
    )

    ### Part 2 ###
    rope = Rope(rope_length=10)
    for instruction in instruction_set.instructions:
        rope.move(instruction.direction, instruction.number_times)

    # Print the number of positions the tail has visited
    print(
        f"P2 - Number of positions the tail has visited: {rope.positions_tail_visited()}"
    )


if __name__ == "__main__":
    main()
