import json
from typing import List, Dict

from interfaces.tools.i_tool import ITool
from interfaces.tools.i_tool_executor import IToolExecutor


class GroceryToolExecutor(IToolExecutor):

    def __init__(self, tools: List[ITool]):
        self._tool_registry = {tool.name: tool for tool in tools}

    def execute(self, message) -> List[Dict]:
        tool_messages = []

        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            tool = self._tool_registry.get(function_name)

            if tool:
                result = tool.execute(arguments)
            else:
                result = "Unknown function call."

            tool_messages.append({
                "role": "tool",
                "content": result,
                "tool_call_id": tool_call.id
            })

        return tool_messages