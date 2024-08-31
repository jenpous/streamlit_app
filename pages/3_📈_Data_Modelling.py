import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Data Modelling", page_icon="📈")
data_dir = 'model_results/'


st.markdown("# Data Modelling")
st.write(
    """
    The objective is to work on a scoring of the risk zones according
    to meteorological information and geographical location.\n
    In total, 5 different models that were presented throughout the course 
    were created to predict the severity of the accidents.
    - Random Forest Classifier (for ternary target and binary target)
    - KNN Classifier (k = 3) for a binary target
    - XGBoost with GridSearchCV for a binary target
    - Dense Neural Network for a binary target\n
    The performance of each model was evaluated by calculating performance metrics such as 
    **Accuracy** and **F1-score** on the training set and test set.\n
    Accuracy was used to measure the overall precision of the model. It measures the proportion of correctly 
    predicted instances (both true positives and true negatives) out of the total instances. 
    If the classes (severity levels) are balanced as it is the case in our data, Accuracy can 
    give a good overall measure of the model's performance.\n
    Furthermore, the F1-score was taken into account. This metric is useful for binary 
    classification problems, as it takes into account both, precision and recall to calculate an overall score.
    For the model’s performance, the Area under the **ROC curve** (Roc-AuC) was also calculated.\n
    The XGBoost model achieved the highest performance with a ROC-AuC score of 0.793, indicating 
    its superior ability to balance sensitivity and specificity. The Densep Neural Network (DNN) followed 
    closely with a score of 0.787, demonstrating its effectiveness in capturing complex patterns within the 
    data. The Random Forest classifier also performed well, achieving a score of 0.780. However, the KNN algorithm, with a ROC-AuC score of 0.688, was less effective for this classification task. 
    Based on these results, XGBoost is identified as the most promising model for accurately predicting 
    accident severity, and further tuning of its hyperparameters is recommended to enhance its performance.\n
    """
)

cola, colb, colc = st.columns([1, 9, 1])
with colb: 
    st.image(os.path.join(data_dir, 'roc_auc_4_models.png'), use_column_width=True)

st.divider()

st.write(
    """
    **For more information, please select a model.**\n
    """
)
option = st.selectbox('## *Select a model*',
    ("Random Forest Classifier", 
     "KNN Classifier", "Dense Neural Network", "XGBoost Classifier"),
     label_visibility="collapsed")

  
