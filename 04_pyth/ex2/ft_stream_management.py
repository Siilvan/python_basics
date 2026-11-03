import sys


class InvalidArgument(Exception):
    pass


def ft_save_file(content: str) -> None:
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_file_dir = sys.stdin.readline().rstrip()
    if not new_file_dir:
        print('Not saving data.\n')
        return
    print(f"Saving data to '{new_file_dir}'")
    new_file = open(new_file_dir, "w")
    new_file.write(content)
    new_file.close()
    print(f"data saved in file '{new_file_dir}'.\n")


def ft_new_content(file_dir: str) -> None:
    print('Transform data:')
    file = open(file_dir, "r")
    content = file.read().splitlines()
    new_lines = [line + '#\n' for line in content]
    new_content = "".join(new_lines)
    print(f'---\n\n{new_content}\n\n---')
    ft_save_file(new_content)


def ft_read_text() -> None:
    if len(sys.argv) != 2:
        raise InvalidArgument("ft_ancient_text.py <file>")
    print('=== Cyber Archives Recovery ===')
    file_dir = sys.argv[1]
    print(f"Accessing file'{file_dir}'")
    file = open(file_dir, "r")
    print(f"---\n\n{file.read()}\n\n---")
    file.close()
    print(f"File '{file_dir}' closed.\n")
    ft_new_content(file_dir)


def main() -> None:
    try:
        ft_read_text()
    except OSError as e:
        print("[STDERR] Error opening file"
              f"{sys.argv[1]}': {e}", file=sys.stderr)
    except InvalidArgument as e:
        print(f"[STDERR] Usage: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
