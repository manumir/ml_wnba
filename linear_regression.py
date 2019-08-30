import pandas as pd
import functions as f
from sklearn.linear_model import LinearRegression
import joblib

data=pd.read_csv('train.csv')
a=data.dropna()
a=a.drop(['Team_left','Match Up_left','Game Date_left','Team_right',
           'Match Up_right','Game Date_right','MIN_left','MIN_right',
           'W/L_left','W/L_right'],1)

train_dataset = a.sample(frac=0.9,random_state=2)
test_dataset = a.drop(train_dataset.index)

train_labels = train_dataset.pop('Result')
test_labels = test_dataset.pop('Result')

clf = LinearRegression(n_jobs=-1)
clf.fit(train_dataset,train_labels)
joblib.dump(clf,'uptodate_linear_regression1.joblib')

acc=clf.score(test_dataset,test_labels)
preds=clf.predict(test_dataset)
print(f.acc(preds,test_labels))

