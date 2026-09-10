import streamlit as st
from database import SupabaseService

class LifetimeGoalManager:
    """Handles rendering and business logic for the Categorized Lifetime Goals section."""
    def __init__(self, db_service: SupabaseService, user_id):
        self.db = db_service
        self.user_id = user_id
        self.categories = ["Study", "Travelling", "Food", "Fitness", "Career", "Other"]

    def handle_add_goal(self):
        task_text = st.session_state.lifetime_input_val.strip()
        selected_cat = st.session_state.lifetime_category_val
        if task_text:
            self.db.add_todo({
                'task': task_text, 'user_id': self.user_id, 'type': 'lifetime',
                'is_completed': False, 'category': selected_cat
            })
            st.toast(f"Added to {selected_cat}! 🎯")
        else:
            st.error("Please enter a goal text.")

    def render(self):
        st.subheader("Life-time Bucket List")
        col_input, col_cat = st.columns([0.7, 0.3])
        with col_input:
            st.text_input("Add a lifetime aspiration:", key="lifetime_input_val")
        with col_cat:
            st.selectbox("Category", self.categories, key="lifetime_category_val")

        st.button("Add Life-time Goal", on_click=self.handle_add_goal)
        st.markdown("---")

        chosen_filter = st.selectbox("Filter Goals By Category:", ["All"] + self.categories)
        filters = {} if chosen_filter == "All" else {"category": chosen_filter}
        
        goals = self.db.get_todos(self.user_id, "lifetime", **filters)
        if goals:
            for todo in goals:
                edit_key = f"edit_life_{todo['id']}"
                if edit_key not in st.session_state:
                    st.session_state[edit_key] = False

                if st.session_state[edit_key]:
                    col1, col2 = st.columns([0.8, 0.2])
                    with col1:
                        updated_text = st.text_input("Edit text", value=todo['task'], key=f"l_txt_{todo['id']}", label_visibility="collapsed")
                    with col2:
                        if st.button("💾 Save", key=f"l_sv_{todo['id']}"):
                            if updated_text:
                                self.db.update_todo(todo['id'], {'task': updated_text})
                                st.session_state[edit_key] = False
                                st.rerun()
                else:
                    col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
                    with col1:
                        st.write(f"• **[{todo['category']}]** {todo['task']}")
                    with col2:
                        if st.button("✏️", key=f"l_ed_{todo['id']}"):
                            st.session_state[edit_key] = True
                            st.rerun()
                    with col3:
                        if st.button("❌", key=f"l_dl_{todo['id']}"):
                            self.db.delete_todo(todo['id'])
                            st.rerun()
        else:
            st.write("No goals available for this criteria.")
