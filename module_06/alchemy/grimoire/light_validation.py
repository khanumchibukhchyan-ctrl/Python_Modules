def validate_ingredients(ingredients: str):
    allowed = ["earth", "air", "fire", "water"]

    normalized = ingredients.lower()

    valid = any(a in normalized for a in allowed)

    status = "VALID" if valid else "INVALID"

    # Keep original formatting in output style
    pretty = ingredients.replace(",", ", ")

    return f"{pretty} - {status}"