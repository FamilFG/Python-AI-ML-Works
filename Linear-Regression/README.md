# Linear Regression

## Overview
This project explores linear regression models for predicting continuous values across multiple real-world datasets including Boston housing prices, car predictions, and online retail sales. Features both scikit-learn implementations and custom preprocessing techniques.

## Datasets
- `bostonhouses.csv`: Boston Housing dataset for price prediction
- `HousingData.csv`: Housing market data
- `turboaz.csv`: Turboaz vehicle data for car prediction

## Projects

### Boston Houses Price Prediction
- **LinearRegression-BostonHouses.ipynb**: Predicts median house prices
- 13 input features including crime rate, rooms, age, and location factors
- Comprehensive outlier detection using IQR method
- Dataset cleaning and feature validation

### Car Prediction
- **LinearRegression-Car-Prediction.ipynb**: Predicts car attributes
- Turboaz vehicle dataset analysis
- Feature engineering and scaling

### Online Retail Sales Prediction
- **LinearRegression-Online-Retail.ipynb**: Predicts sales metrics
- E-commerce transaction data
- Time-series and feature analysis

## Features (Boston Houses)
- **CRIM**: Crime rate per capita
- **ZN**: Proportion of land zoned for large lots
- **INDUS**: Proportion of non-retail business acres
- **CHAS**: Charles River dummy variable
- **NOX**: Nitrogen oxide concentration
- **RM**: Average rooms per dwelling
- **AGE**: Proportion of buildings built before 1940
- **DIS**: Distance to employment centers
- **RAD**: Index of highway accessibility
- **TAX**: Property tax rate
- **PTRATIO**: Pupil-teacher ratio
- **B**: Proportion of African Americans
- **LSTAT**: Lower status population percentage
- **MEDV**: Median home value (target)

## Data Preprocessing
- Missing value handling with `dropna()`
- Outlier detection using Interquartile Range (IQR)
- Statistical methods for identifying anomalies
- Feature scaling and normalization

## Model Evaluation
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Residual Analysis

## Usage
Open any notebook in Jupyter to explore different linear regression applications and preprocessing techniques.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
