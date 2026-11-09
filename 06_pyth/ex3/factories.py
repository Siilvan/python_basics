from abc import ABC, abstractmethod
from . import creatures as c


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> c.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> c.Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> c.Creature:
        return c.Flameling("Flameling", "Fire")

    def create_evolved(self) -> c.Creature:
        return c.Pyrodon("Pyrodon", "Fire/Flying")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> c.Creature:
        return c.Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> c.Creature:
        return c.Morphagon("Morphagon", "Normal/Dragon")
