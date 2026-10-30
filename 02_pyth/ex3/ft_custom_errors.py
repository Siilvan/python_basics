class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)
        self.message = message


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)
        self.message = message


def ft_custom_errors(err: str) -> None:
    if err == "GardenError":
        raise GardenError("Some garden error")
    elif err == "PlantError":
        raise PlantError("The tomato plant is wilting!")
    elif err == "WaterError":
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    errors: list[str] = ["PlantError", "WaterError"]
    for error in errors:
        print(f"\ntesting {error}....")
        try:
            ft_custom_errors(error)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nTesting catching all garden errors....")
    for error in errors:
        try:
            ft_custom_errors(error)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("\nAll custom errors work correctly!")


if __name__ == "__main__":
    test_custom_errors()
