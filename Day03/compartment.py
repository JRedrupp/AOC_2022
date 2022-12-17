
class Compartment:
    def __init__(self, items: str):
        self.items = items

    def get_items(self) -> str:
        """Returns the items in this compartment."""
        return self.items
