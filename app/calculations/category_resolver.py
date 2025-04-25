from app.weight_categories import WEIGHT_CATEGORIES

def get_category_from_hp(horsepower: int) -> str:
    for category in WEIGHT_CATEGORIES:
        if category["min_hp"] <= horsepower <= category["max_hp"]:
            return category["name"]
    return "Unknown"

def get_list_category_names():
    categories = [cat["name"] for cat in WEIGHT_CATEGORIES]
    return categories

def get_category_feedback(horsepower: int) -> str:
    output = ""
    category = get_category_from_hp(horsepower=horsepower)
    for cat in WEIGHT_CATEGORIES:
        if cat["name"] == category:
            min_hp = cat["min_hp"]
            max_hp = cat["max_hp"]

            utilisation = ((horsepower - min_hp) / (max_hp - min_hp)) * 100
            utilisation = max(0, min(utilisation, 100))  # Limit percentage between 0 - 100

            output = f"Utilising {utilisation:.0f}% of the {min_hp}-{max_hp} {category.lower()} category power range"
    return output
