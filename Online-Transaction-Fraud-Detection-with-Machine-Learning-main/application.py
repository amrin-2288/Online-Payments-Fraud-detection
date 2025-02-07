#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Creating Prediction application using Streamlit


# In[26]:


import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


# In[38]:


from joblib import load

model_file_path = r"C:\Users\akash\Desktop\ONLINEAPP\random_forest_model.joblib"
# Load the saved model
rf_model = load(model_file_path)


# In[63]:


import streamlit as st
import pandas as pd
import joblib
import base64

# Define a mapping for transaction types
type_mapping = {
    'Type 1': 1,
    'Type 2': 2,
    'Type 3': 3,
    'Type 4': 4
}

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1

# Function to make predictions based on input data
def predict_fraud(model, input_data):
    input_df = pd.DataFrame([input_data], columns=['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig'])
    prediction = model.predict(input_df)
    return prediction[0]

# Function to load background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.example.com/background.jpg");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Function to play celebration animation
def play_celebration_animation():
    st.markdown(
        """
        <style>
        @keyframes confetti-fall {
            0% {transform: translateY(0);}
            100% {transform: translateY(100vh);}
        }
        .confetti {
            position: fixed;
            width: 10px;
            height: 10px;
            background: #FF0;
            animation: confetti-fall 2s linear infinite;
        }
        </style>
        <div class="confetti"></div>
        """,
        unsafe_allow_html=True
    )

# Function to play bomb explosion animation
def play_bomb_animation():
    st.markdown(
        """
        <style>
        @keyframes bomb-blast {
            0% {transform: scale(1);}
            50% {transform: scale(1.5);}
            100% {transform: scale(1);}
        }
        .bomb {
            position: fixed;
            width: 100px;
            height: 100px;
            background: url('https://www.example.com/bomb.png') no-repeat center center;
            animation: bomb-blast 1s linear infinite;
        }
        </style>
        <div class="bomb"></div>
        """,
        unsafe_allow_html=True
    )

# Function to get user input for each step
def get_user_input_step1():
    st.title('Welcome to Online Fraud Predictor')
    st.markdown("### Get started by clicking 'Next'")
    if st.button('Next', key='next_step1'):
        st.session_state.step = 2
        st.experimental_rerun()

def get_user_input_step2():
    st.subheader('Select Transaction Type')
    type_ = st.selectbox('Transaction Type', list(type_mapping.keys()))
    st.session_state.type_ = type_
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Back', key='back_step2'):
            st.session_state.step = 1
            st.experimental_rerun()
    with col2:
        if st.button('Next', key='next_step2'):
            st.session_state.step = 3
            st.experimental_rerun()

def get_user_input_step3():
    st.subheader('Enter Transaction Amount ($)')
    amount = st.number_input('Amount', min_value=0.0)
    st.session_state.amount = amount
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Back', key='back_step3'):
            st.session_state.step = 2
            st.experimental_rerun()
    with col2:
        if st.button('Next', key='next_step3'):
            st.session_state.step = 4
            st.experimental_rerun()

def get_user_input_step4():
    st.subheader('Enter Old Balance ($)')
    oldbalanceOrg = st.number_input('Old Balance', min_value=0.0)
    st.session_state.oldbalanceOrg = oldbalanceOrg
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Back', key='back_step4'):
            st.session_state.step = 3
            st.experimental_rerun()
    with col2:
        if st.button('Next', key='next_step4'):
            st.session_state.step = 5
            st.experimental_rerun()

def get_user_input_step5():
    st.subheader('Enter New Balance ($)')
    newbalanceOrig = st.number_input('New Balance', min_value=0.0)
    st.session_state.newbalanceOrig = newbalanceOrig
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Back', key='back_step5'):
            st.session_state.step = 4
            st.experimental_rerun()
    with col2:
        if st.button('Next', key='next_step5'):
            st.session_state.step = 6
            st.experimental_rerun()

def show_prediction():
    st.subheader('Prediction Result')
    model_file_path = r"C:\Users\akash\Desktop\ONLINEAPP\random_forest_model.joblib"
    rf_model = joblib.load(model_file_path)
    input_data = {
        'type': type_mapping[st.session_state.type_],
        'amount': st.session_state.amount,
        'oldbalanceOrg': st.session_state.oldbalanceOrg,
        'newbalanceOrig': st.session_state.newbalanceOrig
    }
    prediction = predict_fraud(rf_model, input_data)
    if prediction == 1:
        play_bomb_animation()
        st.error('Fraudulent Transaction')
    else:
        play_celebration_animation()
        st.success('Non-Fraudulent Transaction')
    if st.button('Restart', key='restart'):
        st.session_state.step = 1
        st.experimental_rerun()

# Add background image
add_bg_from_url()

# Display the appropriate step based on the session state
if st.session_state.step == 1:
    get_user_input_step1()
elif st.session_state.step == 2:
    get_user_input_step2()
elif st.session_state.step == 3:
    get_user_input_step3()
elif st.session_state.step == 4:
    get_user_input_step4()
elif st.session_state.step == 5:
    get_user_input_step5()
elif st.session_state.step == 6:
    show_prediction()


# In[ ]:




