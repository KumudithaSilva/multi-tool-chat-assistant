from typing import Dict

from interfaces.tools.i_tool import ITool
from utils.item_count import get_item_count


class GetItemCountTool(ITool):

    # Use default ITool schema generation based on class attributes
    description = "Get available stock count of an item"
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
        return "get_count_item"

    def execute(self, arguments: Dict) -> str:
        item = arguments.get("item")
        return get_item_count(item)
