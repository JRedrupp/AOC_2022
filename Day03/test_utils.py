import unittest

from utils import get_item_priority


class TestGetItemPriority(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(get_item_priority('a'), 1)
        self.assertEqual(get_item_priority('b'), 2)
        self.assertEqual(get_item_priority('c'), 3)
        self.assertEqual(get_item_priority('z'), 26)

    def test_uppercase(self):
        self.assertEqual(get_item_priority('A'), 27)
        self.assertEqual(get_item_priority('B'), 28)
        self.assertEqual(get_item_priority('C'), 29)
        self.assertEqual(get_item_priority('Z'), 52)

    def test_non_alphabetic(self):
        self.assertEqual(get_item_priority('1'), 0)
        self.assertEqual(get_item_priority('@'), 0)
        self.assertEqual(get_item_priority(' '), 0)


if __name__ == '__main__':
    unittest.main()
