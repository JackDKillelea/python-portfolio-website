import streamlit as st
import send_email

st.set_page_config(page_title="Jack Killelea - Contact Me")

st.header("Contact Me")
with st.form(key="form"):
    email_address = st.text_input("Your email address")
    msg = st.text_area("Enter your message")
    button = st.form_submit_button("Contact Me")

    formatted_message = f"""\
Subject: Contact me - Portfolio Website
    
Sender: {email_address}
{msg}
"""

    if button:
        send_email.email(formatted_message)
        st.info("Email sent successfully.")
