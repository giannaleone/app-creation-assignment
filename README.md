# Room Makeover Planner

## Student Name
Your Name Here

## App Description
Room Makeover Planner is a Streamlit app that helps users plan a room redesign from start to finish. Users choose a room type, decor style, and room size and get style tips and room essentials in return. They set a budget, pick a color palette, and build a shopping list of furniture and decor items. As they add items and check them off, the app updates the total cost, the money remaining, a spending chart, and a progress bar showing how much of the makeover is done.

## Intended Users
This app is intended for college students, renters, and first-time homeowners who want to redecorate on a budget but feel overwhelmed by the process. It is also useful for anyone who wants one place to keep track of their ideas, costs, and progress.

## Current Features (Implemented)
- **Room and style selector:** choose a room, a style, and a room size, and get a style tip, space advice, and a list of essentials for that room
- **Color palette picker:** three color pickers that start with a suggested palette for the chosen style, displayed as swatches with hex codes
- **Budget input:** enter a total budget in dollars
- **Shopping list:** add items with a name, price, store, category, and priority
- **Budget summary:** total planned cost, budget remaining, a budget-used progress bar, and an over-budget warning
- **Progress tracker:** check off items as purchased and see a percent-complete bar
- **Spending by category chart** and a full shopping list table
- **Clear all items** button to start over

## Planned Features (Still To Do)
- Save room plans and shopping lists to a Supabase database so they are still there when the app is reopened
- Downloadable summary of the finished plan
- Edit and delete individual items from the list
- Before and after photo upload
- Simple 2D room layout planner to check whether furniture fits

## Running the App Locally
```
pip install -r requirements.txt
streamlit run app.py
```