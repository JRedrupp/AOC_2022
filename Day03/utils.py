

def get_item_priority(letter: str) -> int:
    """
    Returns the priority of the given letter.
    The priority of a lowercase letter is its ASCII value - ord('a') + 1.
    The priority of an uppercase letter is its ASCII value - ord('A') + 27.
    """
    if letter.islower():
        return ord(letter) - ord('a') + 1
    elif letter.isupper():
        return ord(letter) - ord('A') + 27
    return 0
