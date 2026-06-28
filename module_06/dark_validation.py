from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()

    normalized = ingredients.lower()

    valid = any(a in normalized for a in allowed)

    status = "VALID" if valid else "INVALID"

    return f"{ingredients} - {status}"