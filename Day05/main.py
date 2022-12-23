from __future__ import annotations

from instructions import InstructionSet
from stack import StackGroup


def main():
    input_path = "input.txt"
    stack_group = StackGroup.from_file(input_path)
    instruction_set = InstructionSet.from_file(input_path)
    instruction_set.apply(stack_group)
    print(f"Top Crates are {''.join(stack_group.get_top_crates())}")


if __name__ == "__main__":
    main()
