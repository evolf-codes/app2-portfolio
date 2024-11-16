import smtplib
import ssl
import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(message):
    host = "smtp.gmail.com"
    port = 465  # SSL port for Gmail's SMTP server

    # Retrieve email credentials securely from st.secrets
    username = st.secrets["GMAIL_USER"]
    email_password = st.secrets["EMAIL_PASSWORD"]

    receiver = "receiver-email@example.com"  # Replace with the receiver's email address

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to Gmail's SMTP server over SSL
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, email_password)  # Login using secrets
            server.sendmail(username, receiver, message)  # Send the email
            st.success("Email sent successfully!")
    except smtplib.SMTPException as e:
        st.error(f"Failed to send email: {e}")
