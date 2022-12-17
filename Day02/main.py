from __future__ import annotations

from game import Game


def main():
    input_path: str = "input.txt"
    game = Game.from_file(input_path)
    game.play_all_turns()
    print(f"Final Score is: {game.get_total_score()}")


if __name__ == "__main__":
    main()
