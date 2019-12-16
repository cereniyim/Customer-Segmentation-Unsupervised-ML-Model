This notebook does a detailed analysis about ASHRAE's energy consumption data available in [Kaggle](https://www.kaggle.com/c/ashrae-energy-prediction).

Three csv files analyzed, in total 20 million rows:
1. building_metadata: characteristics of a building
2. weather_train: weather data measured between 1 Jan - 31 Dec 3016 among different sites
3. train: energy consumption of the buildings available in building_metadata between 1 Jan - 31 Dec 3016 in four different energy categories:
  * electricity
  * steam
  * chilled water
  * hot water
  
This is also initial part of a machine learning problem aiming to predict the energy consumption of the building. Thus, during the detailed analysis, focus is kept on the `meter_reading` values and its relationship to other variables.

Original kernel is available [here](https://www.kaggle.com/cereniyim/save-the-energy-for-the-future-1-detailed-eda).

Analysis is done with Python 3 and with the following libraries:
* plotly
* pandas
* seaborn
* pandas_profiling
