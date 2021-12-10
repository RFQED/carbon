import plotly.express as px
import pandas as pd
import json
import streamlit as st
st.set_page_config(layout="wide")

with open("geojson_suburbs.json") as response:
    suburbs = json.load(response)


df = pd.DataFrame(data={'suburb': ['a', 'b'], 'phase': ['d', 'e']})

mapbox_token='pk.eyJ1IjoicmZxZWQiLCJhIjoiY2t4MHBxZjE4MHU3NzJ2bnl3cmV6bzZodCJ9.qwxACnMntkPpdmBIa1zzug'
px.set_mapbox_access_token(mapbox_token)

fig = px.choropleth_mapbox(
    df, 
    geojson=suburbs, 
    locations='suburb',
    color='phase',
    color_continuous_scale="Viridis",
    range_color=(0, 2),
    zoom=3, 
    center = {"lat": 55.828, "lon": -4.731},
    opacity=0.2)
fig.update_layout(height=750, margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)


#
#
#import streamlit as st
#import plotly.express as px
#import geopandas as gpd
#
#"""
## Welcome to Carbon..!
#Something. 
#"""
#geojsoninfo = {
#  "type": "Feature",
#  "geometry": {
#    "type": "Point",
#    "coordinates": [125.6, 10.1]
#  },
#  "properties": {
#    "name": "Dinagat Islands"
#  }
#}
#
##df = px.data.election()
##geo_df = gpd.GeoDataFrame.from_features(
##    px.data.election_geojson()["features"]
##).merge(df, on="district").set_index("district")
#
#fig = px.choropleth_mapbox(geo_df,
#                           #geojson=geo_df.geometry,
#                           geojson=geojsoninfo,
#                           center={"lat": 125.6, "lon": 10.1},
#                           mapbox_style="open-street-map",
#                           zoom=8.5)
#st.plotly_chart(fig)

