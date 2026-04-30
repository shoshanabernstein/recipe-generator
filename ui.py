import streamlit as st
from database import get_food_restaurant, filter_foods, get_categories_by_restaurant

def sidebar():
    with st.sidebar:
        st.header("🔍Search")

        # Choose restaurant radio button
        chosen_restaurant = st.radio("Pick A Restaurant", get_food_restaurant())

        # Choose calorie button
        chosen_calories = st.slider("Calories", 0, 800, 300)

        # Choose categores dropdown
        chosen_category = st.selectbox("Category", get_categories_by_restaurant(chosen_restaurant))
        return chosen_restaurant, chosen_calories, chosen_category

def food_card(food):
    with st.expander(food['food_name']):
        with st.container(border=True):
            st.header(food['food_name'])

            col1, col2, col3 = st.columns(3)

            col1.metric("🍽️ Restaurant", food['food_restaurant'])
            col2.metric("🏷️ Category", food['food_category'])
            col3.metric("🔥 Calories", food['food_calories'])
            st.link_button("Nutrition Info", food['food_link'])
            st.image(food['food_logo'],)

def tab_card():
    tab1, tab2, tab3 = st.tabs(["Items", "Chart", "AI"])


    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


chosen_restaurant, chosen_calories, chosen_category = sidebar()
filtered_foods = filter_foods(chosen_restaurant, chosen_calories, chosen_category)[:50]

for food in filtered_foods:
    food_card(food)
tab_card()