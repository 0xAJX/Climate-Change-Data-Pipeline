import re
from os import listdir
from os.path import isfile, join
import numpy as np
import streamlit as st
import pandas as pd
import datetime

st.write("Average Temperature Based On Year For India")
working_directory = "ClimateChangeModified"
files = [f for f in listdir(working_directory) if isfile(join(working_directory, f))]

df = None

for f in files:
    if re.search(".csv$", f):
        df = pd.read_csv(working_directory + "/" + f, names=["year", "averagetemperature"])

if df is None:
    raise Exception("Issue with reading file")

df.set_index('year', inplace=True)
st.line_chart(df)