import pandas as pd
import streamlit as st

# ---------- Page setup ----------
st.set_page_config(page_title="Room Makeover Planner", page_icon="🛋️")

# ---------- Data used by the app ----------
ROOMS = ["Bedroom", "Living Room", "Dorm Room", "Kitchen", "Home Office"]
SIZES = ["Small", "Medium", "Large"]
CATEGORIES = ["Furniture", "Lighting", "Decor", "Textiles", "Storage", "Other"]
PRIORITIES = ["Must-have", "Nice-to-have"]

STYLES = {
    "Minimalist": {
        "tip": "Keep surfaces clear, choose simple shapes, and stick to neutral tones.",
        "colors": ["#F5F5F5", "#BDBDBD", "#212121"],
    },
    "Cozy": {
        "tip": "Layer soft blankets and pillows, and use warm lamps instead of overhead light.",
        "colors": ["#D7B899", "#8B5E3C", "#F3E5D0"],
    },
    "Boho": {
        "tip": "Mix patterns and textures, add plants, and use woven or natural materials.",
        "colors": ["#C8A27A", "#6B8E6B", "#B5543C"],
    },
    "Modern": {
        "tip": "Use clean lines, one bold accent color, and statement lighting.",
        "colors": ["#FFFFFF", "#2F3E46", "#E07A5F"],
    },
    "Vintage": {
        "tip": "Look for secondhand wood pieces, framed art, and warm brass details.",
        "colors": ["#8C6A4F", "#D9C5A0", "#4F6D5A"],
    },
}

ROOM_ESSENTIALS = {
    "Bedroom": ["Bed frame and mattress", "Bedside lamp", "Storage for clothes"],
    "Living Room": ["Sofa or seating", "Coffee table", "Area rug"],
    "Dorm Room": ["Desk lamp", "Under-bed storage", "Wall decor that is easy to remove"],
    "Kitchen": ["Storage containers", "Good lighting", "Small appliance organizer"],
    "Home Office": ["Desk and chair", "Task lighting", "Cable management"],
}

SIZE_ADVICE = {
    "Small": "Choose multi-purpose furniture and use vertical storage to save floor space.",
    "Medium": "You have room for a few statement pieces, so balance them with open space.",
    "Large": "Use rugs and furniture groupings to divide the room into zones.",
}


# ---------- Helper functions ----------
def show_palette(colors):
    """Display color swatches side by side with their hex codes."""
    columns = st.columns(len(colors))
    for column, color in zip(columns, colors):
        column.markdown(
            f"<div style='background:{color};height:60px;border-radius:8px;"
            f"border:1px solid #ccc'></div>",
            unsafe_allow_html=True,
        )
        column.caption(color.upper())


def add_item(name, price, store, category, priority):
    """Save a new item to the shopping list stored in session state."""
    st.session_state["shopping_list"].append(
        {
            "Item": name,
            "Price": price,
            "Store": store,
            "Category": category,
            "Priority": priority,
            "Purchased": False,
        }
    )


# ---------- Session state (keeps the list while the app reruns) ----------
if "shopping_list" not in st.session_state:
    st.session_state["shopping_list"] = []

# ---------- Title and description ----------
st.title("Room Makeover Planner")
st.write(
    "Plan a room redesign in one place. Choose your room and style, set a budget, "
    "add the items you want to buy, and watch your total and progress update as you go."
)

# ---------- Section 1: Room and style ----------
st.header("1. Choose Your Room and Style")
col1, col2, col3 = st.columns(3)
room = col1.selectbox("Which room are you redecorating?", ROOMS)
style = col2.selectbox("Which style do you want?", list(STYLES))
size = col3.radio("Room size", SIZES, horizontal=True)

st.subheader(f"Your plan: {style} {room}")
st.info(f"**Style tip:** {STYLES[style]['tip']}")
st.write(f"**Space advice ({size.lower()} room):** {SIZE_ADVICE[size]}")
st.write("**Essentials to consider for this room:**")
for essential in ROOM_ESSENTIALS[room]:
    st.write(f"- {essential}")

# ---------- Section 2: Color palette ----------
st.header("2. Pick Your Color Palette")
st.caption("The colors start with a suggestion for your style. Change them to match your taste.")
picker_columns = st.columns(3)
chosen_colors = []
for i, column in enumerate(picker_columns):
    color = column.color_picker(
        f"Color {i + 1}",
        STYLES[style]["colors"][i],
        key=f"color_{style}_{i}",
    )
    chosen_colors.append(color)
show_palette(chosen_colors)

# ---------- Section 3: Budget ----------
st.header("3. Set Your Budget")
budget = st.number_input(
    "Total budget ($)", min_value=0.0, value=500.0, step=25.0, format="%.2f"
)

# ---------- Section 4: Shopping list ----------
st.header("4. Build Your Shopping List")
with st.form("add_item_form", clear_on_submit=True):
    f1, f2 = st.columns(2)
    name = f1.text_input("Item name", placeholder="e.g., Floor lamp")
    price = f2.number_input("Price ($)", min_value=0.0, step=5.0, format="%.2f")
    f3, f4, f5 = st.columns(3)
    store = f3.text_input("Store", placeholder="e.g., IKEA")
    category = f4.selectbox("Category", CATEGORIES)
    priority = f5.selectbox("Priority", PRIORITIES)
    submitted = st.form_submit_button("Add to list")

if submitted:
    if name.strip():
        add_item(name.strip(), price, store.strip() or "Not listed", category, priority)
        st.success(f"Added {name.strip()} to your list.")
    else:
        st.warning("Please enter an item name before adding.")

# ---------- Outputs that change with user input ----------
if st.session_state["shopping_list"]:
    st.subheader("Your Items")
    st.caption("Check the box when you have bought or set up an item.")

    for index, item in enumerate(st.session_state["shopping_list"]):
        item["Purchased"] = st.checkbox(
            f"{item['Item']} - ${item['Price']:.2f} ({item['Category']}, {item['Priority']})",
            value=item["Purchased"],
            key=f"purchased_{index}",
        )

    df = pd.DataFrame(st.session_state["shopping_list"])
    total_cost = df["Price"].sum()
    remaining = budget - total_cost
    done = int(df["Purchased"].sum())
    percent_done = done / len(df)

    st.header("5. Budget and Progress Summary")
    m1, m2, m3 = st.columns(3)
    m1.metric("Total planned cost", f"${total_cost:,.2f}")
    m2.metric("Budget remaining", f"${remaining:,.2f}")
    m3.metric("Items completed", f"{done} of {len(df)}")

    if budget > 0:
        st.progress(min(total_cost / budget, 1.0), text="Budget used")
    if remaining < 0:
        st.error(f"You are ${-remaining:,.2f} over budget. Consider removing a nice-to-have item.")
    else:
        st.success("You are within your budget.")

    st.progress(percent_done, text=f"Makeover progress: {percent_done:.0%}")

    st.subheader("Spending by Category")
    st.bar_chart(df.groupby("Category")["Price"].sum())

    st.subheader("Full Shopping List")
    st.dataframe(df, hide_index=True)

    if st.button("Clear all items"):
        for index in range(len(st.session_state["shopping_list"])):
            st.session_state.pop(f"purchased_{index}", None)
        st.session_state["shopping_list"] = []
        st.rerun()
else:
    st.info("Your list is empty. Add your first item above to see your budget summary.")