from typing import Dict

from interfaces.tools.i_tool import ITool
from utils.item_price import get_item_price


class GetItemPriceTool(ITool):

    # Use default ITool schema generation based on class attributes
    description = "Get the price of an item"
    parameters = {
        "type": "object",
        "properties": {
            "item": {"type": "string", "description": "The grocery item name"}
        },
        "required": ["item"],
        "additionalProperties": False,
    }

    @property
    def name(self) -> str:
        return "get_item_price"

    def execute(self, arguments: Dict) -> str:
        item = arguments.get("item")
        return get_item_price(item)
