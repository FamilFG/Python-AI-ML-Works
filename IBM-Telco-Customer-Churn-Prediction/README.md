# IBM Telco Customer Churn Prediction

## Overview
This project analyzes and predicts customer churn for IBM's Telco dataset. Using logistic regression with comprehensive preprocessing pipelines, the model identifies customers at risk of leaving the service provider.

## Features
- **Numerical Features**: Tenure, monthly charges, total charges, etc.
- **Categorical Features**: Contract type, internet service, payment method, phone service, online security, etc.
- **Binary Target**: Churn (Yes/No) - customer attrition indicator

## Dataset
- `customer-churn.csv`: IBM Telco customer data with churn labels
- `churn.csv`: Alternative data format for analysis

## Model
- **Algorithm**: Logistic Regression
- **Preprocessing Pipeline**:
  - StandardScaler for numerical features (standardization)
  - OneHotEncoder for categorical features (with unknown handling)
  - ColumnTransformer for unified preprocessing
- **Train-Test Split**: 80/20 ratio with random_state=42

## Data Processing
- Customer IDs are excluded from model features
- Churn values mapped: Yes → 1, No → 0
- Automatic feature type detection (numerical vs categorical)
- Sparse matrix handling for efficient computation

## Evaluation
- Accuracy Score

## Usage
Open `Customer-Churn-Prediction.ipynb` in Jupyter Notebook to explore the model training, preprocessing, and churn predictions.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
