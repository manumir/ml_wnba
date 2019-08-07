import pandas as pd
import glob


files=['raw_2019.csv','raw_2018.csv']

lines=['Team,Match Up,Game Date,W/L,MIN,PTS,FGM,FGA,FG%,3PM,3PA,3P%,FTM,FTA,FT%,OREB,DREB,REB,AST,TOV,STL,BLK,PF,+/-,\n']
for name in files:
  print(name)
  file=open(name,'r')
  lines+=file.readlines()
  file.close()

file=open('raw.csv','w')
for line in lines:
  file.write(line)
file.close()

