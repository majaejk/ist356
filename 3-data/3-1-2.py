import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
customers = pd.read_csv(url, header=0)
# use the first row as the header, don't use the first column as the index
# st.dataframe(customers)
customers_ny = customers[customers['State'] == 'NY']
# when filtering always use a new variable to hold the dataframe
# st.dataframe(customers_ny)
customers_ny_info = customers_ny[['First', 'Last', 'Gender', 'State', 'Total Purchased']]
# state shows what we filtered on so we need to keep it,
# it is not needed for analysis but it is important context 
# also show any values that you derive a new number from
# column filtering is for display, never get rid of columns even after parsing
st.dataframe(customers_ny_info)
# print(customers.info())