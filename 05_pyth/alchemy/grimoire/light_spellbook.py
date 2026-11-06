def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from . import light_validator
    validated: str = light_validator.validate_ingredients(ingredients)
    prefix = f"Spell {"recorded " if "VALID" in validated else "rejected "}"
    return (f"{prefix}{spell_name} {validated}")
