import re
from os import listdir
from os.path import isfile, join
import streamlit as st
import pandas as pd

st.write("Climate Change")
working_directory = "ClimateChangeModified"
files = [f for f in listdir(working_directory) if isfile(join(working_directory, f))]

df = None

for f in files:
    if re.search(".csv$", f):
        df = pd.read_csv(working_directory + "/" + f, names=["Year", "Average Temperature"])

udf = df

if df is None:
    raise Exception("Issue with reading file")

df.set_index('Year', inplace=True)

col1, col2 = st.columns([10, 2])

col1.subheader("Average Temperature Based On Year For India")
st.line_chart(df)

col2.subheader("Sneak Peek to Data")
col2.write(udf)