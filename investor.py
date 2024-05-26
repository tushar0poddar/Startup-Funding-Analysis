import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# Loading Investor Details
def load_investors_details(df, investor):
    st.title(investor)
    st.subheader('Most Recent Investments')
    # Recent Investments
    recent_investments = df[df['investors'].str.contains(investor )].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.dataframe(recent_investments)

    #Section 1
    col1, col2 = st.columns(2)
    # Maximum Investment
    with col1:
        max_investment = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Top Biggest Investments')

        # Plotting Bar chart
        fig, ax = plt.subplots()
        ax.bar(max_investment.index, max_investment.values)
        st.pyplot(fig)
    
    # Investments Sectors
    with col2: 
        verticals = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()

        st.subheader('Investment Sectors ')
        # Plotting Pie graph
        fig, ax = plt.subplots()
        ax.pie(verticals, labels=verticals.index, autopct='%0.01f%%')
        st.pyplot(fig)

    # Section 2
    col3, col4 = st.columns(2)
    # Investment Stages
    with col3: 
        rounds = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()

        st.subheader('Investment Rounds')
        # Plotting Pie graph
        fig, ax = plt.subplots()
        ax.pie(rounds, labels=rounds.index, autopct='%0.01f%%')
        st.pyplot(fig)

    # Investment Cities
    with col4: 
        cities = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()

        st.subheader('Investment Cities')
        # Plotting Pie graph
        fig, ax = plt.subplots()
        ax.pie(cities, labels=cities.index, autopct='%0.01f%%') 
        st.pyplot(fig)


    # Section 3
    col5, col6 = st.columns(2)
    # Year on Year Investments
    with col5:
        yoy_investment = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

        st.subheader(' Year on Year Investments')
        # Plotting Line graph
        fig, ax = plt.subplots()
        ax.plot(yoy_investment.index, yoy_investment.values) 
        st.pyplot(fig)