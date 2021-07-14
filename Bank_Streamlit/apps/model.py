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
    #st.write(df)
    # Model building
    st.header('Model performance')
    st.subheader('Making Prediction')
    st.markdown('**Please provide banker information**:')  # you can use markdown like this
    
    


    #inputs
    Married = st.radio("What is your Martial Status:",("Single",'Married','Divorced'))
    Age = st.slider('Age', min_value=18, max_value=100)
    Education = st.selectbox('What is your Education Level:',['Primary','Secondary','Tertiary','Unknown'])
    Job = st.selectbox('What is your Occupation:',["Admin.","Blue-collar","Entrepreneur","Housemaid","Management", "Retired","Self-employed","Services","Student","Technician","Unemployed","Unknown"])
    Month = st.selectbox('Month', ['January','February','March','April','May','June','July','August','September','October','November','December'])
    Duration = int(st.number_input("Enter Duration of call",00,1000,00))
    Default = st.radio("Did you default:",('Yes','No'))
    Loan = st.radio('Do you have a loan?', ('Yes','No'))
    Balance = int(st.number_input('Enter an amount'))
    Housing = st.radio("Do you have a house loan?",('Yes','No'))
    Contact = st.radio("How were you contacted",("Cellular",'Telephone','Unknown'))
    Day = int(st.number_input("Which day were you contacted on ",1,31,1))
    Campaign = int(st.number_input("How many times were you contacted",0,1000,00))
    pDays = int(st.number_input("pDays",-1,1000,00))
    Previous = int(st.number_input("previous",-1,1000,00))
    pOutcome = st.radio("What is the Poutcome",( "unknown","other","failure","success"))

    # this is how to dynamically change text
    prediction_state = st.markdown('calculating...')

    banker1 = pd.DataFrame(
        {   
            'age' : 64, 
            'job' : 'retired',
            'marital' : 'divorced',
            'education' : 'primary', 
            'default' : 'no', 
            'balance' : 109, 
            'housing' : 'no',
            'loan' : 'no',
            'contact' : 'cellular',
            'day' : 23, 
            'month' : 'jun', 
            'duration' : 706,
            'campaign' : 1,
            'pdays': 225, 
            'previous' : 2,
            'poutcome' : ['success']   
         
        }
    )
    

    banker2 = pd.DataFrame(
        {   
            'age' : [Age], 
            'job' : [Job],
            'marital' : [Married],
            'education' : [Education], 
            'default' : [Default], 
            'balance' : [Balance], 
            'housing' : [Housing],
            'loan' : [Loan],
            'contact' : [Contact],
            'day' : [Day], 
            'month' : [Month], 
            'duration' : [Duration],
            'campaign' : [Campaign],
            'pdays': [pDays], 
            'previous' : [Previous],
            'poutcome' : [pOutcome]        
         

        }
    )
    

    y_pred = saved_tree_clf.predict(banker2) 

    if y_pred[0] == 1:
        msg = 'This customer is predicted to be: **subscribed**'
        
    else:
        msg = 'This customer is predicted to be: **Not subscribed**'
       

    prediction_state.markdown(msg)
    
