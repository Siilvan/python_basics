from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    valid: bool = False
    for allow in allowed:
        if allow in ingredients.lower():
            valid = True
    return (f"({ingredients} - {"VALID" if valid else "INVALID"})")
