import unittest

from compartment import Compartment
class TestCompartment(unittest.TestCase):
    def test_get_items(self):
        compartment = Compartment('books, pencils, erasers')
        self.assertEqual(compartment.get_items(), 'books, pencils, erasers')

    def test_get_items_empty(self):
        compartment = Compartment('')
        self.assertEqual(compartment.get_items(), '')

    def test_get_items_single(self):
        compartment = Compartment('book')
        self.assertEqual(compartment.get_items(), 'book')


    def test_get_items_none(self):
        compartment = Compartment(None)
        self.assertEqual(compartment.get_items(), None)

if __name__ == '__main__':
    unittest.main()