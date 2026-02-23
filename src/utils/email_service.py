import mailtrap as mt

from infrastructure.dotenv import DotEnvLoader
from infrastructure.email_provider import EmailApiKeyProvider
from interfaces.infra.i_api_key_provider import IApiKeyProvider
from interfaces.infra.i_env_loader import IEnvLoader


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
        text: str,
        sender_email: str = "hello@demomailtrap.co",
        sender_name: str = "SuperMart",
        subject: str = "SuperMart Receipt",
    ):
        mail = mt.Mail(
            sender=mt.Address(email=sender_email, name=sender_name),
            to=[mt.Address(email=recipient_email)],
            subject=subject,
            text=text,
            category="Integration Test",
        )

        response = self.client.send(mail)
        return response


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
