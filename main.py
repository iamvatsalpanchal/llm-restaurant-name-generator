import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Italian","Arabic", "Mexican","Indian","Americano"))

if cuisine:
    response = langchain_helper.get_cuisine(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-", item)
