import streamlit as st
from database import SupabaseService

class AuthInterface:
    """Handles rendering the authentication screens."""
    def __init__(self, db_service: SupabaseService):
        self.db = db_service
        if "user" not in st.session_state:
            st.session_state.user = None

    def render(self):
        if st.session_state.user is not None:
            return True

        st.title("Welcome to Todo App")
        choice = st.sidebar.selectbox("Menu", ["Login", "SignUp"])
        email = st.text_input("Email", key="auth_email")
        password = st.text_input("Password", type="password", key="auth_password")

        if choice == "Login" and st.button("Login"):
            try:
                user = self.db.sign_in(email, password)
                if user:
                    st.session_state.user = user
                    st.rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")

        elif choice == "SignUp" and st.button("Sign Up"):
            try:
                user = self.db.sign_up(email, password)
                if user:
                    st.session_state.user = user
                    st.success("Signup successful! Please check your email.")
                    st.rerun()
            except Exception as e:
                st.error(f"Signup failed: {e}")

        st.stop()
