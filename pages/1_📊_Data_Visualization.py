import streamlit as st
import os

st.set_page_config(page_title="Data Visualization", page_icon="📊")


st.markdown("# Data Visualization")
#st.sidebar.header("Data Visualization")
st.write(
    """Understanding the factors contributing to road accidents is crucial for enhancing road safety 
    and reducing accident severity. In this section, we dive into the data through interactive visualizations 
    that help uncover patterns, trends, and correlations. By exploring key variables such as weather conditions, 
    time of day, and traffic density, we aim to gain insights into the circumstances under which severe accidents 
    are more likely to occur.
    """
)

st.write(
    """
    To provide a structured and comprehensive analysis, we have organized the visualizations into four tabs, each 
    corresponding to a specific dataset:

    - **Passengers**: Explore data related to the individuals involved in accidents.
    - **Vehicles**: Analyze the characteristics and conditions of vehicles involved.
    - **Characteristics**: Examine the details surrounding the accidents, such as time, location, and environmental factors.
    - **Places**: Investigate the geographical distribution and features of accident locations.

    These visualizations serve as a foundation for building predictive models that can anticipate accident severity, 
    enabling proactive measures for improving road safety in France."""
)

tab1, tab2, tab3, tab4 = st.tabs(["Passengers", "Vehicles", "Characteristics", "Places"])

with tab1:
    data_dir = 'attachements/passengers/'
    attachements = os.listdir(data_dir)
    
    
    col1, col2 = st.columns([6, 6])
    with col1: 
        st.write('Distribution of Gender')
        st.image(os.path.join(data_dir, 'gender_dist.png'), use_column_width=True)

    with col2:
        st.write('Distribution of User Category')
        st.image(os.path.join(data_dir, 'severity_dist.png'), use_column_width=True)
    
    st.write(
        """ 
        From the visuals, we can observe that Males are involved in road accidents at a significantly higher 
        rate than Females, representing a majority of the cases. This disparity may reflect differences in driving 
        habits, exposure, or risk-taking behaviors between genders. \n
        Most individuals involved in road accidents are either Unharmed or Lightly Injured, indicating that many 
        accidents result in minor or no injuries. However, a notable portion is Hospitalized, and a small yet significant 
        percentage are Killed, underlining the critical need for safety measures.\n
        """
    )

    col3, col4 = st.columns([6, 6])
    with col3:
        st.write('Distribution of Gender and Accident Severity')
        st.image(os.path.join(data_dir, 'gender_sev_dist.png'), use_column_width=True)

    with col4:
        st.write('Distribution of Severity')
        st.image(os.path.join(data_dir, 'user_dist.png'), use_column_width=True)

    st.write(
        """ 
        Analyzing the Gender among the Accident Severity shows again that a higher number of accidents involving male passengers
        in comparison to female passengers. Also, the accident severity for male passengers is slightly higher.\n
        The majority of those involved in road accidents are Drivers, comprising over 70% of the total, followed by Passengers.
        Pedestrians and Roller Skaters are involved much less frequently, with roller skaters being nearly negligible.\n
        """
    )

    col5, col6 = st.columns([11, 1])
    with col5:
        st.write('Distribution of Passenger Age')
        st.image(os.path.join(data_dir, 'age_dist.png'), use_column_width=True)

    st.write(
        """ 
        We have binned passenger's ages into 5 bins: 
        - 1: age 0-18
        - 2: age 19-53
        - 3: age 54-59
        - 4: age 60-69
        - 5: age 70-999\n
        Analyzing the age distribution of passengers involved in a car accident shows, that people from age 19-53 are mostly
         involved in accidents. \n
        """
    )


