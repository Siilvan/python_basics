from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Transformcapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Shiftling(Creature, Transformcapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.attackstr: str = f"{self.name} attacks normally."

    def attack(self) -> str:
        return self.attackstr

    def revert(self) -> str:
        return "Shiftling returns to normal."

    def transform(self) -> str:
        self.attackstr = f"{self.name} performs a boosted strike!"
        return "Shiftling shifts into a sharper form!"


class Morphagon(Creature, Transformcapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        self.attackstr: str = f"{self.name} attacks normally."

    def attack(self) -> str:
        return self.attackstr

    def revert(self) -> str:
        return "Morphagon stabilizes its form."

    def transform(self) -> str:
        self.attackstr = "Morphagon unleashes a devastating morph strike!"
        return "Morphagon morphs into a dragonic battle form!"
