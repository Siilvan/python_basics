def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "5" + 5
    return operation_number


def test_error_types() -> None:
    operation_nbrs = [0, 1, 2, 3, 4]

    print("=== Garden Error Types Demo ===")
    for nbr in operation_nbrs:
        print(f"Testing operation {nbr}...")
        try:
            garden_operations(nbr)
            print("Operation completed succesfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
