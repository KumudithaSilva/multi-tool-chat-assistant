from typing import Dict

from interfaces.tools.i_tool import ITool
from utils.generate_quote import generate_quote


class GenerateQuoteTool(ITool):

    description = "Generate a price quote for multiple grocery items"
    parameters = {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "description": "List of items to quote",
                "items": {
                    "type": "object",
                    "properties": {
                        "item": {"type": "string"},
                        "quantity": {"type": "integer"},
                    },
                    "required": ["item", "quantity"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["items"],
        "additionalProperties": False,
    }

    @property
    def name(self) -> str:
        return "generate_quote"

    def execute(self, arguments: Dict) -> str:
        items = arguments.get("items", [])
        return generate_quote(items)
