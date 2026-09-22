import streamlit as st

st.title("Saying Hello!")
name = st.text_input("And you are?")
age = st.slider("How old are you?", min_value=18, max_value=65, value=(65+18)//2, step=1)

mybutton = st.button("Say Hello!", type="primary")

if mybutton: # when the button is clicked, display the following:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")

# python (run python) -m (run a module) streamlit run 2-ui/2-hello.py (run script path)
# ctrl + c (stop the server)
# localhost:18501