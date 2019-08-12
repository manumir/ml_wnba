import pandas as pd
import glob


files=['raw_2019.csv','raw_2018.csv','raw_2017.csv','raw_2016.csv','raw_2015.csv',
        'raw_2014.csv','raw_2013.csv','raw_2012.csv','raw_2011.csv','raw_2010.csv',
        'raw_2009.csv','raw_2008.csv','raw_2007.csv','raw_2006.csv','raw_2005.csv',
        'raw_2004.csv','raw_2003.csv','raw_2002.csv','raw_2001.csv','raw_2000.csv',
        'raw_1999.csv','raw_1998.csv','raw_1997.csv']

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

