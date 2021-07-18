import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


# load models
saved_tree_clf = joblib.load('clf-best.pickle')

    
def app():
    st.title('Model')

    st.write('This is the Model page')

    st.write('The model performance of the Bank Model dataset is presented below.')

    # Load dataset
    df = pd.read_csv('projectdataset-1.csv')

    # Model building
    st.header('Model Performance')
    st.subheader('Making Prediction')
    st.markdown('**Please Provide Information**:')        


    #inputs
    Duration = int(st.number_input("Enter Duration of call",00,1000,00))
    Default = st.radio("Did you default:",('Yes','No'))
    Loan = st.radio('Do you have a loan?', ('Yes','No'))
    pDays = int(st.number_input("pDays",-1,1000,00))
    Housing = st.radio("Do you have a house loan?",('Yes','No'))
    Age = st.slider('Age', min_value=18, max_value=100)
    Balance = int(st.number_input('What is your yearly average balance?'))
    Contact = st.radio("How were you contacted",("Cellular",'Telephone','Unknown'))
    Job = st.selectbox('What is your Occupation:',["Admin.","Blue-collar","Entrepreneur","Housemaid","Management", "Retired","Self-employed","Services","Student","Technician","Unemployed","Unknown"])
    Education = st.selectbox('What is your Education Level:',['Primary','Secondary','Tertiary','Unknown'])

    # Married = st.radio("What is your Martial Status:",("Single",'Married','Divorced'))
    # Month = st.selectbox('Month', ['January','February','March','April','May','June','July','August','September','October','November','December'])
    # Day = int(st.number_input("Which day were you contacted on ",1,31,1))
    # Campaign = int(st.number_input("How many times were you contacted",0,1000,00))
    # Previous = int(st.number_input("previous",-1,1000,00))
    # pOutcome = st.radio("What is the Poutcome",( "unknown","other","failure","success"))


    # this is how to dynamically change text
    prediction_state = st.markdown('calculating...')

    banker1 = pd.DataFrame(
        {   
            'duration' : 706,
            'default' : 'no', 
            'loan' : 'no',
            'pdays': 225, 
            'housing' : 'no',
            'age' : 64, 
            'balance' : 109, 
            'contact' : 'cellular',
            'job' : 'retired',
            'education' : 'primary' 

            # 'marital' : 'divorced',
            # 'day' : 23, 
            # 'month' : 'jun', 
            # 'campaign' : 1,
            # 'previous' : 2,
            # 'poutcome' : ['success']   
         
        }
    )
    

    banker2 = pd.DataFrame(
        {   
            'duration' : [Duration],
            'default' : [Default], 
            'loan' : [Loan],
            'pdays': [pDays], 
            'housing' : [Housing]
            'age' : [Age], 
            'balance' : [Balance], 
            'contact' : [Contact],
            'job' : [Job],
            'education' : [Education] 
        }
    )
    

    y_pred = saved_tree_clf.predict(banker2) 

    if y_pred[0] == 1:
        msg = 'This customer is predicted to be: **subscribed**'
        
    else:
        msg = 'This customer is predicted to be: **Not subscribed**'
       

    prediction_state.markdown(msg)
    
