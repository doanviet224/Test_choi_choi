import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import sklearn as sk

# Importing the dataset
df = pd.read_csv('Diabetes_Diagnosis.csv')


X = df.drop('Diabetes', axis=1)  # thay bằng tên cột nhãn thật sự nếu khác
y = df['Diabetes']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)

print(y_pred)
