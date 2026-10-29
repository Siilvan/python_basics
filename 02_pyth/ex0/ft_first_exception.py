def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test = 25
    print(f"Input data is '{test}'")
    try:
        input_temperature(test)
        print(f"Temperature is now {test}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    test2 = 'abc'
    print(f"Input data is '{test2}'")
    try:
        input_temperature(test2)
        print(f"Temperature is now {test2}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()