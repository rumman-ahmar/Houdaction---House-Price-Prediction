# Houdaction: House-Price-Prediction

A Machine Learning web application with the model accuracy of `87%` to predict the home prices of several Indian cities. APIs are written in FastAPI and whereas the frontend uses the Vanilla JavaScript. The video demonstration can be seen here: https://www.linkedin.com/posts/rummanahmar_datascience-machinelearning-regression-activity-7037108005993140224-gmgV?utm_source=share&utm_medium=member_desktop


# Project file explanation
- main.py: It contains the APIs that are written in FastAPI
- regression.py: It has the machine learning part
- static directory: It has the static file i.e. JavaScript and script.js holds all the JavaScript code
- templates directory: It has the HTML file and index.html is the only and main file of for the frontend

# Machine Learning model selection
During the training and testing I found KNeighborsRegressor has the best score amongs all the Regression model so that's why I choosed it and it also avaiable in the repository with the name `knr_model`
