import streamlit as st
from Password_Strength_Checker import check_password_strength
from passGen import generate_password
def main():
    st.title("Password Strength Checker")
    
    password = st.text_input("Enter your password", type="password")
    
    if st.button("Check Password"):
        if password:
            result = check_password_strength(password)
            st.success(result)
        else:
            st.error("Please enter a password to check.")
            
    st.title("Password Generator")

    if st.button("Generate Password"):
        password = generate_password()
        st.success(f"Generated Password: {password}")
        st.text_input("Generated Password", value=password, disabled=True)
        st.write("The generated password has been copied to your clipboard.")

if __name__ == "__main__":
    main()
    

