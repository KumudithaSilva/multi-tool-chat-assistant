from tools.grocery_data import GROCERY_PRICES, GROCERY_COUNTS


def get_item_price(item: str) -> str:
    """Return price of requested grocery item."""
    if not item:
        return "Item not provided."

    price = GROCERY_PRICES.get(item.lower(), "unknown item price")
    return f"The price of {item} is {price}."


def get_count_item(item: str) -> str:
    """Return stock count of requested grocery item."""
    if not item:
        return "Item not provided."

    count = GROCERY_COUNTS.get(item.lower(), "unknown item")
    return f"There are {count} of {item} in stock."