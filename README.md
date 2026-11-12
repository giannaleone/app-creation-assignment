# Room Makeover Planner

## Student Name
Gianna Leone

## App Description
Room Makeover Planner is a Streamlit app that helps users plan and organize a room redesign from start to finish. Users will choose a room type and decor style, set a budget, and build a shopping list of furniture and decor items with prices. The app will track total spending against the budget, display a color palette for the room, and show how far along the makeover is as items are purchased or set up.

## Intended Users
This app is intended for college students, renters, and first-time homeowners who want to redecorate on a budget but feel overwhelmed by the process. It is also useful for anyone who wants one place to keep track of their ideas, costs, and progress.

## Planned Features
- **Room and style selector:** Users choose a room type (bedroom, living room, dorm, etc.), a style (minimalist, cozy, boho, modern), and a room size.
- **Budget tracker:** Users enter a total budget, and the app shows total spent, money remaining, and a warning if they go over budget.
- **Shopping list:** Users add items with a name, price, store, category, and priority (must-have or nice-to-have), and see them in a sortable table with a running total.
- **Color palette picker:** Users choose two to four colors and see them displayed side by side with their hex codes.
- **Progress tracker:** Users check off items as they are purchased or set up, and the app shows a percentage complete.
- **Downloadable summary:** Users can download a text file of their full plan.
- **Database storage:** Plans, budgets, and shopping list items will be saved in a SQLite database (using Streamlit's `st.connection` with SQL) so they are still there when the user returns.

## Database
This project uses [Supabase](https://supabase.com) (a hosted PostgreSQL database) to store room plans and shopping list items. The tables are defined in `schema.sql`. For Assignment 1 the app only creates the connection; later assignments will save and load data.

### Database Setup
1. Create a free project at supabase.com.
2. Open the SQL Editor and run the contents of `schema.sql`.
3. In Project Settings > API, copy the project URL and the anon public key.
4. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and paste in your URL and key.
5. Never commit `secrets.toml` (it is already in `.gitignore`).

## Running the App Locally
```
pip install -r requirements.txt
streamlit run app.py
```