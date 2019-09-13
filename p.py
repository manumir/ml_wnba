#/usr/bin/env python

import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import functions as f

a=pd.read_csv('train.csv')
a=a.dropna()

a=a.drop(['Team','Match Up','Game Date','Team_right',
          'Match Up_right','Game Date_right','MIN','MIN_right',
          'W/L','W/L_right'],1)

corr=a.corr()['Result']
del2=[]
for x in corr.index:
  if abs(corr[x]) < 0.1:
    del2.append(x)

a=a.drop(del2,1)

train_dataset = a.sample(frac=0.85,random_state=5)
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

print(len(train_dataset.keys()))

def build_model():
    model = keras.Sequential([
    layers.Dense(6, input_shape=[len(train_dataset.keys())],activation='sigmoid'),
    layers.Dense(6,activation='sigmoid'),
    layers.Dense(1,activation='sigmoid'),
  ])
    model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])
    return model

model = build_model()
early_stop = keras.callbacks.EarlyStopping(monitor='val_acc', patience=20)
history = model.fit(normed_train_data, train_labels,validation_split=0.2, epochs=500, callbacks=[early_stop])

print(model.evaluate(normed_test_data,test_labels)[1])
test_predictions = model.predict(normed_test_data)

#model.save('1.h5')
