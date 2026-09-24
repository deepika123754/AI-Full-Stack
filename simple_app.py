import streamlit as st
st.title("Welcome to my first Streamlit App")
st.header("HELLO")
name=st.text_input("Enter your name...")
if st.button("Submit"):
    st.write(f"Hello, {name}!")