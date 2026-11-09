import ex3.factories as facts
from ex4 import strategies as strats


def battle(
        opponents: list[tuple[facts.CreatureFactory, strats.BattleStrategy]]
        ) -> None:
    enemies = []
    for factory, strategy in opponents:
        creature = factory.create_base()
        enemies.append((creature, strategy))
    print(f"*** Tournament ***\n{len(enemies)} opponents involved\n")
    print("* Battle *")
    descs = [enemy.describe() for enemy, strat in enemies]
    print(f"{"\n vs.\n".join(descs)}")
    print("now fight!")
    for enemy, strat in enemies:
        if not strat.is_valid(strat, enemy):
            raise Exception(
                f"Invalid Creature '{type(enemy).__name__}' "
                f"for this {strat.__name__}"
            )
        strat.act(strat, enemy)


def main() -> None:
    flame_fact = facts.FlameFactory
    transform_fact = facts.TransformCreatureFactory
    agressive = strats.AggressiveStrategy
    normal = strats.NormalStrategy
    print("Tournament 0 (basic)\n"
          " [ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle([(flame_fact, normal), (transform_fact, agressive)])
    print("\nTournament 1 (error)\n"
          " [ (Flameling+Aggressive), (Shiftling+Aggressive) ]")
    try:
        battle([(transform_fact, agressive), (flame_fact, agressive)])
    except Exception as e:
        print(f"Battle error, aboring tournament {e}")


if __name__ == "__main__":
    main()
