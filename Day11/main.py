from game import Game


def main():
    INPUT_PATH = "input.txt"
    game = Game.from_file(INPUT_PATH)

    # Play 10000 turns
    game.play_n_turns(10000)

    # Get the 2 most active monkeys
    most_active = game.get_n_most_active_monkey(2)

    # Multiply the number of inspections together
    result = 1
    for monkey in most_active:
        result *= monkey.number_inspections

    print(f"Shenanigans result: {result}")


if __name__ == "__main__":
    main()
