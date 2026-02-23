import mailtrap as mt

from infrastructure.dotenv import DotEnvLoader
from infrastructure.email_provider import EmailApiKeyProvider
from interfaces.infra.i_api_key_provider import IApiKeyProvider
from interfaces.infra.i_env_loader import IEnvLoader
from utils.email_template import HtmlEmailTemplate


class EmailService:
    def __init__(
        self,
        env_loader: IEnvLoader = None,
        key_provider: IApiKeyProvider = None,
    ):

        if env_loader is None:
            env_loader = DotEnvLoader()

        if key_provider is None:
            key_provider = EmailApiKeyProvider(env_loader)

        email_api_key = key_provider.get_api_key()
        self.client = mt.MailtrapClient(token=email_api_key)

    def send_email(
        self,
        recipient_email: str,
        text: dict,
        sender_email: str = "hello@demomailtrap.co",
        sender_name: str = "SuperMart",
        subject: str = "SuperMart Receipt",
    ):
        email_template = HtmlEmailTemplate(quote=text)
        receipt_html = email_template.build_receipt_html()
        
        mail = mt.Mail(
            sender=mt.Address(email=sender_email, name=sender_name),
            to=[mt.Address(email=recipient_email)],
            subject=subject,
            html=receipt_html, 
            category="Integration Test",
        )

        response = self.client.send(mail)

        if response.get('success'):
            return f"Email sent to {recipient_email}"
        else:
            return f"Error sending email to {recipient_email}"


if __name__ == "__main__":

    email_service = EmailService()
    email_test = email_service.send_email(
        sender_email="hello@demomailtrap.co",
        sender_name="SuperMart",
        recipient_email="kumuditha99@outlook.com ",
        subject="Test Email",
        text="Testing Mailtrap API",
    )

    print(email_test)
