import re
from os import listdir
from os.path import isfile, join
import streamlit as st
import pandas as pd

st.header("Climate Change")
working_directory = "ClimateChangeModified"
files = [f for f in listdir(working_directory) if isfile(join(working_directory, f))]

india_df, cities_df = None, None

for f in files:
    if re.search("IndiaTemperature.csv$", f):
        india_df = pd.read_csv(working_directory + "/" + f, names=["Year", "Average Temperature"])

for f in files:
    if re.search("india-cities-grouped.csv$", f):
        cities_df = pd.read_csv(working_directory + "/" + f)

if india_df is None and cities_df is None:
    raise Exception("Issue with reading file")

cities_df = pd.DataFrame(cities_df, columns = ["City", "Date", "Average Temperature"])

india_df.set_index('Year', inplace=True)
# cities_df.set_index(['Date', "Average Temperature"], inplace=True)


container1 = st.container()
container1.write("Average Temperature Based On Year For India")
container1.line_chart(india_df)

container2 = st.container()
container2.write("Sneak Peek to Data")
container2.write(india_df)