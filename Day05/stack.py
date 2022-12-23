from __future__ import annotations

from collections import deque

from instructions import Instruction

UNWANTED_CHARS = "[]"


class Stack:

    def __init__(self, crates: deque[str]):
        # End of the list is the top of the stack
        self.crates = crates

    def pop(self, n: int) -> list[str]:
        removed = []
        for _ in range(n):
            removed.append(self.crates.pop())
        removed.reverse()
        return removed

    def append(self, crates: list[str]):
        for crate in crates:
            self.crates.append(crate)

    @classmethod
    def from_list(cls, stack_list: list[str]):
        cleaned_stack = [cls.clean(s) for s in stack_list]

        # Remove Empty Strings
        cleaned_stack = list(filter(None, cleaned_stack))
        return cls(deque(cleaned_stack))

    @classmethod
    def clean(cls, crate_string: str):
        crate_string = crate_string.strip()
        for unwanted_char in UNWANTED_CHARS:
            crate_string = crate_string.replace(unwanted_char, '')
        return crate_string

    def get_top_crate(self):
        return self.crates[-1]


class StackGroup:
    def __init__(self, stacks: list[Stack]):
        self.stacks = stacks

    @classmethod
    def from_file(cls, file_path: str) -> StackGroup:
        split_size = 4
        stacks = []
        with open(file_path, 'r') as f:
            for line in f:
                if not "[" in line:
                    continue
                items = [line[i:i + split_size] for i in range(0, len(line), split_size)]
                for i, item in enumerate(items):
                    if not len(stacks) > i:
                        stacks.append([])
                    stacks[i].insert(0, item.strip())
        stack_groups = [Stack.from_list(s) for s in stacks]
        return cls(stack_groups)

    def apply_instruction(self, instruction: Instruction):
        items = self.stacks[instruction.start_pos].pop(instruction.number_of_times)
        self.stacks[instruction.end_pos].append(items)

    def get_top_crates(self):
        top_crates = []
        for stack in self.stacks:
            top_crates.append(stack.get_top_crate())
        return top_crates
