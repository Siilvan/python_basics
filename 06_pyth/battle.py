import ex3.factories as fct


def test_factory(factory: fct.CreatureFactory) -> None:
    print("\nTesting factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(fct1: fct.CreatureFactory, fct2: fct.CreatureFactory) -> None:
    print("\nTesting battle")
    base1 = fct1.create_base()
    base2 = fct2.create_base()
    print(f"{base1.describe()}\n vs.\n{base2.describe()}\n fight!")
    print(f"{base1.attack()}")
    print(f"{base2.attack()}")


def main() -> None:
    flame_factory = fct.FlameFactory()
    transform_factory = fct.TransformCreatureFactory()
    test_factory(flame_factory)
    test_factory(transform_factory)
    test_battle(flame_factory, transform_factory)


if __name__ == "__main__":
    main()
