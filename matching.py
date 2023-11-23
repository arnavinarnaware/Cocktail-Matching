# matching.py
def match_cocktail(selected_ingredients):
    mojito_ingredients = ["mint", "rum", "sugar", "lime", "soda water"]
    blush_ingredients = ["vodka", "cranberry juice", "orange juice", "lime"]
    martini_ingredients = ["vodka", "vermouth", "lemon"]

    if set(selected_ingredients) == set(mojito_ingredients):
        return "Mojito"
    elif set(selected_ingredients) == set(blush_ingredients):
        return "Vodka & Cranberry Blush"
    elif set(selected_ingredients) == set(martini_ingredients):
        return "Vodka Martini"
    else:
        return "No match found"
