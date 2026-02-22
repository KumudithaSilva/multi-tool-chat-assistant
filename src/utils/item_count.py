from tools.grocery.grocery_data import GROCERY_COUNTS

def get_item_count(item: str) -> str:
    if not item:
        return "Item not provided."
    count = GROCERY_COUNTS.get(item.lower(), "unknown item")
    return f"There are {count} of {item} in stock."