with tab2:
    data_dir = 'attachements/vehicles/'
    attachements = os.listdir(data_dir)

    st.write('Distribution of Vehicle Category')
    st.image(os.path.join(data_dir, 'vehicle_cat_dist.png'), use_column_width=True)
    
    st.write(
        """ 
        Based on the provided categories for the variable catv, we create groups. 
        This grouping is based on the similarity of vehicle types and their usage.
        The results depict the distribution of transportation modes: cars dominate at 
        approximately 71%, followed by motorcycles at 25%, with specialized modes 
        making up a smaller proportion at 2%. Public transport represents a minimal 
        fraction, accounting for only about 0.3% of the total.\n
        """
    )

    col1, col2 = st.columns([3, 9])
    with col1:
        st.write('Nr. of Involved Vehicles')
        st.image(os.path.join(data_dir, 'involved_veh.png'), use_column_width=True)           
    
    with col2:
        st.write('Distribution of Obstacle hit')
        st.image(os.path.join(data_dir, 'obst_dist.png'), use_column_width=True)
        
    st.write(
        """ 
        It can be seen that in most of the accidents 2 vehicles were involved, whereas 
        still in a considerable number of accidents only one car was involved.\n

        Furthermore, it can be observed that the majority of accidents involve a vehicle hitting 
        another moving vehicle which is in line with the previous graph 
        where the highest share of accidents involve 2 vehicles.\n
        """
    )

    st.write('Number of Accidents by Severity and Main Maneuver Before Accident')
    st.image(os.path.join(data_dir, 'manv_severity.png'), use_column_width=True)
    
    st.write(
        """ 
        The characteristics of the variable main maneuver have been grouped into 5 categories. 
        The highest level of severity accounts for most of the accidents without change of direction.\n
        """
    )   

with tab3:
    data_dir = 'attachements/characteristics/'
    attachements = os.listdir(data_dir)
    
    st.write('Distribution of Number of Accidents per Year')
    st.image(os.path.join(data_dir, 'acc_per_yr.png'), use_column_width=True)
    
    st.write(
        """ 
        It can be observed a decrease of accidents in period between year 2005 and 2012. 
        It can also see the effect of lockdown during the COVID pandemic in 2020 
        with a considerably lower number of accidents that can maybe be attributed 
        to the reduction of car usage during that period.\n
        """
    )

    st.write('Distribution of Number and Severity of Accidents per Location')

    col1, col2 = st.columns([6, 6])
    with col1:
        st.image(os.path.join(data_dir, 'acc_per_loc1.png'), use_column_width=True)     
    
    with col2:
        st.image(os.path.join(data_dir, 'acc_per_loc2.png'), use_column_width=True) 

    st.write(
        """ 
        The decrease in the number of accidents in period 2005-2012 looks to be 
        especially observed in built-up areas (in comparison to areas out of agglomeration).\n
        However, accidents in areas out of agglomeration lead to a higher incidences of 
        death in comparison to built-up areas. For this reason the decrease in the number of 
        accidents observed from 2005 to 2012 might not necessarily lead to a proportional decrease of deaths\n
        """
    ) 

    st.write('Distribution of Number of Accidents per Day and Hour')
    st.image(os.path.join(data_dir, 'acc_per_day_hour.png'), use_column_width=True)
    
    st.write(
        """ 
        It can be observed that the accidents are concentrated in peak hours of the day. 
        From 10 pm to 6 am, the highest proportions of death and hospitalized cases occur, 
        with a peak reached at 3 to 5 am. This suggests that brightness and activity 
        (reason for taking the car) may indirectly impact accident severity and time of day 
        A higher number of accidents during the night is observed on Saturday and Sunday.\n
        """
    )


    st.write('Distribution of Number of Accidents by Light Condition')
    st.image(os.path.join(data_dir, 'light_dist.png'), use_column_width=True)     
    st.write(
        """ 
        It can be observed that most accidents occur during the day.\n
        """
    )

    st.write('Distribution of Number and Severity of Accidents per Location')
    st.image(os.path.join(data_dir, 'weather_dist.png'), use_column_width=True) 
    st.write(
        """ 
        It can be observed that most accidents are happen under normal weather conditions
        followed by light rain.\n
        """
    )

with tab4:
    data_dir = 'attachements/places/'
    attachements = os.listdir(data_dir)
    
    st.write('Distribution of Accidents per Region')
    st.image(os.path.join(data_dir, 'region_dist.png'), use_column_width=True) 
    st.write(
        """ 
        Looking at the graph, it can be seen that the highest number of accidents 
        are in the region Ile-de-France. This is to be expected as population density 
        in this region is the highest in France. However, taking the accident severity 
        into consideration, it can be observed that it is quite low for this region.\n
        """
    )

    st.write('Distribution of Accidents by Longitude and Latitude')
    st.image(os.path.join(data_dir, 'long_lat_dist.png'), use_column_width=True) 
    st.write(
        """ 
        Latitude and longitude coordinates enable us to observe how accidents occurred 
        in in-built areas are more often with lower severity. High severity claims occur 
        outside the cities. The map confirms the results coming from the analysis per Region.
        Even though most accidents are concentrated in the Paris area, most of them are 
        low-severity accidents.\n
        """
    )
