# Pull Request: Boosting Algorithms Implementation

## Description
Two ensemble learning regressors for predictive modeling:
- **XGBoost-Regressor.ipynb**: XGBoost for laptop price prediction on `Laptop_price.csv`
- **Gradient-Descent-Regressor.ipynb**: Scikit-learn GradientBoostingRegressor for house price prediction on `house_prices_dataset.csv`

## What's Being Added

### 1. XGBoost-Regressor.ipynb
- Dataset: `Laptop_price.csv`
- Features: Data preprocessing, train-test split (80/20), metrics evaluation
- Metrics: R² Score, MAE, MSE, RMSE (train & test)
- Includes feature importance analysis

### 2. Gradient-Descent-Regressor.ipynb
- Dataset: `house_prices_dataset.csv`
- Features: GridSearchCV hyperparameter tuning, model evaluation
- Metrics: R² Score, MAE, MSE, RMSE (train & test)
- Model explanation functions included

## Dependencies
```
pandas, numpy, matplotlib
scikit-learn (GradientBoostingRegressor, GridSearchCV)
xgboost
```

## Key Features
- ✓ Proper train-test split (80/20) with fixed random state (42)
- ✓ Comprehensive evaluation metrics on both train and test sets
- ✓ `explain_model1()` function for model performance reporting
- ✓ Ready for production after hyperparameter tuning

## Why These Changes?
**XGBoost**: Handles non-linear relationships, built-in regularization, superior on tabular data
**Gradient Boosting**: Reduces bias/variance, better generalization, interpretable results

## How to Use
1. Install: `pip install xgboost`
2. Ensure datasets are in working directory
3. Run notebook cells sequentially
4. Review performance metrics

## Files Added
- XGBoost-Regressor.ipynb
- Gradient-Descent-Regressor.ipynb

## Checklist
- [x] Code follows conventions
- [x] Notebooks properly structured
- [x] Evaluation metrics implemented
- [x] Random seeds set for reproducibility
- [ ] Cross-validation for robust evaluation (future)
- [ ] SHAP values for interpretability (future)

**Status**: Ready for Review
