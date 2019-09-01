import numpy as np
import pandas as pd
import functions as f

data=pd.read_csv('raw.csv')
#data=data.dropna()
data.pop('Unnamed: 24')
data=data.astype('object')
#data=data[:1000]

c2_avg=['PTS', 'FGM', 'FGA','FG%', '3PM', '3PA', '3P%',
        'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB',
        'AST', 'TOV', 'STL', 'BLK', 'PF', '+/-']

for ix in range(len(data)):
  print(ix)
  data1=data.loc[ix,'Game Date']
  team=data.loc[ix,'Team']
  ixs=f.get_past_games(data,data1,team,30)
  past=data.loc[ixs]
  data.at[ix,'winrate 30']=f.create_winrate(past,30)
  data.at[ix,'winrate 6']=f.create_winrate(past,6)
  
  for c in c2_avg:
    data.at[ix,c]=f.get_avgs(past,c)

data.to_csv('data.csv',index=False)

b=f.append2for1(data)
b=b.dropna()
b['Result']=f.result(b)
b['Location']=f.location(b)

b.to_csv('train.csv',index=False)

