from joblib import load
from build_data import Xtest, ytest
from sklearn.metrics import classification_report

model = load('../model/model.joblib')

ypre = model.predict(Xtest)

print(classification_report(ytest, ypre))