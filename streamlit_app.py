import plotly.express as px
import pandas as pd
import json
import geojson
import geopandas as gpd
import streamlit as st
import random
import numpy as np

st.set_page_config(layout="wide")

'''
This is a quick project to explore geospatial analysis tools. This is example data, not to be used. This tool was written on Fri 11th/Sat 12th December and probably not developed further after.

The map is fully interactive to allow web-based exploration. 
'''

geojson = gpd.read_file('geojson_suburbs.json')
df = pd.read_csv('electiondata.csv')

mapbox_token='pk.eyJ1IjoicmZxZWQiLCJhIjoiY2t4MHBxZjE4MHU3NzJ2bnl3cmV6bzZodCJ9.qwxACnMntkPpdmBIa1zzug'
px.set_mapbox_access_token(mapbox_token)


col1, col2 = st.columns(2)

with col1:
    plot_variable = st.selectbox(
        'Variable to be plotted.',
        ('Avg_Soil_Magnesium','MeasuredRainFall[cm^3/m^2]', 'Avg_Soil_Calcium', 'derivedCO2Absorbed'))

with col2:
    plot_zscale = st.selectbox(
        'Colourscale to use.',
        ('viridis','blackbody', 'rainbow', 'thermal'))

random_lat = np.random.uniform(55.8926412, 55.7557135, 50)
random_lon = np.random.uniform(-4.8405405, -4.554896, 50)
random_sizes = np.random.uniform(1, 30, 50)
random_str_options = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega', 'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
random_str = random.sample(random_str_options, 50)


fig = px.choropleth_mapbox(df, geojson=geojson, color=plot_variable,
                           color_continuous_scale=plot_zscale,
                           locations="district", featureidkey="properties.district",
                           center={"lat": 55.836, "lon": -4.754},
                           zoom=11, opacity=0.4 )


fig.add_scattermapbox(lat = random_lat,
                      lon = random_lon,
                      mode = 'markers+text',
                      text = random_str,
                      below='',                 
                      marker_size=random_sizes, marker_color='rgb(235, 0, 100)')

fig.update_layout( height=750, margin={"r":0,"t":0,"l":0,"b":0}, mapbox = {
        'style': "mapbox://styles/rfqed/ckx0prtk02gmq15mty3tlmhpu"},
    showlegend = False)

fig.update_mapboxes(pitch=35)
##
#fig.update_layout(height=750, margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)
