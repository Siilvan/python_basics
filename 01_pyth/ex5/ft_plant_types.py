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

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}"
              f"cm, {self._age} days old")

    def grow(self) -> None:
        self._height += 2.1

    def age_plant(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = 0

    def bloom(self) -> None:
        self.bloomed = 1

    def has_bloomed(self) -> None:
        if self.bloomed == 1:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        self.has_bloomed()


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of " +
              f"{super().get_height():.1f}cm long " +
              f"and {self.diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow_and_age(self, amount: int) -> None:
        count = range(1, amount + 1)
        for i in count:
            super().age_plant()
            super().grow()
            self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[Asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[Asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.show()
    print("[Asking the tomato to grow and age for 20 days]")
    tomato.grow_and_age(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
