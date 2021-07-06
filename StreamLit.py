# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import joblib
from sklearn.model_selection import train_test_split
plt.style.use('seaborn')  # change the default style
from sklearn import tree
from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.model_selection import GridSearchCV



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
