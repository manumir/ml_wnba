import pandas as pd
import functions as f

file=pd.read_csv('data.csv')

b=f.append2for1(file)

print(len(b))
