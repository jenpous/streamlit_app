import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Exploration", page_icon="📈")

df =  pd.read_pickle('pickle_files/df_road_accidents.xz')

st.markdown("# Data Exploration")
#st.sidebar.header("Data Exploration")
st.write(
    """INSERT DESCRIPTION"""
)

st.dataframe(df.head(10), use_container_width=True)
st.write(df.shape)
st.dataframe(df.describe(), use_container_width=True)
if st.checkbox("Show NA") :
    st.dataframe(df.isna().sum())

