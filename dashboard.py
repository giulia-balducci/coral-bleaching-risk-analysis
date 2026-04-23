import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
st.set_page_config(layout='wide')

st.markdown("""
<style>
[data-testid="stSlider"] [role="slider"] {
    background-color: teal !important;
    border-color: teal !important;
}
[data-testid="stSlider"] [data-testid="stSliderTrackFill"] {
    background-color: coral !important;
}
</style>
""", unsafe_allow_html=True)

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
col_map, col_right = st.columns([4, 2])
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
    if not points:
        st.markdown("""<div style="background-color:#e0f5f5; border-left:4px solid teal;
            padding:12px; border-radius:4px; color:#005555;">
            👆 Click a site on the map to explore its bleaching history and predict risk.</div>""",
            unsafe_allow_html=True)
    if points:
        lat_click = points[0]['lat']
        lon_click = points[0]['lon']
        # History table
        site_history = df_history[
            (abs(df_history['Latitude_Degrees'] - lat_click) < 0.01) & 
            (abs(df_history['Longitude_Degrees'] - lon_click) < 0.01)
        ]
        site_history['Status'] = site_history['Bleaching_Binary'].map({'none': '✅ No Bleaching', 'bleaching': '🚨 Bleached'})
        site_history['Date'] = site_history['Date_Month'].astype(str) + '/' + site_history['Date_Year'].astype(str)
        name_match = df_history[
            (abs(df_history['Latitude_Degrees'] - lat_click) < 0.01) &
            (abs(df_history['Longitude_Degrees'] - lon_click) < 0.01) &
            df_history['Site_Name'].notna()
        ]['Site_Name']
        site_name = name_match.iloc[0] if len(name_match) > 0 else 'Not Recorded'
        site_history['Site_Name'] = site_name
        site_history = site_history[['Date_Year', 'Date_Month', 'Date', 'Site_Name', 'Country_Name', 'Status']].sort_values(['Date_Year', 'Date_Month'])
        site_history = site_history[['Date', 'Site_Name', 'Country_Name', 'Status']].drop_duplicates(subset=['Date'])
        st.dataframe(site_history, hide_index=True)
        # Latest observation for slider defaults
        # .iloc[0] converts the filtered DataFrame (1-row table) into a Series
        # so site_latest['Temperature_Mean'] returns a float, not a column
        site_latest = df_latest[
            (abs(df_latest['Latitude_Degrees'] - lat_click) < 0.01) &
            (abs(df_latest['Longitude_Degrees'] - lon_click) < 0.01)
        ].iloc[0]

    st.divider()
    st.subheader('Predict Bleaching Risk')
    if points:
        col_depth, col_reset = st.columns([1, 1])
        with col_depth:
            st.metric(label="Site Depth (m)", value=f"{site_latest['Depth_m']:.1f}")
        with col_reset:
            st.write('')
            st.write('')
            if st.button('Reset to site values'):
                st.session_state['temp'] = float(site_latest['Temperature_Mean']) - 273.15
                st.session_state['dhw'] = float(site_latest['TSA_DHW'])
                st.session_state['tsa_freq'] = float(site_latest['TSA_Frequency'])
                st.session_state['month'] = int(site_latest['Date_Month'])
                st.session_state['year'] = int(site_latest['Date_Year'])
                st.session_state.pop('prediction', None)

        # Reset session_state when a new site is selected
        if st.session_state.get('last_site') != (lat_click, lon_click):
            st.session_state['last_site'] = (lat_click, lon_click)
            st.session_state['temp'] = float(site_latest['Temperature_Mean']) - 273.15
            st.session_state['dhw'] = float(site_latest['TSA_DHW'])
            st.session_state['tsa_freq'] = float(site_latest['TSA_Frequency'])
            st.session_state['month'] = int(site_latest['Date_Month'])
            st.session_state['year'] = int(site_latest['Date_Year'])

        col_s1, col_s2 = st.columns(2)
        with col_s1:
            temp = st.slider('Temperature (°C)',
                             min_value=(float(df_latest['Temperature_Mean'].min()) - 273.15),
                             max_value=(float(df_latest['Temperature_Mean'].max()) - 273.15),
                             key='temp')
        with col_s2:
            dhw = st.slider('Degree Heating Weeks',
                            min_value=float(df_latest['TSA_DHW'].min()),
                            max_value=float(df_latest['TSA_DHW'].max()),
                            key='dhw')
        col_s3, col_s4 = st.columns(2)
        with col_s3:
            tsa_freq = st.slider('Thermal Stress Freq.',
                            min_value=float(df_latest['TSA_Frequency'].min()),
                            max_value=float(df_latest['TSA_Frequency'].max()),
                            key='tsa_freq')
        with col_s4:
            month = st.slider('Month', min_value=1, max_value=12, key='month')
        col_s5, col_predict = st.columns([1, 1])
        with col_s5:
            year = st.slider('Year',
                             min_value=int(df_latest['Date_Year'].min()),
                             max_value=int(df_latest['Date_Year'].max()),
                             key='year')
        with col_predict:
            st.write('')
            st.write('')
            if st.button('Predict Bleaching Risk', use_container_width=True):
                X = pd.DataFrame([site_latest])
                X['Temperature_Mean'] = temp + 273.15
                X['TSA_DHW'] = dhw
                X['TSA_Frequency'] = tsa_freq
                X['Date_Month'] = month
                X['Date_Year'] = year
                X_transformed = preprocessor.transform(X)
                st.session_state['prediction'] = model.predict(X_transformed)[0]

        if 'prediction' in st.session_state:
            if st.session_state['prediction'] == 'bleaching':
                st.warning("⚠️ Bleaching risk detected. Visual inspection by a conservation team is advised.")
            else:
                st.success("✅ No significant bleaching risk detected.")



