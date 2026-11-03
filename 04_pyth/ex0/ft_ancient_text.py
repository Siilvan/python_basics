import sys
import typing


class InvalidArgument(Exception):
    pass


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        raise InvalidArgument("ft_ancient_text.py <file>")
    print('=== Cyber Archives Recovery ===')
    file_dir = sys.argv[1]
    print(f"Accessing file'{file_dir}'")
    file = open(file_dir, "r")
    print(f"---\n\n{file.read()}\n\n---")
    file.close()
    print(f"File '{file_dir}' closed.")


def main() -> None:
    try:
        ft_ancient_text()
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except InvalidArgument as e:
        print(f'Usage: {e}')


if __name__ == "__main__":
    main()