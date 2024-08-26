import streamlit as st

st.markdown("# Conclusion")

st.write(
    """
The different models all resulted in an accuracy of about 72%. The best model we found was an XGBoost Classifier 
with an accuracy of 73% and an Area under the curve of 0.787. The addition of external data, such as holiday dates
 in France, did not improve the forecast accuracy.
"""
)

# st.write(
#     """
# This solution can potentially help reduce amount of high severity road accidents. Generally speaking, such analysis can be useful for different agencies and companies; e.g.:
# •	Roads and transportation authorities in towns/cities can benefit from such analysis to design and optimize traffic infrastructure for safety, e.g., improving road safety (speed limits, signage, number of lanes, safety lanes, emergency refuge areas, etc.), planning of new roads, scheduling of road maintenance, etc…
# •	Insurers can use such analysis for processes like risk assessments, pricing, claims handling for Motor insurance
# •	Car manufacturers can use such analysis to identify areas of improvement for car safety
# •	Industries and retail that heavily rely on effective supply chain can use such analysis to avoid substantial disruptions in supply chain
# •	Navigation system providers and autonomous vehicles manufacturers can use such analysis to deliver functionalities like planning trip routes and suggesting safer roads
# This all could potentially help save a lot of lives -millions of people sustain severe or fatal injuries each year- and ease heavy financial burdens on people and institutions.

# """
# )

# st.write(
#             """
# ● Our dataset degree of information was limited. It was impossible to identify which driver/car was at fault in the accident. 
# Also some of the dataset variables’ completion was imprecise (e.g. road width or presence of lights near the accident).
# \n \n
# ● Unlike recall, positive precision is not a monotone performance criterion. Positive precision is linked to positive 
# observations prevalence. We can therefore imagine that the calibration of our models depends exclusively on our dataset.
# \n \n
# ● It should be borne in mind that our model does not predict road accidents but rather the severity of an accident as a 
# function of certain factors. This means that we could estimate the degree of severity of an accident considering involved 
# features when the accident unfortunately already occurred, but we would not be sure that the case-study players’ decisions
# would have a direct impact on the proportion of severe accident.
#         """
#         )


# st.write(
#             """

# ● During pre-processing, when we selected our explanatory variables, one of the criteria was the variable’s completion rate. 
# If we had used a high-performance imputation method (e.g. multiple imputations), we could have saved the use of specific variables 
# but also increased the size of our dataset. 
# By evaluating the impact on the test dataset with/without imputation, we could have had an idea of the value of this lead.
#             """
#         )


# st.write(
#             """
# ● During data pre-processing, we could have improved our feature selection decision to keep only 70 features.
# We decided to keep the features most frequently ranked among last ones by XGBoost feature importance.
# One possible amelioration would have been to keep the mean rank of each feature when we pool XGBoost feature importance.
#             """
#         )


# st.write(
#             """
# ● We observed that some features had a much higher weight than others in poorly predicted accidents (e.g. village — yes/no). 
# This can be problematic, as the model can almost systematically predict an accident in the same way based on a feature, creating 
# a systematic prediction bias. One idea upstream would have been randomly transforming part of the feature’s values to reduce its 
# importance in the models and give more weight to the other features.
#         """
#         )
