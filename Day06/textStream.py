from collections import deque


class LookbackTextStream:
    def __init__(self, lookback: int = 4):
        self.__lookback: int = lookback
        self.__stream: deque = deque()
        self.counter: int = 0

    def add_and_check_marker(self, char: str) -> bool:
        """
        Add a character to the stream.
        Returns a bool for if the marker has been hit yet
        :param char: 
        :return: bool
        """
        self.__stream.extend(char)
        if len(self.__stream) > self.__lookback:
            self.__stream.popleft()
        self.counter += 1
        if not self._marker_hit():
            return False
        return True

    def _marker_hit(self) -> bool:
        """
        Check if the marker has been hit in the stream.
        The marker is considered hit if the stream contains exactly
        `self.lookback` characters and all characters in the stream
        are unique.
        :return: bool
        """
        # Check if the length of the stream is equal to self.lookback
        if len(self.__stream) != self.__lookback:
            return False

        # Check if all characters in the stream are unique
        unique_chars = set(self.__stream)
        if len(self.__stream) != len(unique_chars):
            return False

        # If both checks pass, the marker has been hit
        return True
