from os import write
from matplotlib import pyplot as plt
import pandas as pd
from pandas.core import groupby
import streamlit as st

def load_data():
    df = pd.read_csv('data.csv')
    return df

df = load_data()

def show_explore_page():
    st.title('Explore Programmers Salaries')

    st.write(

        '''
        ### Kaggle Survey 2021
        '''
    )

    data = df['Country'].value_counts().nlargest(10)

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    st.write('#### Distribution of the top 10 countries')

    st.pyplot(fig1)

    st.write(
        '''
        #### Top 40 countries by Average Annual Salary ($USD)
        '''
    )

    data = df.groupby(['Country'])['Average Annual Salary ($USD)'].mean().nlargest(40)
    st.bar_chart(data)

    st.write(
        '''
        ####  Total Salary by Number of Programming Languages
        '''
    )

    data = df.groupby(['Num Language'])['Average Annual Salary ($USD)'].sum().sort_values(ascending=True)
    st.line_chart(data)