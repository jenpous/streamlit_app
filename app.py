import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#df=pd.read_csv("train.csv")
df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 45, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']})

st.title("Road Accidents : (binary) classification project")
st.sidebar.title("Table of contents")
pages=["Exploration", "Data Vizualization", "Modelling"]
page=st.sidebar.radio("Go to", pages)


if page == pages[0] : 
  st.write("### Presentation of data")
  st.dataframe(df.head(10))
  st.write(df.shape)
  st.dataframe(df.describe())

  if st.checkbox("Show NA") :
    st.dataframe(df.isna().sum())



if page == pages[1] : 
  st.write("### Data Vizualization")
  
  fig = plt.figure()
  sns.countplot(x = 'Name', data = df)
  st.pyplot(fig)

  gig = plt.figure()
  sns.countplot(x = 'Age', data = df)
  plt.title("Distribution of the passengers gender")
  st.pyplot(fig)
  
  fig = plt.figure()
  sns.countplot(x = 'Age', data = df)
  plt.title("Distribution of the passengers class")
  st.pyplot(fig)
  
  fig = sns.displot(x = 'Age', data = df)
  plt.title("Distribution of the passengers age")
  st.pyplot(fig)

  fig, ax = plt.subplots()
  sns.heatmap(df.corr(), ax=ax)
  st.write(fig)


if page == pages[2] : 
  st.write("### Modelling")


