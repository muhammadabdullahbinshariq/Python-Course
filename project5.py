# Project 5. Date : 24 / 10 / 26. Topic : Regression Analysis

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y = True)

diabetes_X = diabetes_X[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_predict = regr.predict(diabetes_X_test)

print("Coefficients : \n", regr.coef_)
print("Mean squared error :%.2f")
print("Coeffiicent of determination: %.2f")

plt.scatter(diabetes_X_test, diabetes_y_test, color = "black")
plt.plot(diabetes_X_test, diabetes_y_predict, color = "blue", linewidth = 3)

plt.xticks(())
plt.yticks(())

plt.show