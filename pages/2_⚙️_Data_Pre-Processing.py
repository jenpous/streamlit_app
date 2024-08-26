import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Pre-Processing", page_icon="⚙️")

df = pd.read_pickle('pickle_files/df_road_accidents.xz')

st.markdown("# Data Pre-Processing")
#st.sidebar.header("Data Exploration")
st.write(
    """
    In the feature engineering process, several key steps were taken to prepare 
    the data for modeling. Initially, standard preprocessing was performed, including 
    handling missing values, scaling numerical features, and encoding categorical variables. 
    The relationship between each feature and the target variable was then assessed through 
    correlation analysis to identify potential predictors.\n
    A sample random forest model was used to determine feature importance, leading to the 
    refinement of the feature set by dropping or grouping certain categories. To further validate 
    the categorical features, a Chi-Square test of independence and Cramer's V were applied to 
    measure the significance and strength of relationships between variables.\n
    Following the removal of irrelevant variables, one-hot encoding was applied to the categorical 
    variables across all four datasets to ensure compatibility with machine learning algorithms.\n
    This transformation maintained the integrity of categorical data and ensured consistency across datasets.
    The final step involved merging the four datasets at the accident level, resulting in a complete dataset 
    with 799,769 accidents. This dataset was then split into a training set (80%) and a test set (20%) to 
    support model development and evaluation.\n
    """
)

st.write('Dataset Shape: ', df.shape)

st.write('Final Dataset: ')
st.dataframe(df.head(5), use_container_width=True)

#st.dataframe(df.describe(), use_container_width=True)
#if st.checkbox("Show NA") :
#    st.dataframe(df.isna().sum())

