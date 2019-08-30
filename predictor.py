#import tensorflow as tf
import pandas as pd
import joblib
data=pd.read_csv('data.csv')

c2_avg=['PTS', 'FGM', 'FGA','FG%', '3PM', '3PA', '3P%',
        'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB',
        'AST', 'TOV', 'STL', 'BLK', 'PF', '+/-','winrate 30','winrate 6']

home=data.loc[data['Team']=='LVA'][:1]
away=data.loc[data['Team']=='PHO'][:1]

home=home.reset_index(drop=True)
away=away.reset_index(drop=True)

home=home[c2_avg]
away=away[c2_avg]

b=home.join(away,lsuffix='_left',rsuffix='_right')

b['Location']=0

print(b)

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
normed_b= norm(b)

#model=tf.keras.models.load_model('1.h5')
#model=joblib.load('11%.joblib')
model=joblib.load('uptodate_linear_regression.joblib')
print(model.predict(b))


