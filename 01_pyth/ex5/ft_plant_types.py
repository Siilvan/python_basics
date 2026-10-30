class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        if height >= 0:
            self.__height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            return
        if age >= 0:
            self.__age = age
        else:
            print(f"{self.name}: Error, age can't be negative")
            return
        print(f"{self.show()}")

    def get_height(self) -> float:
        return self.__height

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {self.__height} days")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return

    def get_age(self) -> int:
        return self.__age

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return

    def show(self) -> str:
        return (f"{self.name}: {self.__height:.1f}" +
                f"cm, {self.__age} days old")

    def grow(self) -> None:
        self.__height += 2.1

    def age_plant(self) -> None:
        self.__age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = 0
        print(f"Color: {self.color}")
        self.has_bloomed()

    def bloom(self) -> None:
        self.bloomed = 1

    def has_bloomed(self) -> None:
        if self.bloomed == 1:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def get_info(self) -> None:
        print(super().show())
        print(f"Color: {self.color}")
        self.has_bloomed()


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter
        print(f"Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of " +
              f"{super().get_height():.1f}cm long " +
              f"and {self.diameter:.1f}cm wide.")

    def get_info(self) -> None:
        print(super().show())
        print(f"Trunk diameter: {self.diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow_and_age(self, amount: int) -> None:
        count = range(1, amount + 1)
        for i in count:
            super().age_plant()
            super().grow()
            self.nutritional_value += 1

    def get_info(self) -> None:
        print(super().show())
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.bloom()
    print("")
    rose.get_info()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.grow_and_age(20)
    tomato.get_info()


if __name__ == "__main__":
    ft_plant_types()
