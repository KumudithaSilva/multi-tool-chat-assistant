from tools.grocery.grocery_data import GROCERY_COUNTS

def check_item_exists(item: str) -> str:
    if not item:
        return "Item not provided."
    if item.lower() in GROCERY_COUNTS:
        return f"{item} exists in inventory."
    else:
        return f"{item} does not exist in inventory."