import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topic.csv")

st.header("Contact")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        "what topic do you want to discuss?",
        df["topic"])
    raw_message = st.text_area("Your message")

    # ✅ Correct SMTP formatting with blank line after headers
    message = f"""\
Subject: New email from  {user_email}

From: {user_email}
topic {option}

{raw_message}
"""

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(message)
        st.success("Email sent successfully!")
