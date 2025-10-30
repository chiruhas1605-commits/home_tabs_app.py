import streamlit as st

st.title("🍴 Teddy's Restaurant")

veg_items = ["Veg Mushroom", "Paneer Roll", "Veg Burrito"]
nonveg_items = ["Chicken Burrito", "Egg Roll", "Fish Fry"]

veg_choice = st.multiselect("🥦 Choose Veg Items", veg_items)
nonveg_choice = st.multiselect("🍗 Choose Non-Veg Items", nonveg_items)
rice = st.checkbox("🍚 Add Rice?")

if st.button("🧾 Create My Dish"):
    total_items = veg_choice + nonveg_choice
    if rice:
        total_items.append("Rice")
    if total_items:
        st.success(f"Your dish is ready! 🍽️ Items: {', '.join(total_items)}")
        st.balloons()
    else:
        st.warning("Please select at least one item!")
