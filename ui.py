import streamlit as st
from Password_Strength_Checker import check_password_strength
from passGen import generate_password
import pyperclip

def main():
    st.title("Password Strength Checker")
    
    # Password Strength Checker Section
    password = st.text_input("Enter your password", type="password")
    if st.button("Check Password"):
        if password:
            result = check_password_strength(password)
            st.success(f"Password Strength: {result}")
        else:
            st.error("Please enter a password to check.")
    
    st.title("Password Generator")
    
    # Password Generator Section
    if st.button("Generate Password"):
        generated_password = generate_password()
        st.success(f"Generated Password: {generated_password}")
        st.text_input("Generated Password", value=generated_password, disabled=True)
        
        try:
            pyperclip.copy(generated_password)
            st.success("The generated password has been copied to your clipboard.")
        except pyperclip.PyperclipException as e:
            st.error("Failed to copy the password to clipboard. Please copy it manually.")

if __name__ == "__main__":
    main()
