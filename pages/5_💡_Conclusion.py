import streamlit as st

st.set_page_config(page_title="Conclusion")
st.markdown("# Conclusion")

st.write(
    """
    In this project, we utilized data from 2005 to 2018, as variables were redefined, and new variables were 
    introduced from 2019 onwards, for which no prior data existed. Furthermore, we opted to create a dataset 
    with one instance per accident. The original data was at the "person" level, so it was necessary to aggregate 
    this information into an accident-level dataset.\n
    
    The different models used all resulted in an accuracy of about 72%. The XGBoost model achieved the highest 
    performance with a ROC-AUC score of 0.793, indicating its superior ability to balance sensitivity and specificity.
    The Dense Neural Network (DNN) followed 
    closely with a score of 0.787, demonstrating its effectiveness in capturing complex patterns within the 
    data. The Random Forest classifier also performed well, achieving a score of 0.780. However, the KNN 
    algorithm, with a ROC-AUC score of 0.688, was less effective for this classification task. 
    Based on these results, XGBoost is identified as the most promising model for accurately predicting 
    accident severity, and further tuning of its hyperparameters is recommended to enhance its performance. 
    The addition of external data, such as holiday dates in France, did not improve the forecast accuracy.
    Interestingly, the results indicated that accident severity was lowest during light rain conditions.
"""
)
st.info(
    """
    One challenge we encountered was the large number of categories in the data, particularly for unsupervised 
    learning methods like K-Means, DBSCAN, and Optics, for which we lacked sufficient computing capacity. 
    Specifically, for the slack package, we did not have enough computational power to assess the influence of 
    features on the target at the model level; calculations were only feasible for individual instances.\n
    For practical implementation, such as deployment as an API, it may be necessary to select a model that 
    uses only the most significant features or employs a Principal Component Analysis (PCA) to ensure acceptable 
    performance. To maintain model accuracy, retraining would be required annually due to the observed yearly 
    decline in both the number of accidents and their severity in France. Additionally, before deploying the model, 
    further plausibility checks would be necessary; for instance, we excluded overseas territories and would need a 
    separate model for accidents occurring in regions like the Atlantic or Mediterranean.\n
    
    """
    )

st.write(
    """
    This solution can potentially help reduce amount of high severity road accidents. Generally speaking, such 
    analysis can be useful for different agencies and companies; e.g.:
    - Roads and transportation authorities in towns/cities can benefit from such analysis to design and optimize 
    traffic infrastructure for safety, e.g., improving road safety (speed limits, signage, number of lanes, safety 
    lanes, emergency refuge areas, etc.), planning of new roads, scheduling of road maintenance, etc…
    - Insurers can use such analysis for processes like risk assessments, pricing, claims handling for Motor 
    insurance
    - Car manufacturers can use such analysis to identify areas of improvement for car safety
    - Industries and retail that heavily rely on effective supply chain can use such analysis to avoid substantial 
    disruptions in supply chain
    - Navigation system providers and autonomous vehicles manufacturers can use such analysis to deliver functionalities 
    like planning trip routes and suggesting safer roads
    This all could potentially help save a lot of lives -millions of people sustain severe or fatal injuries each 
    year- and ease heavy financial burdens on people and institutions.
    
    At Allianz, understanding and analyzing frequency and severity of insurable risks are a big competitive 
    advantage. Creating classes or segments with different risk scores is a vital step in pricing insurance 
    products and reserving sufficient funds for future claims. Creating risk zones based on geography for example 
    is a vital part of pricing and reserving for NatCat insurance or insurance of similar risks (hazards). 
    At the same time, predicting severity of road accidents is one of the two main actuarial tasks that actuaries 
    try to model for Motor insurance. Predicting severity of road accidents using ML models and data shared about 
    the accident (claims data) is becoming more widely used, this could help to triage claims, automate some claims 
    handling steps, predict large claims common in the case of bodily injury or predict a total loss (i.e., 
    vehicle needs to be replaced).

"""
)

