import streamlit as st

name= st.text_input("Enter your name: ")
age= st.text_input("Enter your age: ")
father_name= st.text_input("Enter your father name: ")
mother_name= st.text_input("Enter your mother name: ")
address= st.text_area("Enter your address: ")
classroom= st.selectbox("Select your classroom",["Class 1", "Class 2", "Class 3"])