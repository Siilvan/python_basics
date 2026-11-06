def healing_potion() -> str:
    from . import elements
    return (f"Healing potion brewed with "
            f"'{elements.create_earth()}' and '{elements.create_air()}'")


def strength_potion() -> str:
    import elements
    return (f"Strength potion brewed with "
            f"'{elements.create_fire()}' and '{elements.create_water()}'")
