def validate_ingredients(ingredients: str):
    for ingredient in ("fire", "water", "earth", "air"):
        if ingredient in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
