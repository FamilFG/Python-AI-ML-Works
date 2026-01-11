# Bagging & Ensemble Methods

## Overview
This project explores ensemble learning techniques, specifically Bagging and Random Forest classifiers. It demonstrates how combining multiple weak learners improves model performance and reduces overfitting on heart disease classification tasks.

## Dataset
- `heart_cleveland.csv`: Heart disease classification data with multiple health features

## Ensemble Techniques

### Bagging (Bootstrap Aggregating)
- Creates multiple samples through random sampling with replacement (bootstrapping)
- Trains separate models on each sample
- Aggregates predictions (voting for classification)
- Reduces variance and prevents overfitting

### Random Forest
- Advanced bagging technique using decision trees
- Each tree trained on random subset of features and samples
- Improves robustness through feature randomness
- Handles non-linear relationships effectively

## Projects

### Random Forest Classifier
- **Random-Forest-Classifier.ipynb**: Heart disease prediction
- Classification on medical features
- Hyperparameter tuning with RandomizedSearchCV
- Model visualization and evaluation

## Key Features
- **Ensemble Learning**: Multiple model combination
- **Variance Reduction**: Bootstrap sampling minimizes overfitting
- **Feature Importance**: Identifies key predictive features
- **Robustness**: Better generalization to unseen data

## Model Evaluation
- Classification Report (Precision, Recall, F1-Score)
- Confusion Matrix
- Accuracy Score
- Train vs Test Performance Comparison
- Feature Importance Analysis

## Hyperparameter Tuning
- **RandomizedSearchCV**: Random sampling of parameter combinations
- Fine-tuning number of trees, tree depth, and feature selection

## Visualization
- Tree structure visualization
- Feature importance plots
- Model performance metrics

## Usage
Open `Random-Forest-Classifier.ipynb` in Jupyter Notebook to explore ensemble methods and heart disease classification.

## Requirements
- pandas
- numpy
- scikit-learn
- matplotlib
- scipy
