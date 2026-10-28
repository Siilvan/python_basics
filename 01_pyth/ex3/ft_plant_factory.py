class Plant:
    def __init__(self, name, height, age1) -> None:
        self.name = name
        self.height = height
        self.age1 = age1

    def show(self) -> None:
        print(
            f"Created: {self.name}: {self.height:.1f}cm, {self.age1} days old")

    def age(self) -> None:
        self.age1 += 1

    def grow(self) -> None:
        self.height += 0.8


def ft_plant_factory():
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()


if __name__ == "__main__":
    ft_plant_factory()
