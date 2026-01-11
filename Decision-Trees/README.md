# Decision Trees

## Overview
This project explores Decision Tree classifiers using the Iris dataset and heart disease data. It covers overfitting prevention, hyperparameter tuning, and optimization techniques including Random Search, Grid Search, and Optuna.

## Datasets
- `heart_cleveland.csv`: Heart disease classification dataset
- Iris dataset: Built-in scikit-learn dataset for flower species classification

## Project Structure

### Basic Grid & Randomized Search
- **Decision-Tree-Classifier-Overfitting.ipynb**: Demonstrates overfitting and how to prevent it with `min_samples_split`
- **Decision-Tree-Classifier-Randomized-Grid_Search.ipynb**: Compares Randomized Search and Grid Search for hyperparameter tuning
- **Decision-Tree-Classifier-Optuna.ipynb**: Uses Optuna for Bayesian optimization

### Hyperparameter Tuning
- **Decision-Tree-Classifier-Optuna.ipynb**: Advanced optimization with Optuna
- **Decision-Tree-Classifier-Randomized-Grid_Search.ipynb**: Systematic hyperparameter search

### Simple Overfitting
- **Decision-Tree-Classifier-Overfitting.ipynb**: Basic overfitting demonstration and prevention

### Random Forest
- **Random-Forest-Classifier.ipynb**: Ensemble method using multiple decision trees

## Key Concepts
- **Overfitting Prevention**: Using constraints like `min_samples_split`, `max_depth`
- **Hyperparameter Tuning**: Grid Search, Randomized Search, Optuna
- **Ensemble Methods**: Random Forest for improved accuracy
- **Model Evaluation**: Accuracy, Precision, Recall, F1-Score, Confusion Matrix

## Evaluation Metrics
- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- Classification Report
- Confusion Matrix

## Usage
Open any notebook in Jupyter to explore different aspects of decision trees and optimization techniques.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
- optuna
