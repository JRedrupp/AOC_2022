from typing import TextIO

from textStream import LookbackTextStream


def read_char(file_pointer: TextIO):
    c = file_pointer.read(1)
    if not c:
        raise EOFError
    return c


def main():
    input_path = "input.txt"
    text_stream = LookbackTextStream(lookback=14)
    with open(input_path, 'r') as fp:
        while True:
            try:
                c = read_char(fp)
                if text_stream.add_and_check_marker(c):
                    break
            except EOFError:
                print(f"End of file {input_path} reached.")
                break
            except Exception as e:
                print(f"ERROR: {e}")
    print(f"Marker hit at: {text_stream.counter}")


if __name__ == "__main__":
    main()
