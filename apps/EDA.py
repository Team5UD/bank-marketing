import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')  # change the default style


def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title('EDA')

    st.subheader("Portuguese Bank Marketing Dataset")
    df = pd.read_csv('projectdataset-1.csv')
    df.Class.replace((1, 2), ('no', 'yes'), inplace=True)
# the table  
    st.write(df)

#Pie Chart so show % of sub/not sub
    st.subheader("Subscribed vs Not Subscribed")
    labels = ["Not \nsubscribed", "Subscribed"]
    explode = (0, 0.1)
    fig = plt.figure() 
    ax = fig.add_axes([0,0,1,1]) 

    ax.pie(df['Class'].value_counts(), 
           labels = labels,
           explode = explode,
           autopct ='%1.2f%%',
           frame = True,
           textprops = dict(color ="black", size=12)) 

    ax.axis('equal') 
    plt.title('Subcription to the term deposit\n% of Total Clients',
         loc='left',
         color = 'black', 
         fontsize = '18')

    plt.show()
    st.pyplot()

#correlation matrix for 9 features
    df9 = df[['age',
        'balance',
        'housing',
        'contact', 
        'day',
        'month',
        'duration',   
        'pdays',
        'poutcome',
         'Class']]


    df9.loc[df9['month']=='jan','month']=1
    df9.loc[df9['month']=='feb','month']=2
    df9.loc[df9['month']=='mar','month']=3
    df9.loc[df9['month']=='apr','month']=4
    df9.loc[df9['month']=='may','month']=5
    df9.loc[df9['month']=='jun','month']=6
    df9.loc[df9['month']=='jul','month']=7
    df9.loc[df9['month']=='aug','month']=8
    df9.loc[df9['month']=='sep','month']=9
    df9.loc[df9['month']=='oct','month']=10
    df9.loc[df9['month']=='nov','month']=11
    df9.loc[df9['month']=='dec','month']=12
                                            
    df9.loc[df9['housing']=='yes','housing']=1
    df9.loc[df9['housing']=='no','housing']=2
                                            
    df9.loc[df9['contact']=='unknown','contact']=1
    df9.loc[df9['contact']=='cellular','contact']=2
    df9.loc[df9['contact']=='telephone','contact']=3

    df9.loc[df9['poutcome']=='unknown','poutcome']=1
    df9.loc[df9['poutcome']=='other','poutcome']=2
    df9.loc[df9['poutcome']=='failure','poutcome']=3
    df9.loc[df9['poutcome']=='success','poutcome']=4

    plt.subplots(figsize=(15,10))
    ax = plt.axes()
    ax.set_title("Marketing Characteristic Heatmap For The 9 Features")
    corr = df9.corr()
    sns.heatmap(corr, 
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values,
               cmap="Blues")
    plt.show()
    st.subheader("Correlation Matrix")

    st.pyplot()

#Chart for Age
    st.subheader("Age Feature")
    plt.figure(figsize=(19, 9))
    sns.countplot(data=df, x='age', hue='Class')
    st.pyplot()

    st.write("")
# Chart for month
    st.subheader("Month Feature")
    fig, ax = plt.subplots(figsize = (15, 5))
    sns.countplot(x = 'month', data = df, order = ['jan','feb','mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    ax.set_xlabel("Months")
    ax.set_ylabel("Count")
    ax.set_title("Count of contacts made in each month")
    st.pyplot()

    df.loc[df['month']=='jan','month']=1
    df.loc[df['month']=='feb','month']=2
    df.loc[df['month']=='mar','month']=3
    df.loc[df['month']=='apr','month']=4
    df.loc[df['month']=='may','month']=5
    df.loc[df['month']=='jun','month']=6
    df.loc[df['month']=='jul','month']=7
    df.loc[df['month']=='aug','month']=8
    df.loc[df['month']=='sep','month']=9
    df.loc[df['month']=='oct','month']=10
    df.loc[df['month']=='nov','month']=11
    df.loc[df['month']=='dec','month']=12

    dict1=dict(list(df.groupby(['month','Class'])))
    list1=[1,2,3,4,5,6,7,8,9,10,11,12]
    no=[]
    yes=[]
    months=[]
    for i in list1:
      months.append(i)
      for j in ['no','yes']:
        if(j=='no'):
          no.append(dict1[i,j].count()['Class'])
        else:
          yes.append(dict1[i,j].count()['Class'])

    total_count_per_month=[]
    dict2=dict(list(df.groupby(['month'])))
    for i in list1:
      total_count_per_month.append(dict2[i].count()['Class'])

    
    month_wise=pd.DataFrame()
    month_wise['Months']=months
    month_wise['Total Enteries per month']=total_count_per_month
    month_wise['Count of Subscribed']=yes
    month_wise['Count of Not Sub']=no
    month_wise['Subscription Rate %']=round((month_wise['Count of Subscribed']/month_wise['Total Enteries per month'])*100)
    month_wise['Not Sub Rate %']=round((month_wise['Count of Not Sub']/month_wise['Total Enteries per month'])*100)
    month_wise=month_wise.sort_values("Months",ascending=True)
    
    st.write("Based off the chart above, May has the most contact made to the customer (",13766,") but the least amount of subscription rate (",7,"%) compared to March which has the second least contact rate (",477,") but the highest subscription rate (",52,"%)")
    st.dataframe(month_wise)


##Housing
    st.subheader("Housing Feature")
    housing_y=df[df['housing']=='yes']
    housing_n=df[df['housing']=='no']

    total=df.shape[0]
    yes=housing_y.count()['Class']
    no=housing_n.count()['Class']
    sns.countplot(df['housing'])
    st.pyplot()

    st.write(round((yes/total)*100,2),"% of customers, which mean",yes," has a house loan and" ,round((no/total)*100,2),"% do not have a house loan with a count of",no)

    yes=housing_y[housing_y['Class']=='yes'].count()['Class']
    no=housing_y[housing_y['Class']=='no'].count()['Class']
    total=housing_y.count()['Class']
    st.write("Out of the total amount of customers that have a house loan",round((yes/total)*100,2)," % subscribed to term deposit and",round((no/total)*100,2),"% did not subscribe")

##Contact
    st.subheader("Contact Feature")
    sns.countplot(df['contact'],hue=df['Class'])
    st.pyplot()

##duration
    st.subheader("Duration Feature")
    plt.figure(figsize=(20,5))
    plt.xticks(np.arange(0,5000,150))
    sns.scatterplot(df['duration'],df['campaign'],hue=df['Class'])
    st.pyplot()
    st.write("For duration of the calls, if the call had a shorter duration the customers least likelty subscribed to the term deposite while when calls lasted longer you can see more customers subscriing.")


