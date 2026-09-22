import streamlit as st

st.title("Area calculator")

width = st.number_input("Width or Base", step=0.1 )
height = st.number_input("Height", step=0.1)

option = st.selectbox("Choose a shape", ["Rectangle", "Triangle", "Trapezoid"], index=None)
calculate_button = st.button("Calculate Area")

if calculate_button:
    if option == "Rectangle":
        area = width * height
        st.write(f"The area of the rectangle is: {area}")
    if option == "Triangle":
        area = 0.5 * width * height
        st.write(f"The area of the triangle is: {area}")
    if option is None:
        st.error("Please select a shape to calculate the area.")
