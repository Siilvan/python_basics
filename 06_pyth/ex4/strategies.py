from typing import abstractmethod
from abc import ABC
from ex3.creatures import Creature, Transformcapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        creature.transform()
        creature.attack()
        creature.revert()

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Transformcapability):
            return True
        return False
