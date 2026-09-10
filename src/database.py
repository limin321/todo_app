import os
from supabase import create_client, Client

class SupabaseService:
    """Manages all direct communication with the Supabase API."""
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.client: Client = create_client(url, key)

    def sign_up(self, email, password):
        res = self.client.auth.sign_up({"email": email, "password": password})
        if hasattr(res, 'user') and res.user:
            return res.user
        return getattr(res, 'session', None) and res.session.user

    def sign_in(self, email, password):
        res = self.client.auth.sign_in_with_password({"email": email, "password": password})
        if hasattr(res, 'user') and res.user:
            return res.user
        elif hasattr(res, 'session') and res.session:
            return res.session.user
        return None

    def sign_out(self):
        self.client.auth.sign_out()

    def get_todos(self, user_id, todo_type, **filters):
        query = self.client.table('todos').select('*').eq('user_id', user_id).eq('type', todo_type)
        for key, value in filters.items():
            if key == "lt_week_start_date":
                query = query.lt('week_start_date', value)
            else:
                query = query.eq(key, value)
        return query.execute().data

    def add_todo(self, data):
        return self.client.table('todos').insert(data).execute()

    def delete_todo(self, todo_id):
        return self.client.table('todos').delete().eq('id', todo_id).execute()

    def update_todo(self, todo_id, updates):
        return self.client.table('todos').update(updates).eq('id', todo_id).execute()
