import pandas as pd
import functions as f

file=pd.read_csv('data.csv')
file=file.reset_index()

b=f.append2for1(file)
a=list(range(len(file)))

for i in a:
  if i in b:
    a.remove(i)

print(len(a),len(b))

