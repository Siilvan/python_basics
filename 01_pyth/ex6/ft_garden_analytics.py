class Plant:
    def __init__(self, name, height, age, grow_rate) -> None:
        self.name = name
        self.grow_rate = grow_rate
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self.__height

    def set_height(self, new_height) -> None:
        if new_height >= 0:
            self.__height = new_height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return

    def get_age(self) -> int:
        return self.__age

    def set_age(self, new_age) -> None:
        if new_age >= 0:
            self.__age = new_age
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return

    def show(self) -> str:
        print(f"{self.name}: {self.__height:.1f}" +
              f"cm, {self.__age} days old")

    def grow(self) -> None:
        self.__height += self.grow_rate

    def age_plant(self) -> None:
        self.__age += 1

    @staticmethod
    def check_year(age) -> bool:
        return age > 365

    @classmethod
    def unknown(cls) -> "Plant":
        return cls("Unknown plant", 0, 0, 0)



class Flower(Plant):
    def __init__(self, name, height, age, grow_rate, color) -> None:
        super().__init__(name, height, age, grow_rate)
        self.color = color
        self.bloomed = False
        self.show()

    def bloom(self) -> None:
        self.bloomed = True

    def has_bloomed(self) -> None:
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        self.has_bloomed()

class Seed(Flower):
    def __init__(self, name, height, age, grow_rate, color, seeds):
        super().__init__(name, height, age, grow_rate, color)
        self.seeds = seeds
        if seeds > 0:
            self.bloomed = True

    def show(self):
        super().show()
        if self.bloomed:
            print(f"Seeds produced{self.seeds}")

class Tree(Plant):
    def __init__(self, name, height, age, diameter) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter
        self.get_info()

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of " +
              f"{super().get_height():.1f}cm long " +
              f"and {self.diameter:.1f}cm wide.")

    def get_info(self):
        print(super().show())
        print(f"Trunk diameter: {self.diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age,
                 harvest_season, nutritional_value) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.get_info()

    def g_a(self, amount) -> None:
        count = range(1, amount + 1)
        for i in count:
            super().age_plant()
            super().grow()
            self.nutritional_value += 1

    def get_info(self):
        print(super().show())
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def ft_garden_analytics():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    check: int = 30
    print(f"Is {check} days more than a year? -> {Plant.check_year(check)}")
    check = 400
    print(f"Is {check} days more than a year? -> {Plant.check_year(check)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, 8, "red")
    rose.bloom()
    print("")
    rose.show()
    print("\n=== Seed")
    sun = Seed("Sunflower", 80, 45, 30, "yellow", 0)
    print("")
    sun.show()
    print("\n=== Anonymous")
    ano = Plant.unknown()
    print(ano.show())

def main():
    ft_garden_analytics()

if __name__ == "__main__":
    main()
