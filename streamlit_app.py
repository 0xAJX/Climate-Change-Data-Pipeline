import re
from os import listdir
from os.path import isfile, join
import streamlit as st
import pandas as pd

st.header("Climate Change")
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

container1 = st.container()
container1.write("Average Temperature Based On Year For India")
container1.line_chart(df)

container2 = st.container()
container2.write("Sneak Peek to Data")
container2.write(udf)