def secure_archive(file_dir: str,
                   action: str = "r", content: str = "") -> tuple[bool, str]:
    try:
        with open(file_dir, action) as file:
            if action == "w":
                file.write(content)
                return (True, 'Content successfully written to file')
            return (True, file.read())
    except Exception as e:
        return (False, f"{e}")


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(f"{secure_archive("IDontExist.txt")}\n")
    print("Using 'secure_archive' to read from an inaccesible file file:")
    print(f"{secure_archive("/sgoinfre/aamini")}\n")
    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("ancient_fragment.txt")
    print(f"{content}\n")
    print("Using 'secure_archive' to write previous content to a new file")
    print(f"{secure_archive("new_file.txt", "w", content[1])}\n")


if __name__ == "__main__":
    ft_vault_security()
