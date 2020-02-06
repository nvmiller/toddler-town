import streamlit as st
import os # os.chdir("link to data if in different place")
os.chdir(r"/Users/natalie/Documents/insight/project/streamlit")

# Analysis packages
import pandas as pd
import numpy as np
import pickle
import joblib
import sklearn
from sklearn.preprocessing import StandardScaler

# Geo Pkgs
import folium
import geopandas as gpd 
import json

#__________main page_________________

st.title("toddler-town")
st.subheader("estimating population access to daycare in cities")

st.text("toddler-town estimates the number of children under 6 years of age without a daycare spot")

#city = st.selectbox("select a city", ("houston", "austin"))


if st.button("austin"):
	# polygon data
	polygons = gpd.read_file("Austin_Census_Tracts_9Gg.json", driver='geoJSON')
	polygons = polygons[['geometry','FIPS']]
	polygons['FIPS'] = polygons['FIPS'].astype(int)
	# loading city data
	city = pd.read_csv('austin_66_features.csv')
	city_analysis = city.drop(columns=['FIPS'])
	sc = StandardScaler()
	city_analysis_scaled = sc.fit_transform(city_analysis)
	# loading the mode
	loaded_model = joblib.load('finalized_model_lasso.sav')
	city['desert_score'] = loaded_model.predict(city_analysis_scaled)
	# mapping the choropleth
	m = folium.Map(location=[30.2672, -97.7431], zoom_start=10)
	folium.Choropleth(
 		geo_data=polygons,
 		name='choropleth',
 		data=city,
 		columns=['FIPS', 'desert_score'],
 		key_on='feature.properties.FIPS',
 		fill_color='YlOrRd',
 		fill_opacity=0.5,
 		line_opacity=0.2,
 		legend_name='toddler-town score',
 		highlight=True
	).add_to(m)

	st.markdown(m._repr_html_(), unsafe_allow_html=True)


if st.button("houston"):
	# polygon data
	polygons = gpd.read_file("Census_Tracts_Houston1_MgV.json", driver='geoJSON')
	polygons = polygons[['geometry','FIPS']]
	polygons['FIPS'] = polygons['FIPS'].astype(int)
	# loading city data
	city = pd.read_csv('houston_66_features.csv')
	city_analysis = city.drop(columns=['FIPS'])
	sc = StandardScaler()
	city_analysis_scaled = sc.fit_transform(city_analysis)
	# loading the mode
	loaded_model = joblib.load('finalized_model_lasso.sav')
	city['desert_score'] = loaded_model.predict(city_analysis_scaled)
	# mapping the choropleth
	m = folium.Map(location=[29.7604, -95.3698], zoom_start=10)
	folium.Choropleth(
 		geo_data=polygons,
 		name='choropleth',
 		data=city,
 		columns=['FIPS', 'desert_score'],
 		key_on='feature.properties.FIPS',
 		fill_color='YlOrRd',
 		fill_opacity=0.5,
 		line_opacity=0.2,
 		legend_name='toddler-town score',
 		highlight=True
	).add_to(m)

	st.markdown(m._repr_html_(), unsafe_allow_html=True)





