class Plant:

    class Counter:
        def __init__(self) -> None:
            self.counts = {
                "grow": 0,
                "age": 0,
                "show": 0
            }

        def record(self, method_name) -> None:
            if method_name in self.counts:
                self.counts[method_name] += 1
            else:
                self.counts[method_name] = 1

    def __init__(self, name, height, age, grow_rate) -> None:
        self.name = name
        self.grow_rate = grow_rate
        self.set_height(height)
        self.set_age(age)
        self.stats = self.Counter()

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

    def show(self) -> None:
        self.stats.record("show")
        print(f"{self.name}: {self.__height:.1f}" +
              f"cm, {self.__age} days old")

    def grow(self, amount=1) -> None:
        self.stats.record("grow")
        self.__height += (self.grow_rate * amount)

    def age_plant(self, amount=1) -> None:
        self.stats.record("age")
        self.__age += amount

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

    def bloom(self) -> None:
        self.bloomed = True

    def has_bloomed(self) -> None:
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        self.has_bloomed()


class Seed(Flower):
    def __init__(self, name, height, age, grow_rate, color):
        super().__init__(name, height, age, grow_rate, color)
        self.seeds = 0

    def show(self):
        super().show()
        if self.bloomed:
            self.seeds = 42
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name, height, age, grow_rate, diameter) -> None:
        super().__init__(name, height, age, grow_rate)
        self.diameter = diameter
        self.stats.counts["shade"] = 0

    def produce_shade(self) -> None:
        self.stats.record("shade")
        print(f"Tree {self.name} now produces a shade of " +
              f"{super().get_height():.1f}cm long " +
              f"and {self.diameter:.1f}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, grow_rate,
                 harvest_season, nutritional_value) -> None:
        super().__init__(name, height, age, grow_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def g_a(self, amount) -> None:
        super().age_plant(amount)
        super().grow(amount)
        self.nutritional_value += 1

    def show(self):
        print(super().show())
        print(f" Harvest season: {self.harvest_season}")
        print(f" utritional value: {self.nutritional_value}")


def display_stats(plant):
    stats = plant.stats.counts
    res = "Stats:"
    print(f"[statistics for {plant.name}]")
    for x in stats:
        res += f" {stats[x]} {x},"
    print(res)


def ft_garden_analytics():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    check = 30
    print(f"Is {check} days more than a year? -> {Plant.check_year(check)}")
    check = 400
    print(f"Is {check} days more than a year? -> {Plant.check_year(check)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, 8, "red")
    rose.show()
    display_stats(rose)
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.bloom()
    rose.grow()
    rose.show()
    display_stats(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 2, 5)
    oak.show()
    display_stats(oak)
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("\n=== Seed")
    sun = Seed("Sunflower", 80, 45, 30, "yellow")
    sun.show()
    print(f"[make {sun.name} grow, age and bloom]")
    sun.bloom()
    sun.grow()
    sun.age_plant(20)
    sun.show()
    display_stats(sun)
    print("\n=== Anonymous")
    ano = Plant.unknown()
    ano.show()
    display_stats(ano)


def main():
    ft_garden_analytics()


if __name__ == "__main__":
    main()
