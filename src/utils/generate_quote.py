import json

from tools.grocery.grocery_data import GROCERY_COUNTS, GROCERY_PRICES


def generate_quote(items: list) -> str:
    total = 0
    quote_lines = []
    notes = []

    for entry in items:
        item_name = entry["item"].lower()
        item_quantity = int(entry["quantity"])

        if item_name not in GROCERY_COUNTS:
            notes.append(f"{item_name} - unavailable")
            continue

        if item_name not in GROCERY_PRICES:
            notes.append(f"{item_name} - price unavailable")
            continue

        price = GROCERY_PRICES[item_name]
        item_total = price * item_quantity
        total += item_total

        quote_lines.append(
            {"item": item_name, "quantity": item_quantity, "subtotal": item_total}
        )

    quote_dict = {"quote_lines": quote_lines, "notes": notes, "total": total}
    return json.dumps(quote_dict, indent=2)
