# Welcome to the **to-to-list-tracking-app**
You can access [here](https://to-do-list-tracking-app.streamlit.app/)


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
   # create requirements.txt -- need to be in the virtual env, and in the app root project.
   pip freeze > requirements.txt
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
1. Backend Database Setup (Supabase)
   Action: I provisioned a cloud database on Supabase.
   Database & SQL: I used SQL commands to structure tables (setting up fields for users, tasks, and completion statuses) and configured the foundational backend infrastructure.
2. Full-Stack Development (Local Python)  -- Test locally before deploy to cloud -- refer the above README section.
   Action: wrote the application logic locally in Python utilizing Streamlit.
   Integration: You integrated your Python codebase with Supabase to handle user authentication (login/signup) and dynamic database interactions (fetching and saving todo items).
3. Version Control & Synchronization (Git & GitHub)
   1) initialized the app folder as a local Git repository to track project files.
   2) Then created an empty repository on GitHub, linked it to the local git as the remote origin, merged the baseline LICENSE history, and successfully pushed your codebase online.
4. Cloud Deployment (Streamlit Community Cloud) - login Streamlit using GitHub account.
   1) Connect git repo to [Streamlit Community Cloud](https://streamlit.io).
   2) Create New App: Set the **Main file path** to `src/app.py`.
   3) Go to **Advanced settings -> Secrets** and paste `.env` keys directly into the cloud configuration:
      ```toml
      SUPABASE_URL = "your-supabase-project-url"
      SUPABASE_KEY = "your-supabase-anon-key"
      ```
      Save and deploy. Make sure to use python 3.11 or 3.12. The 3.14 will fail to build the app.
