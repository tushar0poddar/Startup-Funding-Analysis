import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

def load_overall_analysis(df):
    st.title('Overall Analysis')

    # Section 1
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        # Total Investment Amount
        total = round(df['amount'].sum())
        st.metric('Total', str(total)+ ' Cr')

    with c2:
        # Maximum Funding Raised
        max_funding = round(df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(1)[0])
        st.metric('Maximum', str(max_funding)+ ' Cr')
    
    with c3:
        # Average Ticket Size
        avg_funding = round(df.groupby('startup')['amount'].sum().mean())
        st.metric('Avg', str(avg_funding)+ ' Cr')
    
    with c4:
        # Total Funded Startups
        no_of_startups = df['startup'].nunique()
        st.metric('Total Funded  Startups', no_of_startups)


    # Section 2
    st.header('Month on Month (MOM) Analysis')

    selected_opt =  st.selectbox('Select Options', ['Total Amount', 'Number of Startups Funded'])

    if selected_opt == 'Total Amount':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        y_axis = temp_df['amount']
    else:
        temp_df = df.groupby(['year', 'month'])['startup'].count().reset_index()
        y_axis = temp_df['startup']

    temp_df['x-axis'] = temp_df['month'].astype(str) + '-'+temp_df['year'].astype(str)

    # Plotting Pie graph
    fig, ax = plt.subplots()
    ax.plot(temp_df['x-axis'], y_axis) 
    st.pyplot(fig)
