import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data=pd.read_csv('train.csv')
a=data.dropna()
a=a.drop(['Team_left','Match Up_left','Game Date_left','Team_right',
           'Match Up_right','Game Date_right','MIN_left','MIN_right',
           'W/L_left','W/L_right'],1)

train_dataset = a.sample(frac=0.85,random_state=2)
test_dataset = a.drop(train_dataset.index)

train_stats =train_dataset.describe()
train_stats.pop('Result')
train_stats = train_stats.transpose()

train_labels = train_dataset.pop('Result')
test_labels = test_dataset.pop('Result')

def norm(x):
  return (x - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

clf = LinearRegression(n_jobs=-1)
clf.fit(normed_train_data,train_labels)
joblib.dump(clf,'11%.joblib')

preds=clf.predict(normed_test_data)
print(preds)

acc=clf.score(normed_test_data,test_labels)
print(acc)

