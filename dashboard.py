import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
st.set_page_config(layout='wide')

# Project colour palette: ocean themed 🌊
color_primary = 'teal'
color_secondary = 'coral'  
color_accent = 'turquoise'

# Creating the st.cache_data for the datasets to reduce loading time and better user experience
@st.cache_data
def load_dataset():
    df_latest = pd.read_csv('data/processed/atlantic_sites_latest.csv')
    df_history = pd.read_csv('data/processed/atlantic_sites_history.csv')
    return df_latest, df_history

# Creating the st.cache_resource for model and preprocessor to reduce loading time and better user experience
@st.cache_resource
def load_model_and_preprocessor():
    model = joblib.load('models/rf_atlantic_model.pkl')
    preprocessor = joblib.load('models/rf_atlantic_preprocessor.pkl')
    return model, preprocessor

# Invoking the functions to load both datasets, model and preprocessor
df_latest, df_history = load_dataset()
model, preprocessor = load_model_and_preprocessor()

# Setting the title and the layout of the dashboard
st.title('Coral Bleaching Analysis and Prediction')
col_map, col_right = st.columns([4, 1.5])
with col_map:
    st.subheader('Atlantic Reef Sites')
    # Creating a temporary column to use ad legend input
    df_latest['Status'] = df_latest['Bleaching_Binary'].map({'none': 'No Bleaching', 'bleaching': 'Bleached'})

    # Map: Atlantic reef sites coloured by bleaching status
    fig = px.scatter_map(
        df_latest,
        lat='Latitude_Degrees',
        lon='Longitude_Degrees',
        center={'lat': 20, 'lon': -75},
        color='Status',
        color_discrete_map={'Bleached': 'coral', 'No Bleaching': 'teal'},
        category_orders={'Status': ['No Bleaching', 'Bleached']},
        zoom=2.5,
        map_style='carto-positron'
    )
    fig.update_layout(legend=dict(x=0.87, y=0.96),
                      height=600)
    selected = st.plotly_chart(fig, width='stretch', on_select='rerun', key='map')

with col_right:
    st.subheader('Bleaching History')
    points = selected['selection']['points']
    if points:
        lat_click = points[0]['lat']
        lon_click = points[0]['lon']
        site_history = df_history[
        (abs(df_history['Latitude_Degrees'] - lat_click) < 0.01) & 
        (abs(df_history['Longitude_Degrees'] - lon_click) < 0.01)
        ]
        site_history['Status'] = site_history['Bleaching_Binary'].map({'none': '✅ No Bleaching', 'bleaching': '🚨 Bleached'})
        site_history['Date'] = site_history['Date_Month'].astype(str) + '/' + site_history['Date_Year'].astype(str)
        site_history['Site_Name'] = site_history['Site_Name'].fillna('Not Specified')
        site_history = site_history[['Date_Year', 'Date_Month', 'Date', 'Site_Name', 'Country_Name', 'Status']].sort_values(['Date_Year', 'Date_Month'])
        site_history = site_history[['Date', 'Site_Name', 'Country_Name', 'Status']]
        site_history = site_history.drop_duplicates(subset=['Date'])
        st.dataframe(site_history, hide_index=True)
st.divider()
st.subheader('Predict Bleaching Risk')


