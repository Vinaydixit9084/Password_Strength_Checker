import streamlit as st
from Password_Strength_Checker import check_password_strength
def main():
    st.title("Password Strength Checker")
    
    password = st.text_input("Enter your password", type="password")
    
    if st.button("Check Password"):
        if password:
            result = check_password_strength(password)
            st.success(result)
        else:
            st.error("Please enter a password to check.")

if __name__ == "__main__":
    main()
    

