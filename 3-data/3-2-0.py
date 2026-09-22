import streamlit as st
import pandas as pd
import numpy as np

url="https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-header-blanks.csv"
# with many datasets read_csv works and can identify the headers if first record
# if delim is , it will work
# file name is helpful but sometimes the delim doesn't match (look at the actual contents)
df = pd.read_csv(url, skiprows=5)
# read_csv will read any delimited file
# if there is no header it will use the first record as header, you must specify header=None
# when header = None one should specify the column names using names= parameter
# this is diffiult due to the lack of metadata (you can guess but don't know what the file is actually saying)
# wo headers to skip empty skip_blank_lines=True or commented "#" comment="#"
# with headers lower than 0 use skiprows (number of rows) to skip to where header=0
st.dataframe(df)