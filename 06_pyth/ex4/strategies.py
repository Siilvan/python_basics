from abc import ABC, abstractmethod
from typing import Any
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
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{type(creature).__name__}' "
                f"for this {type(self).__name__}"
            )
        transform_creature: Any = creature
        print(transform_creature.transform())
        print(transform_creature.attack())
        print(transform_creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Transformcapability):
            return True
        return False
