"""
Tool schema definitions used by LLM.
"""

PRICE_FUNCTION = {
    "name": "get_item_price",
    "description": "Get the price of an item",
    "parameters": {
        "type": "object",
        "properties": {
            "item": {
                "type": "string",
                "description": "The grocery item name"
            }
        },
        "required": ["item"],
        "additionalProperties": False
    }
}

COUNT_FUNCTION = {
    "name": "get_count_item",
    "description": "Get available stock count of an item",
    "parameters": {
        "type": "object",
        "properties": {
            "item": {
                "type": "string",
                "description": "The grocery item name"
            }
        },
        "required": ["item"],
        "additionalProperties": False
    }
}

TOOLS = [
    {"type": "function", "function": PRICE_FUNCTION},
    {"type": "function", "function": COUNT_FUNCTION},
]