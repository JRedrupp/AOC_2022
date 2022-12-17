import unittest

from backpack import Backpack, BackpackGroup

class TestBackpack(unittest.TestCase):
    def test_get_letters(self):
        # Test that get_letters returns the correct string of letters
        backpack = Backpack("abcdef")
        self.assertEqual(backpack.get_letters(), "abcdef")

    def test_split_string(self):
        # Test that split_string correctly splits the input string into two equal parts
        self.assertEqual(Backpack.split_string("abcdef"), ("abc", "def"))

class TestBackpackGroup(unittest.TestCase):
    def test_find_common_letter(self):
        # Test that find_common_letter returns the correct common letter
        backpacks = [Backpack("abc"), Backpack("ade"), Backpack("afg")]
        backpack_group = BackpackGroup(backpacks)
        self.assertEqual(backpack_group.find_common_letter(), "a")

    def test_get_priority(self):
        # Test that get_priority returns the correct priority for the common letter
        backpacks = [Backpack("abc"), Backpack("ade"), Backpack("afg")]
        backpack_group = BackpackGroup(backpacks)
        self.assertEqual(backpack_group.get_priority(), 1)
