# E-Commerce Sales Prediction

## Overview
This project predicts the number of units sold in e-commerce transactions using linear regression. It features a custom linear regression implementation from scratch with gradient descent optimization.

## Features
- **Temporal Features**: Month and day of week extracted from date
- **Product Category**: Categorical encoding of product types
- **Customer Segment**: Customer segment classification
- **Price and Promotional Features**: Additional sales factors

## Dataset
- `dataset.csv`: E-commerce transaction data with sales outcomes

## Model
- **Custom LinearRegression Implementation**:
  - Gradient descent optimization
  - Configurable learning rate (alpha)
  - Optional feature normalization
  - Adjustable iterations
- **Train-Validation-Test Split**: 60/20/20 split with random_state=42
- **Preprocessing**:
  - Date-time feature engineering
  - One-hot encoding for categorical variables
  - Feature standardization

## Hyperparameters
- **iterations**: Number of gradient descent iterations (default: 10,000)
- **alpha**: Learning rate for gradient descent (default: 0.01)
- **normalize**: Whether to standardize features (default: True)

## Usage
Open `E-Commerce-Sales-Prediction.ipynb` in Jupyter Notebook to explore the custom linear regression model and sales predictions.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
