import streamlit as st
from datetime import datetime, timedelta
from database import SupabaseService

class WeeklyTaskManager:
    """Handles rendering and business logic for the Weekly Todo section."""
    def __init__(self, db_service: SupabaseService, user_id):
        self.db = db_service
        self.user_id = user_id
        self.current_week = (datetime.now().date() - timedelta(days=datetime.now().date().weekday())).strftime("%Y-%m-%d")

    def run_rollover(self):
        try:
            past_unfinished = self.db.get_todos(
                self.user_id, "weekly", is_completed=False, lt_week_start_date=self.current_week
            )
            if past_unfinished:
                for item in past_unfinished:
                    self.db.update_todo(item['id'], {'week_start_date': self.current_week})
                st.toast("Unfinished tasks rolled over to this week! 🔄")
        except Exception as e:
            print(f"Rollover failed: {e}")

    def handle_add_task(self):
        task_text = st.session_state.get("weekly_input", "").strip()
        if task_text:
            self.db.add_todo({
                'task': task_text, 'user_id': self.user_id, 'type': 'weekly',
                'is_completed': False, 'week_start_date': self.current_week
            })
            st.session_state["weekly_input"] = ""
            st.toast("Weekly task added! 📅")
        else:
            st.error("Please enter a task.")

    def render(self):
        st.subheader("This Week's Commitments")
        st.text_input("Add a task for this week:", key="weekly_input")
        st.button("Add Weekly Task", on_click=self.handle_add_task, key="btn_add_weekly")

        todos = self.db.get_todos(self.user_id, "weekly", week_start_date=self.current_week)
        if todos:
            for todo in todos:
                edit_key = f"edit_weekly_{todo['id']}"
                if edit_key not in st.session_state:
                    st.session_state[edit_key] = False

                if st.session_state[edit_key]:
                    col1, col2 = st.columns([0.8, 0.2])
                    with col1:
                        updated_text = st.text_input("Edit", value=todo['task'], key=f"w_txt_{todo['id']}", label_visibility="collapsed")
                    with col2:
                        if st.button("💾 Save", key=f"w_sv_{todo['id']}"):
                            if updated_text:
                                self.db.update_todo(todo['id'], {'task': updated_text})
                                st.session_state[edit_key] = False
                                st.rerun()
                else:
                    col1, col2, col3, col4 = st.columns([0.1, 0.6, 0.15, 0.15])
                    with col1:
                        is_done = st.checkbox("", value=todo['is_completed'], key=f"chk_{todo['id']}")
                        if is_done != todo['is_completed']:
                            self.db.update_todo(todo['id'], {'is_completed': is_done})
                            st.rerun()
                    with col2:
                        st.markdown(f"~~{todo['task']}~~" if todo['is_completed'] else todo['task'])
                    with col3:
                        if st.button("✏️", key=f"w_ed_{todo['id']}"):
                            st.session_state[edit_key] = True
                            st.rerun()
                    with col4:
                        if st.button("❌", key=f"w_dl_{todo['id']}"):
                            self.db.delete_todo(todo['id'])
                            st.rerun()
        else:
            st.write("No tasks for this week yet.")

        with st.expander("📦 View Passed Weeks Backup (Finished Tasks)"):
            past_completed = self.db.get_todos(self.user_id, "weekly", is_completed=True, lt_week_start_date=self.current_week)
            if past_completed:
                for past_todo in past_completed:
                    st.write(f"✅ **{past_todo['task']}** *(Week of {past_todo['week_start_date']})*")
            else:
                st.write("No archived history found.")
