import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')  # change the default style

def app():
    st.title('EDA')

    st.write("This is the EDA page")

    st.write("The following is the DataFrame of the Bank Model dataset.")

    df = pd.read_csv('projectdataset-1.csv')
    st.write(df)

    X = df.drop(['Class'], axis=1)
    y = df['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,test_size=0.2, random_state=42)

    X_train.hist(figsize=(15,15))
    plt.show()
    st.pyplot()



