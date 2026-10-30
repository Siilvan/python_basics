class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self.name}: Error, height can't be negative")

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
        else:
            print(f"{self.name}: Error, age can't be negative")

    def show(self) -> str:
        return (f"{self.name}: {self._height:}" +
                f"cm, {self._age} days old")

    def grow(self) -> None:
        self._height += 0.8


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print(f"Created: {rose.show()}\n")
    ages = [30, -3]
    heights = [25, -10]
    for height in heights:
        rose.set_height(height)
        if rose.get_height() == height:
            print(f"Height updated: {rose.get_height()}cm\n")
        else:
            print("Height update rejected")
    print("")
    for age in ages:
        rose.set_age(age)
        if rose.get_age() == age:
            print(f"Age updated: {rose.get_age()} days\n")
        else:
            print("Age update rejected")
    print("\nCurrent state:", rose.show())


if __name__ == "__main__":
    ft_garden_security()
