import streamlit as st

st.set_page_config(page_title="Estudo Obesidade",
                   page_icon=":bar_chart:",
                   layout="wide")

st.header("**Estudo Obesidade**")

st.read_csv("Obesity.csv")

st.bar_chart(df.Age)
