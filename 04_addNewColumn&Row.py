#load pandas as pd
import pandas as pd

#Create a column
data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p'], 'ReTest':['y','y','n','n','n']}
df = pd.DataFrame(data, columns = ['score','PF','ReTest'])
'''
   score PF ReTest
0     10  f      y
1     20  f      y
2     30  p      n
3     40  p      n
4     40  p      n
'''

df['name'] = ['song','park','kim','hyun','jun']
print(df)
'''
   score PF ReTest  name
0     10  f      y  song
1     20  f      y  park
2     30  p      n   kim
3     40  p      n  hyun
4     40  p      n   jun
'''

df = df.assign(age = [20,18,22,23,24])
print(df)
'''
   score PF ReTest  name  age
0     10  f      y  song   20
1     20  f      y  park   18
2     30  p      n   kim   22
3     40  p      n  hyun   23
4     40  p      n   jun   24
'''

#Create a row
df.ix[5] = [50, 'p', 'n', 'ripple', '22']
print(df)
'''
   score PF ReTest    name age
0     10  f      y    song  20
1     20  f      y    park  18
2     30  p      n     kim  22
3     40  p      n    hyun  23
4     40  p      n     jun  24
5     50  p      n  ripple  22
'''

#Example_1
#load numpy as np
import numpy as np

data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p']}
df = pd.DataFrame(data, columns = ['score','PF'])
'''
   score PF
0     10  f
1     20  f
2     30  p
3     40  p
4     40  p
'''

df['ReTest'] = np.where(df['PF']=='f','True','False')
print(df)
'''
   score PF ReTest
0     10  f   True
1     20  f   True
2     30  p  False
3     40  p  False
4     40  p  False
'''

#Example_2

data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p']}
df = pd.DataFrame(data, columns = ['score','PF'])

grades = []

for row in data['score']:
    if row >= 40:
        grades.append('A')

    elif row >= 30:
        grades.append('B')

    elif row >= 20:
        grades.append('C')

    elif row >= 10:
        grades.append('D')

    else:
        grades.append('F')

df['grade'] = grades
print(df)
'''
   score PF grade
0     10  f     D
1     20  f     C
2     30  p     B
3     40  p     A
4     40  p     A
'''