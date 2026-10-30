class Plant:
    def __init__(self, name: str, height: float, age1: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age1 = age1
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age1} days old")

    def age(self) -> None:
        self.age1 += 1

    def grow(self) -> None:
        self.height += self.growth_rate


def ft_plant_growth() -> None:
    start_h = 25
    rose = Plant("Rose", start_h, 30, 0.8)
    days = range(1, 8)

    print("=== Garden Plant Growth ===")
    rose.show()
    for i in days:
        print(f"=== Day {i} ===")
        rose.age()
        rose.grow()
        rose.show()
    print(f"Growth this week: {round(rose.height - start_h, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
