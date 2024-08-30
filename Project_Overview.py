import streamlit as st

st.set_page_config(layout='wide')

st.markdown(
        "<h1 style='text-align: center; color: black;'>Road Accidents in France:</br> A Classification Project</h1>",
        unsafe_allow_html=True,
    )

col1, col2, col3 = st.columns([1, 3, 1])
with col1: 
    st.write(" ")

with col2:
    st.image("attachements/background.jpg", use_column_width=True, caption='Road accidents in France')

with col3:
    st.write(" ")

st.markdown(
        "<h4 style='text-align: center; color: black;'>Context</h4>",
        unsafe_allow_html=True,
    )

st.write("""
         The project aims at providing a Machine Learning-powered solution that helps predict the severity 
         of road accidents in France. Data about previous road accidents in France has been collected over 
         many years. This historical data can be used to train and test ML model(s) to spot and learn correlations 
         between different aspects about road accidents and their severity and location.
         Those models are then used to predict potential severity of road accidents based on their corresponding 
         characteristics. This helps to create risk zones with dynamic risk scores according to meteorological 
         information and geographical location among other information.
          """)

st.markdown(
        "<h4 style='text-align: center; color: black;'>Objective </h4>",
        unsafe_allow_html=True,
    )

st.write("""
        The objective of this project is to try to predict the severity of road accidents in France. 
          Therefore, we aim to design a classification model for predicting the severity of road 
          accidents in France. Predicting the severity of road accidents in France is a task related to 
          predictive analytics and risk assessment. This type of task involves analyzing historical data 
          and other relevant factors to predict future outcomes or the severity of incidents.
          """)

st.markdown(
        "<h4 style='text-align: center; color: black;'>Data </h4>",
        unsafe_allow_html=True,
    )
st.write(
        """
        The data on which our project is based derives from the Observatoire National Interministériel de la Sécurité 
        [National Cross-ministry Safety Observatory]. The databases, extracted from the BAAC 
        (([“Bulletins d’Analyse des Accidents Corporels de la circulation”]
        (https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/)). 
        Four tables were documented between 2005 and 2018 with different types of information:
        “characteristics”, “places”, “users”, “vehicles”.
    """
    )
st.divider()
st.info(
    """
    Allianz Cohort Data Scientist Sep 2023, DataScientest

    - Ahed Abdelky
    - Alessandro Perani
    - Falk Kegler
    - Jennifer Pousada
    """)
st.write(
    """
    Credits: The image has been generated using the Deep AI text to image generator at 
    https://deepai.org/machine-learning-model/text2img.
         """)



