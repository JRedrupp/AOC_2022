from __future__ import annotations


class AssignmentRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __contains__(self, key: AssignmentRange) -> bool:
        xs = set(range(self.start, self.end + 1))
        return bool(xs.intersection(range(key.start, key.end + 1)))


class AssignmentPair:
    def __init__(self, range_1: tuple[int, int], range_2: tuple[int, int]):
        self.range_1 = AssignmentRange(range_1[0], range_1[1])
        self.range_2 = AssignmentRange(range_2[0], range_2[1])

    def is_range_overlap(self) -> bool:
        return self.range_1 in self.range_2

    @classmethod
    def from_file(cls, input_path: str) -> list[AssignmentPair]:
        assignment_pairs = []
        with open(input_path, 'r') as f:
            for line in f:
                assignment_pairs.append(cls.from_string(line.strip()))
        return assignment_pairs

    @classmethod
    def from_string(cls, string: str) -> AssignmentPair:
        pairs = string.split(',')
        ranges = [p.split('-') for p in pairs]
        return cls((int(ranges[0][0]), int(ranges[0][1])), (int(ranges[1][0]), int(ranges[1][1])))
