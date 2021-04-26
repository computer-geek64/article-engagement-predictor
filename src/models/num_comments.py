#!/usr/bin/python3
# num_comments.py

import optuna
import xgboost
from sklearn import model_selection


def xgb_objective(trial, X, y, estimator):
    n_estimators = trial.suggest_int('n_estimators', 40, 280, 40)
    max_depth = trial.suggest_int('max_depth', 2, 12, 2)
    learning_rate = trial.suggest_loguniform('learning_rate', 0.001, 0.1)
    params = {
        'n_estimators': n_estimators,
        'max_depth': max_depth,
        'learning_rate': learning_rate
    }
    estimator.set_params(**params)
    accuracy = model_selection.cross_val_score(estimator, X, y).mean()

    # Try without this and use if accuracy is negative
    '''
    if accuracy < 0: 
        accuracy = model_selection.cross_val_score(estimator, X, y, scoring='neg_mean_squared_error').mean()
        return accuracy
    '''
    return accuracy


def optimize(estimator, X_train, X_val, y_train, y_val):
    estimator.fit(X_train, y_train)
    study = optuna.create_study(direction='maximize')  # maximize or minimize?
    study.optimize(lambda trial: xgb_objective(trial, X_val, y_val, estimator))
    estimator.set_params(**study.best_params)


def generate_and_evaluate_model(data, optimize=False):
    X = data.drop(labels='num comments', axis=1)  # change this with actual col name
    y = data['num comments']  # change this with actual col name

    # 70% train, 15% val, 15% test
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.15)
    X_train, X_val, y_train, y_val = model_selection.train_test_split(X_train, y_train, test_size=(0.15/0.85))

    if optimize:
        model = xgboost.XGBRegressor()
        optimize(model, X_train, X_val, y_train, y_val)
    else:
        model = xgboost.XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.01)
        model.fit(X_train, y_train)
    accuracy = model_selection.cross_val_score(model, X_test, y_test)
    return model, accuracy


model, accuracy = generate_and_evaluate_model()
print(accuracy)
print(model.get_params())