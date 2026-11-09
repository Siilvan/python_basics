from abc import ABC
from typing import abstractmethod
from . import creatures as c


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> c.Creature:
        pass

    def create_evolved() -> c.Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base() -> c.Creature:
        return c.Flameling("Flameling", "Fire")

    def create_evolved() -> c.Creature:
        return c.Pyrodon("Pyrodon", "Fire/Flying")


class TransformCreatureFactory(CreatureFactory):
    def create_base():
        return c.Shiftling("Shiftling", "Normal")

    def create_evolved():
        return c.Morphagon("Morphagon", "Normal/Dragon")
