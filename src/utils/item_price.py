from tools.grocery.grocery_data import GROCERY_PRICES

def get_item_price(item: str) -> str:
    if not item:
        return "Item not provided."
    price = GROCERY_PRICES.get(item.lower(), "unknown item price")
    return f"The price of {item} is {price}."