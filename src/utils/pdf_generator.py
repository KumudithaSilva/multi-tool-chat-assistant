from fpdf import FPDF
from datetime import datetime

class PDFGenerator:
    SHOP_NAME = "SuperMart"
    SHOP_ADDRESS = "123 Main Street, Colombo, Sri Lanka"
    SHOP_PHONE = "+94 77 123 4567"
    SHOP_EMAIL = "info@supermart.lk"

    def create_pdf(self, quote: dict, customer: str) -> str:
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()

        # HEADER
        pdf.set_font("Arial", "B", 18)
        pdf.cell(0, 10, self.SHOP_NAME, ln=True, align="C")
        pdf.set_font("Arial", "", 10)
        pdf.cell(0, 5, self.SHOP_ADDRESS, ln=True, align="C")
        pdf.cell(0, 5, f"Phone: {self.SHOP_PHONE} | Email: {self.SHOP_EMAIL}", ln=True, align="C")
        pdf.ln(7)

        # CUSTOMER INFO
        pdf.set_font("Arial", "", 11)
        pdf.cell(0, 6, f"Customer: {customer}", ln=True)
        pdf.cell(0, 6, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
        pdf.ln(7)

        # TABLE HEADER
        pdf.set_font("Arial", "B", 11)
        pdf.set_fill_color(200, 200, 200)  
        pdf.cell(80, 8, "Item", border=1, fill=True)
        pdf.cell(30, 8, "Qty", border=1, align="C", fill=True)
        pdf.cell(40, 8, "Price", border=1, align="R", fill=True)
        pdf.cell(40, 8, "Subtotal", border=1, align="R", fill=True)
        pdf.ln()

        # TABLE ROWS
        pdf.set_font("Arial", "", 12)
        for line in quote.get("quote_lines", []):
            price = line['subtotal'] / line['quantity'] if line['quantity'] else 0
            pdf.cell(80, 8, line['item'], border=1)
            pdf.cell(30, 8, str(line['quantity']), border=1, align="C")
            pdf.cell(40, 8, f"LKR {price:.2f}", border=1, align="R")
            pdf.cell(40, 8, f"LKR {line['subtotal']:.2f}", border=1, align="R")
            pdf.ln()

        # TOTAL
        pdf.set_font("Arial", "B", 12)
        pdf.cell(150, 8, "Total", border=1)
        pdf.cell(40, 8, f"LKR {quote.get('total', 0):.2f}", border=1, align="R")
        pdf.ln(15)

        # NOTES
        notes = quote.get("notes", [])
        if notes:
            pdf.set_font("Arial", "I", 10)
            pdf.cell(0, 6, "Notes:", ln=True)
            for note in notes:
                pdf.cell(0, 6, f"- {note}", ln=True)

        # FOOTER
        pdf.ln(10)
        pdf.set_font("Arial", "I", 10)
        pdf.multi_cell(0, 6, "Thank you for shopping at SuperMart! Visit again.\nTerms & conditions apply.", align="C")

        # SAVE FILE
        filename = f"receipt_{customer}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(filename)
        return filename


if __name__ == "__main__":
    quote = {
        "quote_lines": [
            {"item": "Apple", "quantity": 3, "subtotal": 300.00},
            {"item": "Bread", "quantity": 2, "subtotal": 400.00},
        ],
        "total": 700.00,
        "notes": ["Thank you for shopping with us!"]
    }
    generator = PDFGenerator()
    generator.create_pdf(quote, "John Doe")