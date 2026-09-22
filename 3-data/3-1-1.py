import streamlit as st # using streamlit to interact with the dataframe more like a spreadsheet (visually)
# streamlit also allows for easy csv downloads, basic statistics, and searching
import pandas as pd
import numpy as np

index = ['a', 'b', 'c', 'd']
s1_series = pd.Series(data=[1, 2, 3, 4], index=index)
s2_series = pd.Series(data=[2.2, np.nan, 3.0, 1.5], index=index)
s3_series = pd.Series(data=['q', 'q', 'z', 'z'], index=index,)
df = pd.DataFrame({'s1': s1_series, 's2': s2_series, 's3': s3_series}) 
# don't transpose (needed when building w/ series lists) it breaks dtype
st.dataframe(df)
st.dataframe(df.describe()) # displays a df with basic statistics
# only prints to the terminal, not the streamlit app
print(df.info())