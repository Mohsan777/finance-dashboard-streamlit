import streamlit as st
from utils import load_data

st.set_page_config(page_title="Finance Dashboard", layout="wide")
st.title("📊 Finance Dashboard")
st.markdown("Welcome to my interactive finance dashboard built with Streamlit!")

data = load_data()

st.subheader("Overview")
st.dataframe(data.head())
