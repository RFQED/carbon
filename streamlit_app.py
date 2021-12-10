import plotly.express as px
import pandas as pd
import json
import geojson
import geopandas as gpd
import streamlit as st

st.set_page_config(layout="wide")

geojson = gpd.read_file('geojson_suburbs.json')
df = pd.read_csv('electiondata.csv')

#mapbox_token='pk.eyJ1IjoicmZxZWQiLCJhIjoiY2t4MHBxZjE4MHU3NzJ2bnl3cmV6bzZodCJ9.qwxACnMntkPpdmBIa1zzug'
#px.set_mapbox_access_token(mapbox_token)
plot_variable = st.selectbox(
     'Variable to be plotted.',
     ('MeasuredRainFall[cm^3/m^2]', 'Home phone', 'Mobile phone'))


fig = px.choropleth_mapbox(df, geojson=geojson, color=plot_variable,
                           locations="district", featureidkey="properties.district",
                           center={"lat": 55.836, "lon": -4.754},
                           mapbox_style="carto-positron", zoom=11, opacity=0.4 )

fig.update_layout( height=750, margin={"r":0,"t":0,"l":0,"b":0}, mapbox = {
        'style': "mapbox://styles/rfqed/ckx0prtk02gmq15mty3tlmhpu"},
    showlegend = False)

fig.update_mapboxes(pitch=45)
##
#fig.update_layout(height=750, margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)
