import streamlit as st
# print number of lines in the text file
# sum of each line in the text file
# no session state variables
st.title("Order proccessor")

total = 0.0
orders = 0

# inputs
file = st.file_uploader("Upload a text file", type=["txt"]) 
calculate_button = st.button("Calculate")

# proccessing
if file is not None and calculate_button:
    for line in file:
        orders += 1
        amount = float(line.strip())
        total += amount


# outputs
st.write(f"There are {orders} orders in the file.")
st.write(f"The total of all orders in the file is ${total}.")