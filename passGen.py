import random
import string
import pyperclip
import streamlit as st

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    if st.button("Copy Generated Password"):
        pyperclip.copy(password)
    return password
