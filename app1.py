import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Disaster Prediction",
                   layout="wide",
                   page_icon="🧑")

    
# getting the working directory of the main.py
# Use current working directory if __file__ is not available
working_dir = os.path.dirname(os.path.abspath(__file__))


# loading the saved models

Earthquake_model = pickle.load(open(f'{working_dir}/saved_models/rf (4).sav', 'rb'))

# Load the saved models
forest_model = pickle.load(open(f'{working_dir}/saved_models/forest (1).sav', 'rb'))

# Load the saved models
drought_model = pickle.load(open(f'{working_dir}/saved_models/droughtfile (2).sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Natural disaster Prediction',

                           ['Earthquake Prediction',
                            'Flood Prediction',
                            'Drought Prediction'],
                           menu_icon='Disaster',
                           icons=['Earth', 'water', 'rock'],
                           default_index=0)


if selected == 'Earthquake Prediction':

    # page title
    st.title('Earthquake Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        lattitude = st.text_input('lattitude')

    with col2:
        longitude = st.text_input('longitude')

    with col3:
        Depth = st.text_input('Depth')

    with col1:
        Noofstations = st.text_input('No of stations')

    


    # code for Prediction
    Earthquake_diagnosis = ''

    # creating a button for Prediction

    if st.button('Earthquake Result'):

        user_input = [lattitude, longitude, Depth, Noofstations]

        user_input = [float(x) for x in user_input]

        Earthquake_diagnosis= Earthquake_model.predict([user_input])

        if(Earthquake_diagnosis>3.0):
            print("No signs of Earthquake")
        else:
            print("Be alert!!! There's a possibility of Earthquake today")



        print('Earth_diagnosis')
        
        
        st.success(Earthquake_diagnosis)


if selected == 'Flood Prediction':
    # Page title
    st.title('Flood Prediction')

    col1, col2, col3 = st.columns(3)

    # Input fields for flood prediction
    with col1:
        MonsoonIntensity = st.text_input('Monsoon Intensity')
    with col2:
        TopographyDrainage = st.text_input('Topography Drainage')
    with col3:
        RiverManagement = st.text_input('River Management')
    with col1:
        Deforestation = st.text_input('Deforestation')
    with col2:
        ClimateChange = st.text_input('Climate Change')
    with col3:
        DamsQuality = st.text_input('Dams Quality')
    with col1:
        Siltation = st.text_input('Siltation')
    with col2:
        AgriculturePractice = st.text_input('Agriculture Practice')
    with col3:
        Encroachments = st.text_input('Encroachments')
    with col1:
        IneffectiveDisasterPreparedness = st.text_input('Ineffective Disaster Preparedness')
    with col2:
        DrainageSystem = st.text_input('Drainage System')
    with col3:
        CoastlVulnerability = st.text_input('Coastal Vulnerability')
    with col1:
        Landslides = st.text_input('Landslides')
    with col2:
        Watersheds = st.text_input('Watersheds')
    with col3:
        DetoratingInfrastructure = st.text_input('Deteriorating Infrastructure')
    with col1:
        PopulationScore = st.text_input('Population Score')
    with col2:
        Wetlandloss = st.text_input('Wetland Loss')
    with col3:
        InadequatePLanning = st.text_input('Inadequate Planning')
    with col1:
        PoliticalFactors = st.text_input('Political Factors')
    with col2:
        urbanisation = st.text_input('Urbanisation')

    # Prediction button
    if st.button('Flood probability Result'):
        try:
            # Collect and convert user input to float
            user_input = [
                MonsoonIntensity, TopographyDrainage, RiverManagement, Deforestation,
                ClimateChange, DamsQuality, Siltation, AgriculturePractice, Encroachments,
                IneffectiveDisasterPreparedness, DrainageSystem, CoastlVulnerability,
                Landslides, Watersheds, DetoratingInfrastructure, PopulationScore,
                Wetlandloss, InadequatePLanning, PoliticalFactors, urbanisation
            ]

            user_input = [float(x) for x in user_input]

            # Make prediction
            flood_prediction = forest_model.predict([user_input])
            flood_diagnosis = f"Flood prediction probability: {flood_prediction[0]}"
        except ValueError as ve:
            flood_diagnosis = f"Error: Please ensure all inputs are numerical values. {ve}"
        except Exception as e:
            flood_diagnosis = f"An error occurred during prediction: {e}"

        # Display the prediction result
        st.success(flood_diagnosis)



if selected == 'Drought Prediction':
    # Page title
    st.title('Drought Prediction')

    col1, col2, col3 = st.columns(3)

    # Input fields for flood prediction
    with col1:
        PS = st.text_input('PS')
    with col2:
        QV2M = st.text_input('QV2M')
    with col3:
        T2M = st.text_input('T2M')
    with col1:
        T2MDEW = st.text_input('T2MDEW')
    with col2:
        T2MWET = st.text_input('T2MWET')
    with col3:
        T2M_MAX = st.text_input('T2M_MAX')
    with col1:
        T2M_MIN = st.text_input('T2M_MIN')
    with col2:
        T2M_RANGE = st.text_input('T2M_RANGE')
    with col3:
        TS = st.text_input('TS')
    with col1:
        WS10M_RANGE = st.text_input('WS10M_RANGE')
    with col2:
        WS50M = st.text_input('WS50M')
    with col3:
        WS50M_MAX = st.text_input('WS50M_MAX')
    with col1:
        WS50M_RANGE = st.text_input('WS50M_RANGE')
    

    # Prediction button
    if st.button('Drought probability Result'):
        try:
            # Collect and convert user input to float
            user_input = [PS,QV2M,T2M,T2MDEW,T2MWET,T2M_MAX,
                         T2M_MIN,T2M_RANGE,TS,WS10M_RANGE
                        ,WS50M,WS50M_MAX,WS50M_RANGE]
               
            

            user_input = [float(x) for x in user_input]

            # Make prediction
            drought_prediction = drought_model.predict([user_input])
            drought_diagnosis = f"drought prediction probability: {drought_prediction[0]}"
        except ValueError as ve:
            drought_diagnosis = f"Error: Please ensure all inputs are numerical values. {ve}"
        except Exception as e:
            drought_diagnosis = f"An error occurred during prediction: {e}"

        # Display the prediction result
        st.success(drought_diagnosis)
