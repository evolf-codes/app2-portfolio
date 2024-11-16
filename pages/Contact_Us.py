from send_email import send_email
import streamlit as st
st.header("Contact Me")

with st.form(key="emaiL_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}
{raw_message}"""
    button = st.form_submit_button()

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")

