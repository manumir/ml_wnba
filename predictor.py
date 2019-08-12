import tensorflow as tf
import pandas as pd

data=pd.read_csv('data.csv')

c2_avg=['PTS', 'FGM', 'FGA','FG%', '3PM', '3PA', '3P%',
        'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB',
        'AST', 'TOV', 'STL', 'BLK', 'PF', '+/-','winrate 50','winrate 7']

home=data.loc[data['Team']=='NYL'][:1]

away=data.loc[data['Team']=='SEA'][:1]

home=home.reset_index(drop=True)
away=away.reset_index(drop=True)

home=home[c2_avg]
away=away[c2_avg]

b=home.join(away,lsuffix='_left',rsuffix='_right')

b['Location']=0

print(b)

model=tf.keras.models.load_model('1.h5')

print(model.predict(b))


