from cpu import CPU
from instructions import InstructionSet


def main():
    INPUT_PATH = "input.txt"
    VALS_TO_RETRIEVE = [20, 60, 100, 140, 180, 220]

    instruction_set = InstructionSet.from_file(INPUT_PATH)
    cpu = CPU()

    cpu.run_instructions(instruction_set.instructions)
    cpu.history[cpu.clock + 1] = cpu.x

    signal_strength = sum([cpu.history[i] * i for i in VALS_TO_RETRIEVE])
    print("###################################")
    print(f"Signal strength: {signal_strength}")
    print("###################################")
    print("")
    print("Render of the screen:")
    print("")
    cpu.print_screen()


if __name__ == "__main__":
    main()
