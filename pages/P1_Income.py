import streamlit as st
import plotly.express as px
from utils import load_data

st.title("💰 Income Overview")

df = load_data()
fig = px.line(df, x="Date", y="Income", title="Income Over Time")
st.plotly_chart(fig, use_container_width=True)
