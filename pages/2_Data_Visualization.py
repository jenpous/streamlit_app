import streamlit as st
import os

st.set_page_config(page_title="Data Visualization", page_icon="📈")


st.markdown("# Data Visualization")
#st.sidebar.header("Data Visualization")
st.write(
    """INSERT DESCRIPTION"""
)

tab1, tab2, tab3, tab4 = st.tabs(["Passengers", "Vehicles", "Characteristics", "Places"])

with tab1:
    #st.subheader("A cat")
    data_dir = 'attachements/passengers/'
    attachements = os.listdir(data_dir)
    
    for filename in attachements:
        st.image(os.path.join(data_dir, filename))

with tab2:
    data_dir = 'attachements/vehicles/'
    attachements = os.listdir(data_dir)
    
    for filename in attachements:
        st.image(os.path.join(data_dir, filename))

with tab3:
    data_dir = 'attachements/characteristics/'
    attachements = os.listdir(data_dir)
    
    for filename in attachements:
        st.image(os.path.join(data_dir, filename))

with tab4:
    data_dir = 'attachements/places/'
    attachements = os.listdir(data_dir)
    
    for filename in attachements:
        st.image(os.path.join(data_dir, filename))