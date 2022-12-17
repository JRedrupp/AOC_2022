from typing import List


def read_data(path: str) -> List[List[int]]:

    calories_lists: list[list[int]] = []
    calories: list[int] = []
    with open(path, 'r') as file:
        for line in file:
            if line == '\n':
                calories_lists.append(calories)
                calories = []
            else:
                calories.append(int(line))
        if calories:
            calories_lists.append(calories)
    return calories_lists


def calculate_calories_per_elf(calories_lists: List[List[int]]) -> List[int]:
    if not calories_lists:
        raise ValueError('calories_lists must contain lists')
    calories_per_elf = [sum(list_item) for list_item in calories_lists]
    calories_per_elf = sorted(calories_per_elf, reverse=True)
    return calories_per_elf


def main(path: str) -> None:
    calories_lists: list[list[int]] = read_data(path)
    calories_per_elf: list[int] = calculate_calories_per_elf(calories_lists)
    print(sum(calories_per_elf[:3]))


if __name__ == "__main__":
    FILE_PATH = "input.txt"
    main(FILE_PATH)
