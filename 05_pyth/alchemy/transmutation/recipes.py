def lead_to_gold() -> str:
    import elements as elem2
    from .. import elements as elem
    from .. import potions as pots
    return (f"Recipe transmuting Lead to Gold: brew '{elem.create_air()}' and "
            f"'{pots.strength_potion()}' mixed with '{elem2.create_fire()}'")
