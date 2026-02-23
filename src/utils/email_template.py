from datetime import datetime
from utils.config_loader import ConfigLoader


class HtmlEmailTemplate:

    def __init__(self, quote: dict):
        shop_info = ConfigLoader.get_shop_info()
        self.shop_name = shop_info.get("name", "")
        self.shop_address = shop_info.get("address", "")
        self.shop_phone = shop_info.get("phone", "")
        self.shop_email = shop_info.get("email", "")
        self.quote = quote

    def build_receipt_html(self) -> str:
        
        rows = ""
        for line in self.quote.get("quote_lines", []):
            price = line["subtotal"] / line["quantity"] if line["quantity"] else 0
            rows += f"""
            <tr>
                <td style="padding:8px;border:1px solid #ddd;">{line['item']}</td>
                <td style="padding:8px;border:1px solid #ddd;text-align:center;">{line['quantity']}</td>
                <td style="padding:8px;border:1px solid #ddd;text-align:right;">LKR {price:.2f}</td>
                <td style="padding:8px;border:1px solid #ddd;text-align:right;">LKR {line['subtotal']:.2f}</td>
            </tr>
            """

        notes_html = ""
        for note in self.quote.get("notes", []):
            notes_html += f"<p style='margin:2px 0;'>- {note}</p>"

        html_content = f"""
        <html>
        <body style="font-family:Arial, sans-serif; line-height:1.5; color:#333;">
            <!-- HEADER -->
            <div style="text-align:center;">
                <h1 style="margin:0;">{ self.shop_name}</h1>
                <p style="margin:2px 0;font-size:12px;">{self.shop_address}</p>
                <p style="margin:2px 0;font-size:12px;">Phone: { self.shop_phone} | Email: { self.shop_email}</p>
            </div>

            <hr style="margin:15px 0;">

            <!-- CUSTOMER INFO -->
            <p><strong>Customer:</strong> {self.quote.get("customer_name", "")}</p>
            <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

            <!-- TABLE -->
            <table style="border-collapse:collapse;width:100%;max-width:600px;">
                <thead>
                    <tr style="background-color:#f2f2f2;">
                        <th style="padding:8px;border:1px solid #ddd;text-align:left;">Item</th>
                        <th style="padding:8px;border:1px solid #ddd;text-align:center;">Qty</th>
                        <th style="padding:8px;border:1px solid #ddd;text-align:right;">Price</th>
                        <th style="padding:8px;border:1px solid #ddd;text-align:right;">Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                    <tr style="font-weight:bold;">
                        <td colspan="3" style="padding:8px;border:1px solid #ddd;text-align:right;">Total</td>
                        <td style="padding:8px;border:1px solid #ddd;text-align:right;">LKR {self.quote.get('total', 0):.2f}</td>
                    </tr>
                </tbody>
            </table>
            <br>

            <!-- NOTES -->
            {notes_html}

            <hr style="margin:15px 0;">

            <!-- FOOTER -->
            <p style="text-align:center;font-size:12px;font-style:italic;">
                Thank you for shopping at {self.shop_name}! Visit again.<br>
                Terms & conditions apply.
            </p>
        </body>
        </html>
        """
        return html_content