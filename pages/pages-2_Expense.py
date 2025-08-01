import streamlit as st
import plotly.express as px
from utils import load_data

st.title("🧾 Expense Breakdown")

df = load_data()
fig = px.pie(df, names="Expense Type", values="Amount", title="Expense Distribution")
st.plotly_chart(fig, use_container_width=True)
