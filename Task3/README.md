# Task 3 

## Description
Here it is demonstrated how to train a simple ML model. The dataset (derived from satellite image processing) is in the /data folder. 

This is a classification problem and here are the steps:

- The training data is divided into three datasets: training dataset, testing dataset, and validation dataset. 
- The performance is displayed after training (confusion matrix, classification report, etc.).
- Develop the model training script and save the model as a .joblib file.

Models used: XGBoost and RandomForest

## Requirements
- `pandas`
- `xgboost`
- `scikit-learn`
- `joblib`

## Result 

The notebooks show some simplle EDA, Comparison of Random Fores and XGBoost models, training and hyperparameter tuning as well as evaluation techniques like cross-validation. 

The script implements the **XGBoost** model, with randomized hyperparameter search shows it's performance and saves the model as .joblib file.