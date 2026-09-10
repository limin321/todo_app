import streamlit as st
from dotenv import load_dotenv

# Import our custom feature modules
from database import SupabaseService
from auth import AuthInterface
from weekly_tasks import WeeklyTaskManager
from lifetime_goals import LifetimeGoalManager

load_dotenv()

class TodoApp:
    """The master orchestrator class bringing all components together."""
    
    # Add version info
    VERSION = "1.0.0"
    
    def __init__(self):
        self.db = SupabaseService()
        self.auth = AuthInterface(self.db)

    def run(self):
        # 1. Enforce user authentication
        self.auth.render()

        # 2. Render Global Sidebar Options
        st.sidebar.write(f"Logged in as: {st.session_state.user.email}")
        if st.sidebar.button("Logout"):
            self.db.sign_out()
            st.session_state.user = None
            st.rerun()

        # Add a subtle visual stamp for version info
        st.sidebar.caption(f"App Version: v{self.VERSION}")

        # 3. Initialize separate view modules
        user_id = st.session_state.user.id
        weekly_mgr = WeeklyTaskManager(self.db, user_id)
        lifetime_mgr = LifetimeGoalManager(self.db, user_id)

        # 4. Trigger rollover automation background logic
        weekly_mgr.run_rollover()

        # 5. Build main interface structure
        st.title("Supabase Productivity App")
        tab1, tab2 = st.tabs(["🗓️ Weekly Todo List", "🚀 Life-time Goals"])
        
        with tab1:
            weekly_mgr.render()
        with tab2:
            lifetime_mgr.render()

if __name__ == "__main__":
    app = TodoApp()
    app.run()
