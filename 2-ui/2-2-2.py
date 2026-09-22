import streamlit as st

st.title("Order Tracker")

# initialize session state variables
if 'total' not in st.session_state:
    st.session_state.total = 0
    st.session_state.history = []

# inputs
new_amnt = st.number_input("Enter the order amount:")
total_button = st.button("Add to total", type='primary')
clear_button = st.button("Clear total")

# data processing; manipulation only
if total_button:
    st.session_state.history.append(new_amnt) # appends the new amount to the history list in the session state
    st.session_state.total += new_amnt # adds the new amount to the total in the session state
elif clear_button:
    st.session_state.total = 0 # sets the total to 0 in the session state
    st.session_state.history = [] # empties the history list in the session state

# data output of information from the session state
st.write(f"Total: {st.session_state.total}")
st.write(f"History: {st.session_state.history}")