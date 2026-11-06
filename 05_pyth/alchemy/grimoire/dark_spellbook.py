from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eye-ball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validated: str = dark_validate_ingredients(ingredients)
    prefix = f"Spell {"recorded " if "VALID" in validated else "rejected "}"
    return (f"{prefix}{spell_name} {validated}")
