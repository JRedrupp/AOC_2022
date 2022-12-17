from unittest import TestCase
from main import read_data, calculate_calories_per_elf


class ReadDataTest(TestCase):
    def test_read_data(self):
        path = "test_input.txt"
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(expected_output, read_data(path))

    def test_read_data_file_not_found(self):
        path = "non_existent_file.txt"
        with self.assertRaises(FileNotFoundError):
            read_data(path)


class CalculateCaloriesPerElfTest(TestCase):
    def test_calculate_calories_per_elf_empty_input(self):
        calories_lists = []
        with self.assertRaises(ValueError):
            calculate_calories_per_elf(calories_lists)

    def test_calculate_calories_per_elf(self):
        calories_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [6, 15, 24]
        self.assertEqual(sorted(expected_output, reverse=True), calculate_calories_per_elf(calories_lists))
