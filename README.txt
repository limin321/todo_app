# 🚀 Supabase Productivity Todo App

A modular, object-oriented **Streamlit** dashboard integrated with **Supabase Auth and Database**. Features a rolling weekly checklist and a categorized lifetime aspiration system.

## ✨ Features
- **Secure Authentication:** Multi-user signup, login, and secure user data isolation via Supabase RLS policies.
- **Weekly Task Manager:** Automatically rolls over unfinished tasks to the current week every Sunday night. Keeps finished tasks safely archived as backups.
- **Categorized Lifetime Goals:** Bucket-list style tracking with customizable filters for categories like Study, Travelling, Food, and Fitness.
- **OOP Architecture:** Built with clean code separation into functional independent modules (`database.py`, `auth.py`, `weekly_tasks.py`, `lifetime_goals.py`).

## 📁 Repository Structure
```text
todo_app/
├── requirements.txt     # Production dependencies
├── README.md            # App documentation
├── .gitignore           # Keeps secrets out of GitHub
└── src/                 # Application source code
    ├── app.py           # Main Entrypoint Orchestrator
    ├── database.py      # Supabase CRUD service layer
    ├── auth.py          # User auth interface
    ├── weekly_tasks.py  # Weekly task component & rollover logic
    └── lifetime_goals.py# Lifetime categorized goals component
```

## 🛠️ Local Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone <your-repository-url>
   cd todo_app
   ```

2. **Set up a Python Virtual Environment:**
   ```bash
   python3 -m venv streamlit_venv
   source streamlit_venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Create a `.env` file in the root directory and populate it with your Supabase credentials:
   ```env
   SUPABASE_URL="your-supabase-project-url"
   SUPABASE_KEY="your-supabase-anon-key"
   ```

5. **Launch the application:**
   ```bash
   streamlit run src/app.py
   ```

## 🌐 Deploying to Streamlit Cloud

1. Push this codebase to your GitHub repository.
2. Connect your repository to [Streamlit Community Cloud](https://streamlit.io).
3. Set the **Main file path** to `src/app.py`.
4. Go to **Advanced settings -> Secrets** and paste your `.env` keys directly into the cloud configuration:
   ```toml
   SUPABASE_URL = "your-supabase-project-url"
   SUPABASE_KEY = "your-supabase-anon-key"
   ```

