import pandas as pd
from sklearn import preprocessing
import joblib
data=pd.read_csv('data.csv')

c2_avg=['PTS', 'FGM', 'FGA','FG%', '3PM', '3PA', '3P%',
        'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB',
        'AST', 'TOV', 'STL', 'BLK', 'PF', '+/-','winrate 30','winrate 6']

c2_avg1=['FG%','+/-','winrate 30','winrate 6','+/-_right',
         'winrate 30_right','Location']

home=data.loc[data['Team']==str(input('home: '))][:1]
away=data.loc[data['Team']==str(input('away: '))][:1]

home=home.reset_index(drop=True)
away=away.reset_index(drop=True)

home= home[c2_avg]
away= away[c2_avg]

b=home.join(away,rsuffix='_right')
b['Location']=0

b=b[c2_avg1]
print(b)

#b=preprocessing.normalize(b)

#model=tf.keras.models.load_model('1.h5')
model=joblib.load('Linear_regression.joblib')
print(model.predict(b))



