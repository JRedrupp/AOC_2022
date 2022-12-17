from __future__ import annotations

from more_itertools import grouper

from compartment import Compartment
from utils import get_item_priority


class Backpack:
    def __init__(self, all_items: str):
        compartment_1_items, compartment_2_items = self.split_string(all_items)
        self.compartment_1: Compartment = Compartment(compartment_1_items)
        self.compartment_2: Compartment = Compartment(compartment_2_items)

    def get_letters(self) -> str:
        """Returns all the letters in both compartments of this backpack."""
        return self.compartment_1.get_items() + self.compartment_2.get_items()

    @staticmethod
    def split_string(value: str):
        """Splits the given string into two equal parts."""
        string1, string2 = value[:len(value) // 2], value[len(value) // 2:]
        return string1, string2


class BackpackGroup:
    GROUP_SIZE = 3

    def __init__(self, backpacks: list[Backpack]):
        self.backpacks = backpacks

    def find_common_letter(self):
        """Returns the first common letter among all the backpacks in this group."""
        letters = [set(bk.get_letters()) for bk in self.backpacks]
        l_1 = letters.pop()
        letter_intersection = l_1.intersection(*letters)
        return letter_intersection.pop()

    def get_priority(self) -> int:
        """Returns the priority of the first common letter among all the backpacks in this group."""
        letter = self.find_common_letter()
        return get_item_priority(letter)

    @classmethod
    def create_backpack_groups_from_file(cls, path: str) -> list[BackpackGroup]:
        """Creates a list of backpack groups from the given file."""
        backpacks = []
        with open(path) as f:
            for line in f:
                backpacks.append(Backpack(line.strip()))
        return [cls(group) for group in grouper(backpacks, cls.GROUP_SIZE)]
