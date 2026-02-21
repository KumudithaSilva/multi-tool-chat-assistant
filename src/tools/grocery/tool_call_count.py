from typing import Dict

from interfaces.tools.i_tool import ITool
from tools.grocery.grocery_data import GROCERY_COUNTS


class GetItemCountTool(ITool):

    # Use default ITool schema generation based on class attributes
    description = "Get available stock count of an item"
    parameters = {
        "type": "object",
        "properties": {
            "item": {"type": "string", "description": "The grocery item name"}
        },
        "required": ["item"],
        "additionalProperties": False
    }

    @property
    def name(self) -> str:
        return "get_count_item"

    def execute(self, arguments: Dict) -> str:
        item = arguments.get("item")
        if not item:
            return "Item not provided."

        count = GROCERY_COUNTS.get(item.lower(), "unknown item")
        return f"There are {count} of {item} in stock."