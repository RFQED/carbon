import streamlit as st
import plotly.express as px
import geopandas as gpd

"""
# Welcome to Carbon..!
Something. 
"""
geojsoninfo = {
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}

#df = px.data.election()
#geo_df = gpd.GeoDataFrame.from_features(
#    px.data.election_geojson()["features"]
#).merge(df, on="district").set_index("district")

fig = px.choropleth_mapbox(geo_df,
                           #geojson=geo_df.geometry,
                           geojson=geojsoninfo,
                           center={"lat": 125.6, "lon": 10.1},
                           mapbox_style="open-street-map",
                           zoom=8.5)
st.plotly_chart(fig)
