def input_temperature(temp_str: int | str) -> int | None:
    temp = int(temp_str)
    if temp <= 40 and temp >= 0:
        return temp
    elif temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    tests: list[int | str] = [25, 'abc', 41, -1]
    print("=== Garden Temperature Checker ===\n")
    for test in tests:
        print(f"Input data is '{test}'")
        try:
            result = input_temperature(test)
            print(f"The temperature is now: {result}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
