import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import folium
import joblib
from streamlit_folium import st_folium
from sklearn.metrics import classification_report

st.set_page_config(page_title="Risk Zones", page_icon="🚘")

st.markdown("# Risk Zones")
st.write(
    """
    Based on the predictive models developed, we have utilized an XGBoost model to classify various 
    risk zones across France, factoring in different weather and visibility conditions. The results 
    are displayed on an interactive map, allowing users to select specific weather and visibility 
    scenarios. The map dynamically highlights the corresponding risk zones in different colors, indicating 
    the predicted severity of road accidents. This visualization tool provides an intuitive way to assess 
    and understand the impact of environmental conditions on road safety, aiding in better decision-making 
    and preventive measures.\n
"""
)
st.markdown('**Map of France divided into risk zones for road accident severity (higher % equals higher risk)**')


df_risk_zones = pd.read_pickle('pickle_files/risk_zones.xz')
# https://matplotlib.org/stable/gallery/color/named_colors.html
center_of_france = [46.71109, 1.7191036]

m = folium.Map(location=center_of_france, zoom_start=5, tiles=None)

# Manually adding the background map so it's always displayed when switching between different layers
folium.TileLayer('openstreetmap', name='Background Map (openstreetmap)', overlay=True).add_to(m)

for weather in df_risk_zones['condition'].unique():
    fg = folium.FeatureGroup(name=weather.capitalize(), overlay=False)

    # Filter df3 for the current weather condition
    df_filtered = df_risk_zones[df_risk_zones['condition'] == weather]

    for _, row in df_filtered.iterrows():
        # Create a rectangle with the defined bounds
        rectangle = folium.Rectangle(
            bounds=row['bounds'],
            color='#122B54',
            weight=0.2,
            #fill=False,
            #fill_color='#006192',
            fill_color='#006192',
            fill_opacity=row['yhat'],
            tooltip="<strong>ŷ = %.0f%%</strong>" % (row['yhat'] * 100)
            ).add_to(fg)

    # Add the feature group to the map
    fg.add_to(m)

# Add a LayerControl to switch between different weather conditions
folium.LayerControl(collapsed=True).add_to(m)

# Display the map with the rectangles in Streamlit

st_folium(m, width=700, height=500)