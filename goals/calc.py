log=open('log1.txt','r')
lines=log.readlines()

# 1 for placard, 5 for first model, 9 for model47
times=['placard',1,'model 70',5]

def calc_total(x):#,model):

  r_lines=[]
  while x<len(lines):
    r_lines.append(lines[x])
    x=x+8
  
  right=0
  count=0
  for line in r_lines:
    right=right + int(line[0:2])
    count=count + int(line[9:11])

  print('right:{}\ntotal:{}\n{}\n'.format(right,count,right/count*100))

for i in times:
  if isinstance(i,str)==False:
    calc_total(i)
  else:
    print(i)
