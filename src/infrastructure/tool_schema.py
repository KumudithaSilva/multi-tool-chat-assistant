from typing import List

from interfaces.tools.i_tool import ITool
from interfaces.tools.i_tool_schema import IToolSchema


class ToolSchemaGenerator(IToolSchema):

    def __init__(self, tools: List[ITool]):
        self._tools = tools

    def generate_schema(self):
        return [{"type": "function", "function": t.schema} for t in self._tools]
