import json
from typing import List, Dict

from interfaces.i_tool_executor import IToolExecutor
from utils.grocery_tools import get_item_price, get_count_item



class GroceryToolExecutor(IToolExecutor):
    """
    Executes grocery-related tool calls.
    """

    def execute(self, message) -> List[Dict]:
        tool_messages = []

        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            if function_name == "get_item_price":
                result = get_item_price(arguments.get("item"))

            elif function_name == "get_count_item":
                result = get_count_item(arguments.get("item"))

            else:
                result = "Unknown function call."

            tool_messages.append({
                "role": "tool",
                "content": result,
                "tool_call_id": tool_call.id
            })

        return tool_messages