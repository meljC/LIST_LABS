import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
import joblib

# Load dataset
file_path = '../data/training_data.csv'
data = pd.read_csv(file_path)

# Features and target
X = data.drop('Class', axis=1)
y = data['Class']

# Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, stratify=y, random_state=1)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, stratify=y, random_state=1)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, stratify=y_temp, random_state=1)

# Initialize XGBoost model with hyperparameter tuning
param_dist = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.01, 0.1, 0.3],
    'max_depth': [3, 5, 7],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0],
    'min_child_weight': [1, 3, 5]
}

xgb = XGBClassifier(eval_metric='mlogloss')

# RandomizedSearchCV with 5-fold stratified cross-validation
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
grid_search = RandomizedSearchCV(xgb, param_distributions=param_dist, n_iter=10, scoring='accuracy', cv=kfold, n_jobs=-1, verbose=1)

# Fit the model
grid_search.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)

# Best hyperparameters
print("Best Hyperparameters:", grid_search.best_params_)

# Evaluate the model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_val)
y_prob = best_model.predict_proba(X_val)
# Evaluation Metrics
print(f"Accuracy: {accuracy_score(y_val, y_pred):.4f}")
print("Confusion Matrix:\n", confusion_matrix(y_val, y_pred))
print("Classification Report:\n", classification_report(y_val, y_pred))
print(f"ROC AUC: {roc_auc_score(y_val, y_prob, multi_class='ovr'):.4f}")


print("\n----------------------")
print("Evaluate on Test data")
y_pred = best_model.predict(X_test)
y_prob = best_model.predict_proba(X_test)
# Evaluation Metrics
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print(f"ROC AUC: {roc_auc_score(y_test, y_prob, multi_class='ovr'):.4f}")

# Save the model
model_path = 'xgboost_optimized.joblib'
joblib.dump(best_model, model_path)
print(f"Model saved to {model_path}")

# Load and use the saved model
# loaded_model = joblib.load('xgboost_optimized.joblib')
# y_pred_loaded = loaded_model.predict(X_val)
# print("Loaded model")
