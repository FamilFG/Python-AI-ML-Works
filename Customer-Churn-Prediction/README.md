# Customer Churn Prediction

## Overview
This project predicts whether customers will churn (leave) from a service provider. The model uses logistic regression with preprocessing pipelines to handle both numerical and categorical features.

## Features
- Numerical features: Tenure, monthly charges, total charges, etc.
- Categorical features: Contract type, internet service, payment method, etc.
- Binary target: Churn (Yes/No)

## Dataset
- `customer-churn.csv`: Customer data with churn labels
- `churn.csv`: Alternative churn dataset

## Model
- **Algorithm**: Logistic Regression
- **Preprocessing Pipeline**:
  - StandardScaler for numerical features
  - OneHotEncoder for categorical features
  - ColumnTransformer for combined preprocessing
- **Train-Test Split**: 80/20 ratio with random_state=42

## Evaluation
- Accuracy Score

## Usage
Open `Customer-Churn-Prediction.ipynb` in Jupyter Notebook to explore the model training and predictions.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
