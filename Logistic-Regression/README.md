# Logistic Regression

## Overview
This project explores logistic regression for binary classification across multiple real-world datasets. It includes both scikit-learn implementations and a custom logistic regression implementation from scratch using gradient descent.

## Datasets
- `exams.csv`: Exam scores predicting admission
- `framingham.csv`: Heart disease prediction data
- `titanic.csv`: Titanic passenger survival prediction

## Projects

### Exam Score Prediction
- **LogisticRegression-Exams.ipynb**: Predicts admission based on two exam scores
- Dataset: Student exam performance and admission status
- Visualization: Scatter plots showing passing/failing classifications

### Heart Disease Prediction
- **LogisticRegression-HeartDisease.ipynb**: Framingham Heart Study data
- Predicts presence/absence of heart disease
- Multiple health features and risk factors

### Iris Classification
- **LogisticRegression-Iris.ipynb**: Multi-class classification on Iris dataset
- Classic flower species classification
- Feature: Sepal/petal measurements

### Titanic Survival Prediction
- **LogisticRegression-Titanic.ipynb**: Predicts passenger survival
- Features: Age, sex, passenger class, fare, etc.
- Historical dataset from RMS Titanic disaster

### Exercise & Testing
- **LogisticRegression-Exercise.ipynb**: Practice problems and exercises
- **LogisticRegression-YTtest.ipynb**: Additional test cases and validation

## Custom Implementation
The project includes `MyLogisticRegression` class with:
- **Sigmoid Function**: Probability transformation
- **Cost Function**: Binary cross-entropy loss
- **Gradient Descent**: Iterative optimization
- **Configurable Parameters**:
  - `alfa`: Learning rate
  - `iterations`: Number of optimization steps
  - `normalize`: Feature normalization option

## Evaluation Metrics
- Accuracy Score
- Precision, Recall, F1-Score
- Classification Reports
- Confusion Matrices
- ROC-AUC Scores

## Usage
Open any notebook in Jupyter to explore different logistic regression applications and implementations.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
