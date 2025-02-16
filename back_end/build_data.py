import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
data = pd.read_csv('/home/vuvanhoc/Documents/Project/project_diabetes/dataset/diabetes.csv')
from joblib import dump, load
from sklearn.preprocessing import StandardScaler


res = data.corr()
# sns.heatmap(res, annot=True, fmt=".2f")
# plt.show()
    # res1 = data['Outcome'].value_counts()
    # plt.figure(figsize = (10,10))
    #
    # sns.histplot(data['Outcome'])
x = data.drop(['Outcome'], axis=1)
y = data['Outcome']
    # Pregnancies
Xtrain, Xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42, shuffle=True)

scaler = StandardScaler()
Xtrain = scaler.fit_transform(Xtrain)
Xtest = scaler.transform(Xtest)
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

param = {
        "n_estimators": [50, 100, 200],
        "criterion": ["gini", "entropy"],
    }
cls = RandomForestClassifier()
model = GridSearchCV(cls, param_grid=param, verbose=2, n_jobs=3, cv=4, scoring='recall')
model.fit(Xtrain, ytrain)
best_params = model.best_params_
best_score = model.best_score_
print(best_params)
print(best_score)

cls = RandomForestClassifier(**best_params)
cls.fit(Xtrain, ytrain)
y_pred = cls.predict(Xtest)
dump(cls, "../model/model.joblib")
dump(scaler, "../model/scaler.joblib")
print(classification_report(ytest, y_pred))
