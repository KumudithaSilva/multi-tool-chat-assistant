from typing import Dict

from interfaces.tools.i_tool import ITool
from utils.item_existence import check_item_exists


class CheckItemExistenceTool(ITool):

    description = "Check whether a grocery item exists in inventory"
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
        return "check_item_existence"

    def execute(self, arguments: Dict) -> str:
        item = arguments.get("item")
        return check_item_exists(item)
