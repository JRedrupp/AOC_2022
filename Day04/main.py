from __future__ import annotations

from assignments import AssignmentPair


def main():
    input_path = "input.txt"
    pairs = AssignmentPair.from_file(input_path)
    overlaps = sum([pair.is_range_overlap() for pair in pairs])
    print(f"Number of overlapping pairs: {overlaps}")


if __name__ == "__main__":
    main()
