import sys


def ft_command_quest() -> None:
    i = 1
    args = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    while i <= len(args[1:]):
        print(f"Argument {i}: {args[i]}")
        i += 1
    if i == 1:
        print("No arguments provided!")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    ft_command_quest()
