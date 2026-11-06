def validate_ingredients(ingredients: str) -> str:
    from . import light_spellbook as book
    valid: bool = False
    valid_ingredients = book.light_spell_allowed_ingredients()
    for v_ingredient in valid_ingredients:
        if v_ingredient in ingredients.lower():
            valid = True
    return (f"({ingredients} - {"VALID" if valid else "INVALID"})")
