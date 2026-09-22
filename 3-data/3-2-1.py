import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"
df=pd.read_csv(url, skiprows=3, sep=" ") # data has 3 commented rows, it is cols /s and rows /n

st.dataframe(df)