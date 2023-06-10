# AV-V

This project involves the implementation of 10 machine learning models and 1 statistical analysis technique to predict the steady state starts for a benchmark fork. 

## Structuring the data

The data is initially given in JSON. For ease of model training the data from JSON is converted to CSV using the [file] (https://github.com/smilieSushmitha/AV-V/blob/main/convertJsonToCSV.py)

## Analysis for data reduction
By using binning method it is found that the data is skewed. This analysis is done in this [file] (https://github.com/smilieSushmitha/AV-V/blob/main/data_distribution_analysis.ipynb). Based on the results the data set is reduced.

## Hyper parameter tuning
All algoritms are experimented with various hyperparameters. The best performing hyperparameters are chosen for implementing in machine learning algorithms

## Algorithms
1. Linear
2. Lasso
3. Ridge
4. Softmax
5. Decision tree
6. Random forest
7. K nearest neighbors (KNN) Regression
8. Gausian
9. Neural network
10. Convolutional neural network (CNN)


## Implementing machine learning algorithms
1. [Full dataset default settings]  (https://github.com/smilieSushmitha/AV-V/blob/main/AV_V_Regression.ipynb)
2. [Full dataset hyperparamer tuning] (https://github.com/smilieSushmitha/AV-V/blob/main/AV_V_Regression_parameter_tuned_full.ipynb)
3. [Reduced dataset default setting] (https://github.com/smilieSushmitha/AV-V/blob/main/AV_V_Regression_reduced_data_set.ipynb)
4. [Reduced dataset hyperparamer tuning] (https://github.com/smilieSushmitha/AV-V/blob/main/AV_V_Regression_tuned_reduced.ipynb)
