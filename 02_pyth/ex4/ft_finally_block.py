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


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n.. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    plants = ["Tomato", "lettuce", "Carrots"]
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n.. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
