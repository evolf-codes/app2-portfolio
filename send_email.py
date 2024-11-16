import os
import smtplib
import ssl
import streamlit as st

def send_email(message):
    host = "smtp.gmail.com"
    port = "465"

    username = "eric.codes.qa@gmail.com"
    email_password = st.secrets["EMAIL_PASSWORD"]

    my_context = ssl.create_default_context()
    receiver = "eric.codes.qa@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, email_password)
        server.sendmail(username, receiver, message)
