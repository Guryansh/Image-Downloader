import smtplib
import os
import sys
from email.message import EmailMessage
from email.utils import make_msgid

def send_email(attachment_path, recipient_email):
    # Email settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'gsingla2_be22@thapar.edu'  # Replace with your email
    sender_password = 'itbujdaijpsaswhr'      # Replace with your email password or app-specific password

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Here is your attachment'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content('Please find the attachment.')

    # Attach the file
    try:
        with open(attachment_path, 'rb') as attachment:
            # Add the attachment to the message
            file_data = attachment.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype='application', subtype='zip', filename=file_name)

    except Exception as e:
        print(f"Failed to attach the file: {e}")
        return

    # Connect to the server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sendToEmail.py <attachment_path> <recipient_email>")
    else:
        attachment_path = sys.argv[1]
        recipient_email = sys.argv[2]
        send_email(attachment_path, recipient_email)
