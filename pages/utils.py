import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("data/finance_data.csv")