if option == "Random Forest Classifier":
    st.write(
        """
        The first model were RandomForest Classifiers.
        We modelled with a ternary and a binary target for the severity of the accident. 
        We also examined the feature importance and visualized it with the help of the 
        SHAP-package for the binary-target model on an instance for target 0 and target 1 
        respectively.\n
        &nbsp;
        """
    )

    col1, col2 = st.columns([6, 6])
    with col1: 
        st.write('Random Forest Classifier with ternary target')
        st.image(os.path.join(data_dir, 'rfc_binary_target/rfc_ter.png'), use_column_width=True)
        st.write(
        """
        For the **ternary severity target**, we have created 3 bins [0,1,2], 
        derived from severity levels killed, hospitalized and lightly injured.\n
        """
        )

    with col2:
        st.write('Random Forest Classifier with binary target')
        st.image(os.path.join(data_dir, 'rfc_binary_target/rfc_bin.png'), use_column_width=True)
        st.write(
        """
        For the **binary severity target**, we have created 2 bins (people who have been 
        hospitalized/killed: 1 else 0).\n
        """
        )
    
    st.write(
    """
    As the Random Forest Classifier for the binary target demonstrates better performance in correctly predicting the target variable 
    with an Accuracy value of 0.72, it is selected for further analyses.\n
    """
    )

    col3, col4, col5 = st.columns([3, 6, 3])
    with col4: 
        st.write(
        """
        ROC Curve - RFC Binary Target\n
        """
        )
        st.image(os.path.join(data_dir, 'rfc_binary_target/roc_0780_rfc_binary_target.png'), use_column_width=True)
    st.write(
        """
        The ROC curve for the logistic regression model shows an **AuC of 0.78**, indicating a moderately 
        strong ability to distinguish between the positive and negative classes. This AuC value suggests that the model performs 
        significantly better than random guessing, as represented by the "No Skill" line. Overall, the model demonstrates 
        a good balance between sensitivity and specificity, making it a reliable tool for this classification task.
        """
    ) 
      
    st.write(
    """
    &nbsp;\n
    **Feature importance from Random Forest Classifier (Top 10)**\n
    """
    )
    col9, col10= st.columns([6, 6])
    with col9: 
        st.image(os.path.join(data_dir, 'rfc_binary_target/feature_importance_rfc_binary.png'), use_column_width=True)
    with col10:
        st.write(
        """
        The prefixes of the feature names are:\n
        - crc for characteristic-features
        - plc for place related features
        - usr for user related features
        - veh for vehicle related features
        """
        )
    
    st.write(
    """
    &nbsp;\n
    **Sin / Cos Transformation of time variable (hrmn)**\n
    The time related features “minute of the day” and “month” in the characteristics-Tables 
    have been replaced using a sin/cos decoding to have nearby times and dates better represented 
    for the models to learn from them:\n
    """
    )
    
    st.image(os.path.join(data_dir, 'rfc_binary_target/time_sine_cosine_transformation.png'), use_column_width=True)
    
    

    st.write(
    """
    &nbsp;\n
    **SHAP**\n
    For the Random Forest Classifier we used the SHAPly values to visualize the feature importance and to show how and 
    to what extent each feature contributed to the final prediction result. 2 instances were chosen, one with prediction 
    result 0 and another with prediction result 1.\n
    """
    )
    st.write('Shap-explainer (waterfall) for instance with prediction result 0:')
    st.image(os.path.join(data_dir, 'rfc_binary_target/shap_waterfall_rfc2.png'), use_column_width=True)

    st.write('Shap-explainer (waterfall) for instance with prediction result 1:')
    st.image(os.path.join(data_dir, 'rfc_binary_target/shap_waterfall_rfc2_2.png'), use_column_width=True)
    st.write(
    """
    The SHAP waterfall plots illustrate how different features contribute to the prediction for individual cases. 
    In the first plot, the prediction starts at a baseline value of 0.476, and factors like "veh_car" and 
    "plc_catr_Municipal Road" reduce the prediction, while "usr_route_Walk_Leisure" slightly increases it, 
    resulting in a final prediction of 0.23. In the second plot, the baseline is again 0.476, but here, 
    features like "crc_agg_Outside_urban_areas" and "crc_col_Two_vehicles_frontal" significantly increase 
    the prediction, leading to a final predicted value of 0.75. These plots reveal the specific contributions 
    of each feature to the final prediction, showing both positive and negative impacts.\n
    """
    )


if option == "KNN Classifier":
    st.write(
    """
    K-Nearest Neighbors (KNN) was utilized for predicting road accident severity due to its simplicity and 
    ability to capture complex, non-linear relationships in the data. The algorithm's flexibility in handling 
    diverse features and multiclass classification makes it well-suited for this task. \n
    """
    )
    col3, col4, col5 = st.columns([3, 6, 3])
    with col4: 
        st.write(
        """
        ROC Curve - KNN Binary Target\n
        """
        )
        st.image(os.path.join(data_dir, 'knn_binary_target/roc_0688_knn_binary_target.png'), use_column_width=True)
    
    st.write(
    """
    Due to the high computational intensity of this algorithm, we've limited the KNN to k = 3 neighbors and 
    reduced the test set to 10,000 records. This resulted in an **AuC of 0.688** which indicates that the model 
    has a moderate level of predictive ability. Specifically, this AUC value means that there is a 68.8% chance 
    that the model will correctly differentiate between a randomly chosen severe accident and a randomly chosen 
    non-severe accident. While the model shows some ability to distinguish between different levels of accident 
    severity, there is room for improvement in its performance.\n
    """
    )
    

