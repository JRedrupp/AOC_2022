from monkey import Monkey


class Game:
    def __init__(self, monkeys: list[Monkey]):
        self.monkey_dict = {monkey.id: monkey for monkey in monkeys}

    @classmethod
    def from_file(cls, path: str):
        with open(path) as f:
            monkeys = [Monkey.from_str(x) for x in f.read().split("\n\n")]
        return cls(monkeys)

    def play_turn(self):
        for monkey in self.monkey_dict.values():
            if not monkey.items:
                continue
            for item in monkey.items:

                # Run the operation
                new_item = monkey.operation(item)

                # Add an inspection
                monkey.number_inspections += 1

                # Monkey gets bored, so divide by 3 and round down
                # new_item = new_item // 3

                # Modulo by Mod Const to keep things moving
                new_item = new_item % Monkey.MOD_CONST

                # Run the test
                result = monkey.test(new_item)

                # Run the decision
                monkey_id = monkey.decision(result)

                # Add the item to the next monkey
                self.monkey_dict[monkey_id].items.append(new_item)

            # Clear the items
            monkey.items = []

    def play_n_turns(self, n: int):
        for _ in range(n):
            self.play_turn()

    def get_n_most_active_monkey(self, n: int) -> list[Monkey]:
        """
        Return the n most active monkeys by number of inspections
        """
        return sorted(self.monkey_dict.values(), key=lambda x: x.number_inspections)[
            -n:
        ]
