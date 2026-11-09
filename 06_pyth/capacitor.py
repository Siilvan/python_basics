import ex3.factories as fact


def main() -> None:
    transform_fact = fact.TransformCreatureFactory
    base = transform_fact.create_base()
    evolved = transform_fact.create_evolved()
    print(
        f" base:\n{base.describe()}\n{base.attack()}\n"
        f"{base.transform()}\n{base.attack()}\n{base.revert()}")
    print(
        f" evolved:\n{evolved.describe()}\n{evolved.attack()}\n"
        f"{evolved.transform()}\n{evolved.attack()}\n{evolved.revert()}")


if __name__ == "__main__":
    main()