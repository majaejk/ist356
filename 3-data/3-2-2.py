import streamlit as st
import pandas as pd
import numpy as np
import requests

url="https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"
json_data = requests.get(url).json()
employees = pd.json_normalize(json_data, record_path="employees", meta=["dept"])
# the path that contains the records is "employees"
# "dept" is a path that is not under "employees" but it is metadata that should be included
# both "employees" and "dept" are at the top level in the json
# each meta path goes in a list that is within the list of meta paths
st.dataframe(employees)
st.write(json_data) # raw json data on streamlit is structued and interactive