import re
from os import listdir
from os.path import isfile, join
import streamlit as st
import pandas as pd
import altair as alt

st.header("Climate Change")
working_directory = "ClimateChangeModified"
files = [f for f in listdir(working_directory) if isfile(join(working_directory, f))]

india_df, cities_df, mumbai_df = None, None, None

for f in files:
    if re.search("IndiaTemperature.csv$", f):
        india_df = pd.read_csv(working_directory + "/" + f, names=["Year", "Average Temperature"])

# for f in files:
#     if re.search("india-cities-grouped.csv$", f):
#         cities_df = pd.read_csv(working_directory + "/" + f)

for f in files:
    if re.search("mumbai-temperature-1.csv$", f):
        mumbai_df = pd.read_csv(working_directory + "/" + f, names=["Date", "temp"])

if india_df is None and mumbai_df is None:
    raise Exception("Issue with reading file")

mumbai_df = mumbai_df[["Date", "temp"]]

india_df.set_index('Year', inplace=True)
# cities_df.set_index(['Date', "Average Temperature"], inplace=True)
mumbai_df.set_index('Date', inplace=True)

container1 = st.container()
container1.write("Average Temperature Based On Year For India")
container1.line_chart(india_df)

container2 = st.container()
container2.write("Sneak Peek to Data")
container2.write(india_df)

container3 = st.container()
container3.write("Recent Temperature in Mumbai")
container3.line_chart(mumbai_df)
#%%
# c = alt.Chart(mumbai_df).mark_circle().encode(
#     x='Date', y='temp', size='temp', color='temp')
#
# container3.altair_chart(c, use_container_width=True)
