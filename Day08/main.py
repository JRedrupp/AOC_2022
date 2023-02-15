from __future__ import annotations

class Forest:

    def __init__(self, trees: list[list[int]]):
        self.trees = trees
        self.visible = self.get_visible_array()

    @classmethod
    def from_file(cls, path: str) -> Forest:
        """
        Create Forest class from file
        File Example:
            30373
            25512
            65332
            33549
            35390
        """
        with open(path) as f:
            trees = [[int(c) for c in line.strip()] for line in f]
        return cls(trees)

    def is_tree_visible(self, x: int, y: int) -> bool:
        """
        Given a Trees Location, x, y, determine if the tree is visible from the top, left, right, and bottom.
        A tree is visible if there are no other higher trees in the way.
        """
        if x < 0 or x >= len(self.trees[0]):
            return False
        if y < 0 or y >= len(self.trees):
            return False

        tree_height = self.trees[y][x]

        return self.check_all_directions(x, y, tree_height)

    def check_all_directions(self, x: int, y: int, tree_height: int) -> bool:
        """
        Check if any of the four sides of the tree
        are visible from outside the forest.
        """
        if self.check_top(x, y, tree_height):
            return True
        if self.check_bottom(x, y, tree_height):
            return True
        if self.check_left(x, y, tree_height):
            return True
        if self.check_right(x, y, tree_height):
            return True
        return False

    def check_top(self, x: int, y: int, tree_height: int) -> bool:
        for i in range(y - 1, -1, -1):
            if self.trees[i][x] >= tree_height:
                return False
        return True

    def check_bottom(self, x: int, y: int, tree_height: int) -> bool:
        for i in range(y + 1, len(self.trees)):
            if self.trees[i][x] >= tree_height:
                return False
        return True

    def check_left(self, x: int, y: int, tree_height: int) -> bool:
        for i in range(x - 1, -1, -1):
            if self.trees[y][i] >= tree_height:
                return False
        return True
    
    def check_right(self, x: int, y: int, tree_height: int) -> bool:
        for i in range(x + 1, len(self.trees[0])):
            if self.trees[y][i] >= tree_height:
                return False
        return True

    def get_visible_array(self) -> list[list[bool]]:
        """
        Return a 2D array of booleans where True represents a visible tree and False represents an invisible tree.
        """
        visible = [[False for _ in range(len(self.trees[0]))] for _ in range(len(self.trees))]
        for y in range(len(self.trees)):
            for x in range(len(self.trees[0])):
                visible[y][x] = self.is_tree_visible(x, y)
        return visible

    def number_visible(self) -> int:
        """
        Return the number of visible trees.
        """
        return sum([sum([1 for x in row if x]) for row in self.visible])

    def calculate_scenic_score(self, x: int, y: int) -> int:
        """
        Given a Trees Location, x, y, calculate the scenic score.
        The scenic score is the total number of trees visible in each direction from the given tree.
        """
        if x <= 0 or x >= len(self.trees[0])-1:
            return 0
        if y <= 0 or y >= len(self.trees)-1:
            return 0

        tree_height = self.trees[y][x]

        top = self.calculate_top(x, y, tree_height)
        bottom = self.calculate_bottom(x, y, tree_height)
        left = self.calculate_left(x, y, tree_height)
        right = self.calculate_right(x, y, tree_height)

        return top * bottom * left * right

    def calculate_top(self, x: int, y: int, tree_height: int) -> int:
        count = 0
        for i in range(y - 1, -1, -1):
            count += 1
            if self.trees[i][x] >= tree_height:
                break
        return count

    def calculate_bottom(self, x: int, y: int, tree_height: int) -> int:
        count = 0
        for i in range(y + 1, len(self.trees)):
            count += 1
            if self.trees[i][x] >= tree_height:
                break
        return count

    def calculate_left(self, x: int, y: int, tree_height: int) -> int:
        count = 0
        for i in range(x - 1, -1, -1):
            count += 1
            if self.trees[y][i] >= tree_height:
                break
        return count

    def calculate_right(self, x: int, y: int, tree_height: int) -> int:
        count = 0
        for i in range(x + 1, len(self.trees[0])):
            count += 1
            if self.trees[y][i] >= tree_height:
                break
        return count
    
    def get_max_scenic_score(self) -> int:
        """
        Return the maximum scenic score.
        """
        max_score = 0
        for y in range(len(self.trees)):
            for x in range(len(self.trees[0])):
                score = self.calculate_scenic_score(x, y)
                if score > max_score:
                    max_score = score
        return max_score

def main():
    forest = Forest.from_file("input.txt")
    print(f"Number of Visible Trees: {forest.number_visible()}")
    print(f"Maximum Scenic Score: {forest.get_max_scenic_score()}")

if __name__ == "__main__":
    main()