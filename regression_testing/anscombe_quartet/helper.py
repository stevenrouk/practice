"""Helper functions for exploring the Anscombe dataset."""

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def split_df_into_xy_dataset(df, dataset_label):
    return df[df['dataset']==dataset_label]['x'], df[df['dataset']==dataset_label]['y']

def compute_univariate_stats(arr):
    arr_mean = round(np.mean(arr), 2)
    arr_std = round(np.std(arr), 2)

    return {'mean': arr_mean, 'standard deviation': arr_std}

def compute_bivariate_stats(x, y):
    correlation = round(np.corrcoef(x, y)[0, 1], 2)
    covariance = round(np.cov(x, y)[1, 0], 2)

    return {'correlation': correlation, 'covariance': covariance}

def compute_linear_model_stats(x, y):
    fit_model = sm.OLS(y, x).fit()
    r2 = round(fit_model.rsquared, 2)
    x_param = round(fit_model.params['x'], 2)
    mse = round(fit_model.mse_resid, 2)
    bic = round(fit_model.bic, 1)

    return {
        'r_squared': r2,
        'x_param': x_param,
        'mse': mse,
        'bic': bic
    }

def calculate_cv_rmse(x, y):
    x1_vals = x.values.reshape(-1, 1)
    y1_vals = y.values.reshape(-1, 1)

    rmse = np.sqrt(np.mean(-1 * cross_val_score(
        LinearRegression(),
        x1_vals,
        y1_vals,
        cv=3,
        scoring='neg_mean_squared_error'
    )))

    return round(rmse, 2)

def run_regression_trials(x, y):
    x = x.values.reshape(-1, 1)
    y = y.values.reshape(-1, 1)
    models = []
    mse_vals = []
    r2_vals = []
    for _ in range(50):
        x_train, x_test, y_train, y_test = train_test_split(x, y)
        model = LinearRegression()
        model.fit(x_train, y_train)
        models.append(model)
        y_test_pred = model.predict(x_test)
        mse_vals.append(mean_squared_error(y_test, y_test_pred))
        r2_vals.append(r2_score(y_test, y_test_pred))
    
    return models, mse_vals, r2_vals

def plot_regression_trials(x, y, models, name, ax=None):
    if ax:
        pass
    else:
        fig, ax = plt.subplots()
    ax.set_title(name, fontsize=20)
    ax.scatter(x, y)
    for model in models:
        m = model.coef_[0, 0]
        b = model.intercept_[0]
        ax.plot(x, m*x + b, color='red', alpha=0.05)

def compute_mean_and_95_quantiles(arr):
    arr_mean = round(np.mean(arr), 2)
    confidence_interval = np.quantile(arr, [0.025, 0.975])
    confidence_interval = [round(x, 2) for x in confidence_interval]
    
    return {'mean': arr_mean, '95% confidence interval': confidence_interval}