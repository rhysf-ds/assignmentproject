import pandas as pd
import numpy as np
import random as rnd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

traindata = pd.read_csv("C:\\Users\\Franc\\PycharmProjects\\pythonProject\\titanic\\train.csv")
testdata = pd.read_csv("C:\\Users\\Franc\\PycharmProjects\\pythonProject\\titanic\\test.csv")

women = traindata.loc[traindata.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)
print(rate_women)

men = traindata.loc[traindata.Sex == 'male']["Survived"]
rate_men = sum(men) / men.count()
print(rate_men)

X_test = pd.get_dummies(testdata[features])
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X,y)
Out[29]: RandomForestClassifier(max_depth=5, random_state=1)
predictions = model.predict(X_test)
output = pd.DataFrame({'PassengerId':testdata.PassengerId, 'Survived':predictions})
print(output)