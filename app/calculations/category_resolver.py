from app.weight_categories import WEIGHT_CATEGORIES

def get_category_from_hp(horsepower: int) -> str:
    for category in WEIGHT_CATEGORIES:
        if category["min_hp"] <= horsepower <= category["max_hp"]:
            return category["name"]
    return "Unknown"

def get_list_category_names():
    categories = [cat["name"] for cat in WEIGHT_CATEGORIES]
    return categories
