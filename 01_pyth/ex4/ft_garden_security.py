class Plant:
    def __init__(self, name, height, age,) -> None:
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
        print(f"Created: {self.show()} \n")

    def get_height(self) -> int:
        return self.__height

    def set_height(self, new_height) -> None:
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {self.__height} days")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return

    def get_age(self) -> int:
        return self.__age

    def set_age(self, new_age) -> None:
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return

    def show(self) -> str:
        return (f"{self.name}: {self.__height:}" +
                f"cm, {self.__age} days old")

    def grow(self) -> None:
        self.__height += 0.8


def ft_garden_security():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-10)
    rose.set_age(-3)
    print("\nCurrent state:", rose.show())


if __name__ == "__main__":
    ft_garden_security()
