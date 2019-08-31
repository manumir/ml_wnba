import numpy as np

# create a data frame of games before a certain date
def get_past_games(df,data1,team,amount):
  ixs=[]
  rows=df.loc[df['Team'] == team]
  dates=rows['Game Date']
  for ix in dates.index:
    value=df.at[ix,'Game Date']
    if datecomp(value,data1)==value:
        ixs.append(ix)
  return ixs[:amount]

#averages for each column 
def get_avgs(df,column):
  count=0
  try:
    for x in df[column].values:
      count+=int(x)
    avg=float(count/len(df[column].values))
    return avg
  except Exception as e:
    print(e)
    return np.nan

def create_winrate(df,amount):
  try:
    df=df[-(amount):]
    b=0
    for x in df['W/L'].values:
      if x == 'W':
        b+=1
    return float(b/amount)
  except:
    return np.nan

def result(df):
    results=[]
    for value in df['W/L_right'].values:
        if value=='L':
            results.append(0)
        else:
            results.append(1)
    return results

def location(df):
    locations=[]
    for value in df['Match Up_right'].values:
        if value[4]=='v':
            locations.append(0)
        else:
            locations.append(1)
    return locations

def append2for1(data):
  data=data.reset_index()
  b=[]
  it=list(range(data.shape[0]))
  for ix in it:
    name=data.at[ix,'Match Up'][-3:]
    date=data.at[ix,'Game Date']
    a=data.loc[data['Game Date']==date]
    a=a.loc[data['Team']==name]
    it.remove(ix)
    try:
      b.append(a.index[0])
    except:
      continue
  return b
  
#create a function to determine if a date is sooner than another date
def datecomp(date1,date2):
    if date1[6:len(date1)]>date2[6:len(date2)]:
        #print("date1's year is later than date2's year")
        return date2
    if date1[6:len(date1)]<date2[6:len(date2)]:
        #print("date2's year is later than date1's year")
        return date1
    
    if date1[6:len(date1)]==date2[6:len(date2)]:
        if date1[0:2]>date2[0:2]:
            #print("date1's month is later than date2's month")
            return date2
    if date1[6:len(date1)]==date2[6:len(date2)]:
        if date1[0:2]<date2[0:2]:
            #print("date2's month is later than date1's month")
            return date1
        
    if date1[6:len(date1)]==date2[6:len(date2)]:
        if date1[0:2]>date2[0:2]:
            if date1[3:5]==date2[3:5]:
                #print("date1's day is later than date2's day")
                return date2
    if date1[6:len(date1)]==date2[6:len(date2)]:
        if date1[0:2]<date2[0:2]:
            if date1[3:5]==date2[3:5]:
                #print("date2's day is later than date1's day")
                return date1
            
    if date1[6:len(date1)]==date2[6:len(date2)]:
        if date1[0:2]==date2[0:2]:
            if date1[3:5]==date2[3:5]:
                return 0

def acc(true_y,pred_y):
  true_y=list(true_y)
  pred_y=list(pred_y)
  count=0 
  for x in range(len(true_y)):
    if round(pred_y[x])==round(true_y[x]):
      count=count+1
  return count/len(true_y)

