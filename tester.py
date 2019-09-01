import pandas as pd
import functions as f

file=pd.read_csv('data.csv')
file=file.reset_index(drop=True)

left,right=f.append2for1(file)

left=left.reset_index(drop=True)
right=right.reset_index(drop=True)

a=left.join(right,rsuffix='_right')
a.to_csv('a.csv')

print(a['Match Up'])
print(a['Match Up_right'])

