# Dron Delivery Code

## Overview
This project predicts on-time delivery performance for drone deliveries using machine learning. The model analyzes various factors including distance, payload, weather conditions, and route complexity to classify deliveries as on-time or late.

## Features
- **Drone Models**: Different drone types and their characteristics
- **Route Analysis**: Parsing route turns and altitude profile changes
- **Weather Data**: Wind direction, speed, and gust information
- **Temporal Features**: 15-minute time slots for delivery scheduling
- **Operator Tags**: Operator-specific performance factors
- **Landing Zones**: Delivery destination zones

## Dataset
- `train.csv`: Training data with delivery outcomes
- `test.csv`: Test data for predictions

## Model
- **Algorithm**: Logistic Regression
- **Preprocessing**: 
  - Categorical encoding with OneHotEncoder
  - Numerical feature scaling
  - Feature engineering from raw route and weather data
- **Evaluation**: Cross-validation with log loss and ROC-AUC metrics

## Usage
Open `Dron-Delivery-Code.ipynb` in Jupyter Notebook to explore the analysis and model training.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
