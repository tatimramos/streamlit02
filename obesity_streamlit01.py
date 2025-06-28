import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Estudo Obesidade",
                   page_icon=":bar_chart:",
                   layout="wide")

st.header("**Estudo Obesidade**")

@st.cache_data
def load_data():
    df = pd.read_csv("Obesity.csv")
    return df

df = load_data()

st.bar_chart(df.Age)
