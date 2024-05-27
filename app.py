# External Dependencies
import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# Internal Dependencies
from investor import load_investors_details
from overall import load_overall_analysis

df = pd.read_csv('./startup-funding-4.csv')

# Global Manipulation in data frame
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Startup List
startups = sorted(df['startup'].unique().tolist())

# Investors List
investors = sorted(set(df['investors'].str.split(',').sum()))
investors.remove('')



## Streamlit Section
st.set_page_config(
    layout='wide', 
    page_title='Startup Analysis', 
    page_icon='🏬'
)
st.sidebar.title("Startup funding Analysis") 

st.session_state.option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

options = st.session_state.option

if options=='Overall Analysis':
    load_overall_analysis(df)
elif options=='Startup':
    st.sidebar.title('Startup Analysis')
    st.sidebar.selectbox('Select Startup', startups)
    btn = st.sidebar.button('Find Startup Details')
else:
    selected_investor =  st.sidebar.selectbox('Select Investor', investors)
    btn = st.sidebar.button('Find Investor Details')
    if btn:
        load_investors_details(df, selected_investor)