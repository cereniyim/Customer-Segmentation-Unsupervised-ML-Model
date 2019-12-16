This notebook aims to predict a building's energy consumption over 2017 and 2018 using the data from 2016 in 4 different consumpiton categories (electricity, chilled water, steam, hot water) using ASHRAE data, which is our problem statement as well.

This is a supervised machine learning model, meaning based on the columns available in the datasets and data from 2016, we are going to train the model to predict an energy consumption of a building in each category. Since, consumption values are labeled as meter_reading and they are continuous, we are going to apply regression techniques to generate predictions on meter_reading.

It is a highly debated and popular competition in Kaggle currently, however my main motivation is to contribute to make energy-efficient buildings by estimating its energy consumption. It seemed like a good start to save our energy for future!

There will be 3 notebooks covering the complete machine learning building pipeline. Original links to kernels can be found below as well as the content for each notebook.

[Notebook 1](https://www.kaggle.com/cereniyim/save-the-energy-for-the-future-1-detailed-eda) will focus on parts 1 and 2 and provide information about the datasets with a detailed EDA.
[Notebook 2](https://www.kaggle.com/cereniyim/save-the-energy-for-the-future-2-fe-lightgbm) will focus on parts 3, 4 and 5 focusing on building the optimal machine learning model.
[Notebook 3](https://www.kaggle.com/cereniyim/save-the-energy-for-the-future-3-predictions) will focus on parts 6, 7 and 8 generating and interpreting the predictions with the best model and summary for the whole project.

1) Understand, Cleand and Format Data

2) Exploratory Data Analysis

3) Feature Engineering & Selection with a simple ML Model

4) Compare Several Machine Learning Models

5) Perform Hyperparameter Tuning and Cross Validation on the Best Model

6) Evaluate the Best Model with Test Data

7) Interpret Model Results

8) Summary & Conclusions
