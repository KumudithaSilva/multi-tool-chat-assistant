from interfaces.tools.i_tool import ITool
from utils.pdf_generator import PDFGenerator


class GenerateReceiptPDFTool(ITool):

    parameters = {
        "type": "object",
        "properties": {
            "customer_name": {
                "type": "string",
                "description": "Name of the customer for the PDF receipt",
            },
            "quote": {
                "type": "object",
                "description": "Structured quote data",
                "properties": {
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
                "required": ["quote_lines", "total"],
                "additionalProperties": False,
            },
        },
        "required": ["customer_name", "quote"],
        "additionalProperties": False,
    }

    @property
    def name(self) -> str:
        return "generate_receipt_pdf"

    def execute(self, arguments: dict) -> str:
        quote = arguments["quote"]
        customer = arguments["customer_name"]

        pdf_gen = PDFGenerator()
        filename = pdf_gen.create_pdf(quote, customer)
        return f"PDF receipt generated: {filename}"
