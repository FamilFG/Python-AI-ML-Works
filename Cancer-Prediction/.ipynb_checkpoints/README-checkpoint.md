# Cancer Prediction

A machine learning project for predicting cancer diagnosis (Benign/Malignant) using Decision Tree and Random Forest classifiers.

## Overview

This project analyzes cancer cell measurements and builds predictive models to classify tumors as benign (B) or malignant (M) based on various features like radius, texture, perimeter, and area.

## Files

- **Cancer-Prediction.ipynb** - Main notebook with model training and evaluation
- **DataFrame-Creation.ipynb** - Synthetic data generation script
- **Cancer_Data.csv** - Original dataset with cancer measurements
- **synthetic_cancer_full.csv** - Generated synthetic dataset for experimentation

## Features

- Data preprocessing and exploratory analysis
- Decision Tree classifier with entropy criterion
- Random Forest classifier
- Model evaluation with classification reports and confusion matrices
- Decision tree visualization
- Hyperparameter tuning with GridSearchCV and RandomizedSearchCV
- Cross-validation analysis
- Entropy calculations for feature importance

## Requirements

- pandas
- numpy
- scikit-learn
- matplotlib
- optuna
- scipy

## Usage

Run the Jupyter notebooks in this order:
1. `DataFrame-Creation.ipynb` - Generate synthetic data
2. `Cancer-Prediction.ipynb` - Train and evaluate models

## Results

The Decision Tree classifier achieves good test accuracy while demonstrating some overfitting on complex decision boundaries.
