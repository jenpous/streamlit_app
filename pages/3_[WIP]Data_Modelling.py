import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
import joblib
from streamlit_folium import st_folium
from sklearn.metrics import classification_report

# roc curve and auc
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

st.set_page_config(page_title="Data Modelling", page_icon="📈")

# df_ypred = pd.read_pickle('pickle_files/df_road_accidents_yhat_proba.xz')
# df_risk_zones = pd.read_pickle('pickle_files/risk_zones.xz')

# # Load the trained model from the compressed .xz file
# rf_ter_loaded = joblib.load('model_results/rfc_ternary_target/rfc_ternary_target.xz')
# rf_bin_loaded = joblib.load('model_results/rfc_binary_target/rfc_binary_target.xz')
# X_train_loaded_rf_t, X_test_loaded_rf_t, y_train_loaded_rf_t, y_test_loaded_rf_t = joblib.load('model_results/rfc_ternary_target/train_test_data_rfc_ternary.xz')
# X_train_loaded_rf_b, X_test_loaded_rf_b, y_train_loaded_rf_b, y_test_loaded_rf_b = joblib.load('model_results/rfc_binary_target/train_test_data_rfc_binary.xz')


st.markdown("# Data Modelling")
# #st.sidebar.header("Data Modelling")
st.write(
    """
    The objective is to work on a scoring of the risk zones according
    to the meteorological information, the geographical location.\n
    We evaluated the performance of each model by calculating performance metrics such as 
    accuracy (Accuracy) and F1-score (F1-score) on the training set and test set.\n
    Accuracy was used to measure the overall precision of the model. It measures the proportion of correctly 
    predicted instances (both true positives and true negatives) out of the total instances. 
    If the classes (severity levels) are balanced as it is the case in our data, accuracy can 
    give a good overall measure of the model's performance.\n
    Furthermore, the F1-score was taken into account. This metric is as well useful for binary 
    classification problems, as it takes into account both precision and recall to calculate an overall score.\n
    For the model’s performance, we also considered the Area under the ROC curve (Roc-AuC).\n
    We tried 5 models to predict the severity of the accidents.
    - Random Forest Classifier for a ternary target
    - Random Forest Classifier for a binary target
    - KMeans Cluster with n_cluster = 2
    - XGBoost with GridSearchCV for a binary target
    - Dense Neural Network for a binary target
    """
)


#  #model_results/rfc_ternary_target/train_test_data_rfc_ternary.xz
option = st.selectbox(
    "Please select a model",
    ("Random Forest - ternary target", "Random Forest - binary target", "KMeans Cluster", "XGBoost Classifier with Hyperparameter Tuning (grid search)", "XGBOOST OUR MODEL", "Dense Neural Network"))

  
# if option == "Random Forest - ternary target":
#     y_pred_rf_t = rf_ter_loaded.predict(X_test_loaded_rf_t)
#     st.dataframe(pd.crosstab(y_test_loaded_rf_t, y_pred_rf_t, rownames=['predicted → actual ↓'], colnames = ['predicted →']))
    
#     cr_dict=pd.DataFrame([])
#     cr_dict = classification_report(y_test_loaded_rf_t, y_pred_rf_t, output_dict=True)
#     cr_df = (round(pd.DataFrame.from_dict(cr_dict),2).T)
#     cr_df.support= cr_df.support.astype(int)
#     cr_df.loc['accuracy','precision'] = ''
#     cr_df.loc['accuracy','recall'] = ''
#     cr_df.loc['accuracy','support'] = cr_df.loc['macro avg','support']
#     pd.options.display.float_format = "{:,.2f}".format
#     pd.options.styler.format.thousands = ','
    
#     st.dataframe(cr_df)

# if option == "Random Forest - binary target":
#     model = rf_bin_loaded
    
#     # generate a no skill prediction (majority class)
#     ns_probs = [0 for _ in range(len(y_test_loaded_rf_b))]
#     # predict probabilities
#     lr_probs = model.predict_proba(X_test_loaded_rf_b)
#     # keep probabilities for the positive outcome only
#     lr_probs = lr_probs[:, 1]
#     # calculate scores
#     ns_auc = roc_auc_score(y_test_loaded_rf_b, ns_probs)
#     lr_auc = roc_auc_score(y_test_loaded_rf_b, lr_probs)
#     # summarize scores
#     st.write('No Skill: ROC AUC=%.3f' % (ns_auc))
#     st.write('Logistic: ROC AUC=%.3f' % (lr_auc))
    
#     # calculate roc curves
#     ns_fpr, ns_tpr, _ = roc_curve(y_test_loaded_rf_b, ns_probs)
#     lr_fpr, lr_tpr, _ = roc_curve(y_test_loaded_rf_b, lr_probs)
    
#     # plot the roc curve for the model
#     fig = plt.figure()
#     plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
#     plt.plot(lr_fpr, lr_tpr, marker='.', label='Logistic')
#     # axis labels
#     plt.xlabel('False Positive Rate')
#     plt.ylabel('True Positive Rate')
#     # show the legend
#     plt.legend()
#     # show the plot
#     plt.show()
#     st.pyplot(fig)

# if option == "KMeans Cluster":
#     st.write("KMeans")

# if option == "XGBoost Classifier with Hyperparameter Tuning (grid search)":
#     st.write("XGBoost 1") 


# if option == "Dense Neural Network":
#     st.write('Dense Neural Network')

# if option == "XGBOOST OUR MODEL":
    
#     # https://matplotlib.org/stable/gallery/color/named_colors.html
#     center_of_france = [46.71109, 1.7191036]

#     m = folium.Map(location=center_of_france, zoom_start=5, tiles=None)

#     # Manually adding the background map so it's always displayed when switching between different layers
#     folium.TileLayer('openstreetmap', name='Background Map (openstreetmap)', overlay=True).add_to(m)

#     for weather in df_risk_zones['condition'].unique():
#         fg = folium.FeatureGroup(name=weather.capitalize(), overlay=False)

#         # Filter df3 for the current weather condition
#         df_filtered = df_risk_zones[df_risk_zones['condition'] == weather]

#         for _, row in df_filtered.iterrows():
#             # Create a rectangle with the defined bounds
#             rectangle = folium.Rectangle(
#                 bounds=row['bounds'],
#                 color='#122B54',
#                 weight=0.2,
#                 #fill=False,
#                 #fill_color='#006192',
#                 fill_color='#006192',
#                 fill_opacity=row['yhat'],
#                 tooltip="<strong>ŷ = %.0f%%</strong>" % (row['yhat'] * 100)
#                 ).add_to(fg)

#         # Add the feature group to the map
#         fg.add_to(m)

#     # Add a LayerControl to switch between different weather conditions
#     folium.LayerControl(collapsed=True).add_to(m)

#     # Display the map with the rectangles in Streamlit
#     st.header("Road Accident Risk Map")

#     st.markdown('**Map of France divided into risk zones for road accident severity (higher % equals higher risk)**')
#     st_folium(m, width=700, height=500)