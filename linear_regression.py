import pandas as pd
import functions as f
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import joblib

data=pd.read_csv('train.csv')
a=data.dropna()
a=a.drop(['Team','Match Up','Game Date','Team_right',
           'Match Up_right','Game Date_right','MIN','MIN_right',
           'W/L','W/L_right'],1)

train_dataset = a.sample(frac=0.9,random_state=10)
test_dataset = a.drop(train_dataset.index)

train_labels = train_dataset.pop('Result')
test_labels = test_dataset.pop('Result')

clf = LinearRegression(n_jobs=-1)

#train_dataset=preprocessing.normalize(train_dataset)
#test_dataset=preprocessing.normalize(test_dataset)

clf.fit(train_dataset,train_labels)
joblib.dump(clf,'Linear_regression.joblib')

acc=clf.score(test_dataset,test_labels)
preds=clf.predict(test_dataset)
print(f.acc(preds,test_labels))

ones,zeros=0,0
for pred in preds:
  if round(pred)==1:
    ones+=1
  else:
    zeros+=1

print('lenght of test:',len(preds))
print('0s:',zeros/len(preds))
print('1s:',ones/len(preds))