if option == "XGBoost Classifier":
    st.write(
        """
        **XGBoost Classifier with Hyperparameter Tuning (grid search)**\n
        The XGBoost-Algorithm is famous for its high accuracy, especially on Kaggle. We tried to find the 
        best model with the help of a grid search cross-validation. Indeed, the model with the best estimators
        {'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 1000} 
        achieved the highest **accuracy of 73%** among all of the applied models and the highest value for the 
        **ROC-AuC of 0.793**.\n
        """
    ) 

    col1, col2, col3= st.columns([3, 6, 3])
    with col2:
        st.write(
        """
        XGB Classifier with Binary Target\n            
        """
        )
        st.image(os.path.join(data_dir, 'xgb_binary_target/xgb_accuracy.png'), use_column_width=True)
    

    col4, col5, col6 = st.columns([3, 6, 3])
    with col5: 
        st.write(
        """
        &nbsp;\n
        ROC Curve - XGB Binary Target\n
        """
        )
        st.image(os.path.join(data_dir, 'xgb_binary_target/roc_0793_xgb_binary_target.png'), use_column_width=True)
    st.write(
        """
        The ROC curve for the logistic regression model shows an **AuC of 0.793**, indicating a moderately 
        strong ability to distinguish between the positive and negative classes. This AuC value suggests that the model performs 
        significantly better than random guessing, as represented by the "No Skill" line. Overall, the model demonstrates 
        a good balance between sensitivity and specificity, making it a reliable tool for this classification task.
        """
    ) 
    
if option == "Dense Neural Network":
    st.write(
        """
        To practice what we have learned, we decided to try a deep learning model as well. 
        We chose to use a dense neural network with two hidden layers to leverage its capacity 
        for capturing complex patterns in the data. This architecture allows the model to learn 
        intricate relationships between features, which may be difficult for simpler models to 
        detect. Additionally, the two hidden layers provide sufficient depth for the network to 
        generalize well across diverse data points, improving overall predictive performance.\n
        """
    ) 
    col1, col2= st.columns([6, 6])
    with col1:
        st.write(
        """
        DNN with two hidden layers\n            
        """
        )
        st.image(os.path.join(data_dir, 'dnn_binary_target/dnn_two_hidden_layers.png'), use_column_width=True)
    with col2:
        st.write(
        """
        DNN with Binary Target\n            
        """
        )
        st.image(os.path.join(data_dir, 'dnn_binary_target/dnn_bin.png'), use_column_width=True)
    
    st.write(
        """
        The dense neural network with two hidden layers achieved an **accuracy of 71%** in predicting 
        the severity of accidents in France. This suggests that the model is reasonably effective 
        at distinguishing between different levels of accident severity, capturing key patterns and 
        interactions within the data. The use of two hidden layers likely helped the model to better 
        understand the complexities of accident-related factors, improving its predictive power. 
        However, while 71% accuracy indicates the model's utility, there is potential for further 
        optimization to enhance its performance in this critical application.\n
        """
    )
    

    col4, col5, col6 = st.columns([3, 6, 3])
    with col5: 
        st.write(
        """
        &nbsp;\n
        ROC Curve - DNN Binary Target\n
        """
        )
        st.image(os.path.join(data_dir, 'dnn_binary_target/roc_0787_DNN_binary_target.png'), use_column_width=True)
    st.write(
        """
        The ROC curve for the logistic regression model shows an **AuC of 0.787**, indicating a moderately 
        strong ability to distinguish between the positive and negative classes. This AuC value suggests that the model performs 
        significantly better than random guessing, as represented by the "No Skill" line. Overall, the model demonstrates 
        a good balance between sensitivity and specificity, making it a reliable tool for this classification task.
        """
    ) 