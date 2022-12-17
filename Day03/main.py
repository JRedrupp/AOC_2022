from __future__ import annotations

from backpack import BackpackGroup


def main():
    input_path = "input.txt"
    backpack_groups = BackpackGroup.create_backpack_groups_from_file(input_path)
    priorities = [i.get_priority() for i in backpack_groups]
    print(f"Sum of Priories is {sum(priorities)}")


if __name__ == "__main__":
    main()
