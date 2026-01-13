import asyncio
from ..logging.loggers import Log, configure_logging
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import aiosmtplib
from flightdeck_etl.configurations.config import AppSettings


class EmailService:
    def __init__(self, settings: AppSettings):
        self.smtp_settings = settings.SMTPConfiguration

    async def send_email(
        self,
        user_name: str,
        client_name: str,
        project_name: str,
        email_template_path: str,
        email_subject: str,
        user_email: str,
        **kwargs
    ):
        Log.info("Starting EmailService.send_email...")

        try:
            # Load and format template
            template_path = Path(email_template_path)
            if not template_path.exists():
                raise FileNotFoundError(
                    f"Email template not found: {email_template_path}")

            html_template = template_path.read_text(encoding="utf-8")
            email_content = (
                html_template.replace("{user_name}", user_name)
                             .replace("{client_name}", client_name)
                             .replace("{project_name}", project_name)
            )
        except Exception as e:
            Log.error(
                f"Error reading or formatting email template: {e}")
            raise

        try:
            # Build message
            msg = MIMEMultipart()
            msg["From"] = self.smtp_settings.From
            msg["To"] = user_email
            msg["Subject"] = email_subject
            msg.attach(MIMEText(email_content, "html"))

            # Send email asynchronously
            await aiosmtplib.send(
                msg,
                hostname=self.smtp_settings.Host,
                port=self.smtp_settings.Port,
                start_tls=True,
                username=self.smtp_settings.UserName,
                password=self.smtp_settings.Password,
            )

            Log.info("Email sent successfully to %s", user_email)
        except Exception as e:
            Log.error(f"Error sending email: {e}")
            raise
