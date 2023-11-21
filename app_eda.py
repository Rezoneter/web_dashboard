import streamlit as st
import pandas as pd

def run_eda_app():
    st.subheader('EDA screen')
    df = pd.read_csv('./data/iris.csv')
    st.dataframe(df)
    st.subheader('correlation coefficient')
    st.dataframe(df.corr(numeric_only=True))