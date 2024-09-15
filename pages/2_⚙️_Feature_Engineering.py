import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Feature Engineering", page_icon="⚙️")
data_dir = 'attachements/feature_engineering/'
df = pd.read_pickle('model_results/df_road_accidents.xz')

st.markdown("# Feature Engineering")
#st.sidebar.header("Data Exploration")
st.write(
    """
    In the feature engineering process, several key steps were taken to prepare 
    the data for modeling. Initially, standard preprocessing was performed, including 
    handling missing values, scaling numerical features, and encoding categorical variables. 
    The relationship between each feature and the target variable was then assessed through 
    correlation analysis to identify potential predictors.\n
    **Feature Importance**\n
    A sample random forest model was used to determine feature importance, leading to the 
    refinement of the feature set by dropping or grouping certain categories. To further validate 
    the categorical features, a Chi-Square test of independence and Cramer's V were applied to 
    measure the significance and strength of relationships between variables.\n
    **Dummy Encoding**\n
    Following the removal of irrelevant variables, dummy encoding was applied to the categorical 
    variables across all four datasets to ensure compatibility with machine learning algorithms.\n
    **Target(s)**\n
    As for the target we decided to create 2 variants: a ternary target and a binary target.
    - Ternary Target (this lead to an unbalanced distribution of the ternary target)
    - Binary Target (This binary target is better balanced)\n
    
    **Cyclic Variables**\n
    Furthermore, cyclic variables such as the hour of the day, the day of the month, the month of the year, and even 
    latitude and longitude should be converted using a sine-cosine approach to make the machine learning 
    model aware that, for example, Monday is closer to Sunday than to Wednesday. 
    The time related features “minute of the day” and “month” in the characteristics-Tables for example 
    have been replaced using a sin/cos decoding to have nearby times and dates better represented for the models 
    to learn from them.
    """)
    
st.image(os.path.join(data_dir, 'time_sine_cosine_transformation.png'), use_column_width=True)
    

st.write(
    """
    **Statistical Analysis and Cleaning**\n
    After dummy encoding and aggregating on an accident basis, we did statistical tests regarding the correlation 
    of the features because some machine learning models suffer from correlated features, because they unnecessarily 
    lead to more complex models. The correlation in a DataFrame in Python can be shown using the corr-function in 
    conjunction with the Seaborn heatmap-plot. The values are showing the Pearson standard correlation coefficient, 
    measuring the strength and direction of the linear relationship between two variables. The correlations for the user table
    look as follows:
    """)
    
st.image(os.path.join(data_dir, 'corr_usr.png'), use_column_width=True)
    

st.write(
    """
    &nbsp;\n
    These transformations maintained the integrity of categorical data and ensured consistency across datasets.
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

