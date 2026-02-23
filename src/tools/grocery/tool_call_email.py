from interfaces.tools.i_tool import ITool
from utils.email_service import EmailService


class EmailTool(ITool):

    parameters = {
        "type": "object",
        "properties": {
            "customer_email": {
                "type": "string",
                "description": "Email of the customer",
            },
            "quote": {
                "type": "object",
                "description": "Structured quote data",
                "properties": {
                    "customer_name": {
                        "type": "string",
                        "description": "Name of the customer for the email send",
                    },
                    "quote_lines": {
                        "type": "array",
                        "description": "List of items in the quote",
                        "items": {
                            "type": "object",
                            "properties": {
                                "item": {
                                    "type": "string",
                                    "description": "Name of the item",
                                },
                                "quantity": {
                                    "type": "number",
                                    "description": "Quantity purchased",
                                },
                                "subtotal": {
                                    "type": "number",
                                    "description": "Subtotal for this item (price x quantity)",
                                },
                            },
                            "required": ["item", "quantity", "subtotal"],
                            "additionalProperties": False,
                        },
                    },
                    "total": {
                        "type": "number",
                        "description": "Total amount for all items",
                    },
                    "notes": {
                        "type": "array",
                        "description": "Optional notes for the receipt",
                        "items": {"type": "string"},
                    },
                },
                "required": ["customer_name", "quote_lines", "total"],
                "additionalProperties": False,
            },
        },
        "required": ["customer_email", "quote"],
        "additionalProperties": False,
    }

    @property
    def name(self) -> str:
        return "send_receipt_email"

    def execute(self, arguments: dict) -> str:
        text = arguments["quote"]
        recipient_email = arguments["customer_email"]

        email_service = EmailService()
        email_response = email_service.send_email(
            recipient_email=recipient_email, text=text
        )

        return email_response
