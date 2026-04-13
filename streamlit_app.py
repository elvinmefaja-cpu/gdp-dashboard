
Ira Murataj
11:01 AM (0 minutes ago)
to me

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Adult Dataset Dashboard")

# Load data
df = pd.read_csv("adult.csv", sep=",", skipinitialspace=True, on_bad_lines="skip")
df.columns = df.columns.str.strip()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Histogram
st.subheader("Age Distribution")
fig1 = px.histogram(df, x="age")
st.plotly_chart(fig1)

# Scatter
st.subheader("Age vs Working Hours")
fig2 = px.scatter(df, x="age", y="hours-per-week", color="income")
st.plotly_chart(fig2)

# Pie
st.subheader("Income Distribution")
fig3 = px.pie(df, names="income")
st.plotly_chart(fig3)
