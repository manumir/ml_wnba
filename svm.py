#! /usr/bin/python3

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from joblib import dump, load
from sklearn.metrics import accuracy_score

data=pd.read_csv('train.csv')
data=data.dropna()

col2drop=['Team_left','Match Up_left','Game Date_left','W/L_left','MIN_left','Team_right','Match Up_right','Game Date_right','W/L_right','MIN_right']

#x=data.drop(col2drop,1)
x=data[['PTS', 'FGM', 'FG%', '3PM',
       '3P%', 'FT%', 'DREB', 'REB', 'AST', 'BLK',
       'TOV', 'PF', '+/-', 'winrate 30',
       'PTS_right', 'FGM_right', 'FG%_right', '3PM_right', '3P%_right',
       'FTM_right', 'DREB_right', 'REB_right', 'AST_right', 'STL_right',
       'BLK_right', 'TOV_right', '+/-_right', 'winrate 30_right',
       'Result','Location']]

y=x.pop('Result')

clf = load('svc_linear.joblib')
predictions=clf.predict(x)

print(accuracy_score(y,predictions))

