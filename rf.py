import pandas as pd
import functions as f
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv('train.csv')
a=data.dropna()
a=a.drop(['Team','Match Up','Game Date','Team_right',
           'Match Up_right','Game Date_right','MIN','MIN_right',
           'W/L','W/L_right'],1)

train_dataset = a.sample(frac=0.85,random_state=1)
test_dataset = a.drop(train_dataset.index)

train_labels = train_dataset.pop('Result')
test_labels = test_dataset.pop('Result')

clf = RandomForestClassifier(n_estimators=43, random_state=11,n_jobs=-1)
clf.fit(train_dataset,train_labels)

preds=clf.predict(test_dataset)

print(f.acc(preds,test_labels))

