import smtplib
from email.message import EmailMessage


def send_ticket_email(
        sender_email,
        app_password,
        recipient_email,
        pdf_file
):

    msg = EmailMessage()

    msg["Subject"] = (
        "Your Flight Ticket"
    )

    msg["From"] = sender_email

    msg["To"] = recipient_email

    msg.set_content(
        "Please find your flight ticket attached."
    )

    with open(pdf_file, "rb") as f:

        pdf_data = f.read()

        msg.add_attachment(
            pdf_data,
            maintype="application",
            subtype="pdf",
            filename=pdf_file.split("/")[-1]
        )

    with smtplib.SMTP(
            "smtp.gmail.com",
            587
    ) as smtp:

        smtp.starttls()

        smtp.login(
            sender_email,
            app_password
        )

        smtp.send_message(msg)

    return True