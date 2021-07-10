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


    
banker1 = pd.DataFrame(
    {   'age' : 33, 
        'job' : 'self-employed',
        'marital' : 'married',
        'education' : 'secondary', 
        'default' : 'no', 
        'balance' : 0, 
        'housing' : 'no',
        'loan' : 'no',
        'contact' : 'cellular',
        'day' : 18, 
        'month' : 'aug', 
        'duration' : 73,
        'campaign' : 7,
        'pdays': -1, 
        'previous' : 0,
        'poutcome' : ['success']       
     
     
    })



# this is how to dynamically change text
#prediction_state = st.markdown('calculating...')
#saved_tree_clf.predict(banker1)




def app():
    st.title('Model')

    st.write('This is the Model page')

    st.write('The model performance of the Bank Model dataset is presented below.')

    # Load dataset
    df = pd.read_csv('projectdataset-1.csv')
    st.write(df)
    # Model building
    st.header('Model performance')
    st.subheader('Making Prediction')
    st.markdown('**Please provide banker information**:')  # you can use markdown like this
    
    
    # Read input 
        '''
    age = int(st.number_input('Age:', 0, 120, 20))
    sex = st.selectbox('Sex', ['female', 'male'])
    sib_sp = int(st.number_input('# of siblings / spouses aboard:', 0, 10, 0))
    #par_ch = int(st.number_input('# of parents / children aboard:', 0, 10, 0))
    pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
    fare = int(st.number_input('# of parents / children aboard:', 0, 100, 0))
    #embarked = st.selectbox('Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)', ['C', 'Q', 'S'])

    # this is how to dynamically change text
    prediction_state = st.markdown('calculating...')



    st.title('Banking Decision')
    # load dataset
    df = pd.read_csv('projectdataset-1.csv')
    Married = st.radio("What is your Martial Status:",
        ("Single",'Married','Divorced'))
    Education = st.selectbox('What is your Education Level:',
        ["Select",'Primary','Secondary','Tertiary','Unknown'])
    Job = st.selectbox('What is your Occupation:',
        ["Select","Admin.","Blue-collar","Entrepreneur","Housemaid","Management", "Retired",
        "Self-employed","Services","Student","Technician","Unemployed","Unknown",])
    Loan = st.selectbox('Do you have a loan?', ["Select","Yes","No"])
    #Features to possibly use for streamlit
    # balance
    # duration - conver seconts to mins (textbox option)
    # campaign
    # age
    # day
    Month = st.selectbox('Month', ['Select','January','February','March',
        'April','May','June','July','August','September','October',
        'November','December'])
    Age = st.slider('Age', min_value=18, max_value=100)
    Duration = st.number_input("Enter Duration of call",00,100,00)
    st.checkbox('Check me out')
    st.radio('Did You Default?', ['yes','no'])
    st.button('Submit')

    '''
    
    
    
    # Prediction :  this is how to dynamically change text
    prediction_state = st.markdown('calculating...')
    y_pred = saved_tree_clf.predict(banker1)

    if y_pred[0] == 0:
        msg = 'This passenger is predicted to be: **died**'
    else:
        msg = 'This passenger is predicted to be: **survived**'

    prediction_state.markdown(msg)
    
