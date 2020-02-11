# Toddler-town

Toddler-town is a modeling tool for estimating daycare need in cities across different neighborhoods. The model estimates a mis-match between supply and demand of daycare spots. It was developed using data from the city of Houston, but the workflow to develop the model could be applied to any city. 

Python was used for data pre-processing, modeling, and geospatial mapping. Toddler-town’s app was developed using Streamlit and deployed on an AWS server. 

## Data sources

Data are collected from several sources:
1.	The United States Census Bureau for demographic and employment information from the American Community Survey. `https://www.census.gov/programs-surveys/acs`
2.	The Quandl API for rental cost information from Zillow. `quandl.com/data/ZILLOW-Zillow-Real-Estate-Research`
3.	The Office of Policy Development and Research for information on residential and business density. `huduser.gov/portal/datasets/usps_crosswalk.html`
4.	Harvard University WorldMap for geospatial data on census tracts. `worldmap.harvard.edu`
5.	Texas Health and Human Services for addresses and capacities of licensed daycares in Houston. `dfps.state.tx.us/Child_Care/Search_Texas_Child_Care` 

## Data processing 

1.	Feature data, including demographic, employment, rental cost, residential/business density, are aggregated at the level of census tract.
2.	The target variable, difference between supply and demand of daycare spots, is calculated using capacity data and demographic data. 

## Modeling and validation

1.	Lasso regression is used to predict daycare need from input features. 
2.	Cross-validation with grid search is used to tune the alpha hyperparameter.
3.	The trained model is 91% accurate for predicting daycare need on a test set. 

## Visualization and user input

Users select a city through a python/Streamlit app. The model is applied to the selected city’s feature data to produce predictions for daycare need. A heatmap of daycare need is generated for users to explore, coded by census tract. 

## Data structures

1. Geospatial data for census tracts by city are in `Austin_Census_Tracts_9Gg.json` and `Census_Tracts_Houston1.MgV.json`.
2. Feature data for cities are in `austin_66_features.csv` and `houston_66_features.csv`.
3. The lasso model is contained in `finalized_model_lasso.sav`.
4. `app4.py` is the streamlit file.


