from typing import Callable


class Monkey:
    MOD_CONST = 1

    def __init__(
        self,
        id,
        operation: Callable[[int], int],
        test: Callable[[int], bool],
        decision: Callable[[bool], int],
        items: list[int] = [],
    ):
        self.id = id
        self.items = items
        self.number_inspections = 0
        self.operation = operation
        self.test = test
        self.decision = decision

    @classmethod
    def from_str(cls, string):
        """
        Create a Monkey from a string
        Example String:
            Monkey 0:
                Starting items: 79, 98
                Operation: new = old * 19
                Test: divisible by 23
                    If true: throw to monkey 2
                    If false: throw to monkey 3
        """
        ident, *rest = string.splitlines()
        ident = int(ident.split(" ")[1].split(":")[0])
        starting_items = [int(x) for x in rest[0].split(":")[1].split(",")]
        operation = rest[1].split(":")[1].strip()
        test = rest[2].split(":")[1].strip()
        decision = cls.create_decision_from_str(
            rest[3].split(":")[1].strip(), rest[4].split(":")[1].strip()
        )
        return cls(
            ident,
            cls.create_operation_from_string(operation),
            cls.create_test_from_string(test),
            decision,
            starting_items,
        )

    @classmethod
    def create_operation_from_string(cls, string) -> Callable[[int], int]:
        """
        Create a function from a string
        Examples:
            new = old * 19
            new = old + 6
            new = old * old
        """
        _, command = string.split("=")
        commands = command.strip().split(" ")
        assert len(commands) == 3
        if commands[0].isalpha() and commands[2].isalpha():
            return lambda x: x * x
        if commands[1] == "*":
            return lambda x: x * int(commands[2])
        if commands[1] == "+":
            return lambda x: x + int(commands[2])

        # Raise not implemented error
        raise NotImplementedError

    @classmethod
    def create_test_from_string(cls, string) -> Callable[[int], bool]:
        """
        Create a function from a string
        Examples:
            divisible by 23
            divisible by 13
            divisible by 7
        """
        divisor = string.split(" ")[-1]
        divisor = int(divisor)
        cls.MOD_CONST *= divisor
        return lambda x: x % divisor == 0

    @classmethod
    def create_decision_from_str(cls, true: str, false: str) -> Callable[[bool], int]:
        """
        Create a function from a string
        Example:
            true: throw to monkey 2
            false: throw to monkey 3
        """
        true_id = int(true.split(" ")[-1])
        false_id = int(false.split(" ")[-1])
        return lambda x: true_id if x else false_id
