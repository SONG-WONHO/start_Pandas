#load pandas as pd
import pandas as pd

#Raw data
data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p'], 'ReTest':['y','y','n','n','n']}

df = pd.DataFrame(data, columns=['score','PF','ReTest'])
'''
   score PF ReTest
0     10  f      y
1     20  f      y
2     30  p      n
3     40  p      n
4     40  p      n
'''

#columns
print(df['score'])
'''
0    10
1    20
2    30
3    40
4    40
Name: score, dtype: int64
'''

print(df.score)
'''
0    10
1    20
2    30
3    40
4    40
Name: score, dtype: int64
'''

print(df[['score', 'PF']])
'''
   score PF
0     10  f
1     20  f
2     30  p
3     40  p
4     40  p
'''

#rows
print(df[:])
'''
   score PF ReTest
0     10  f      y
1     20  f      y
2     30  p      n
3     40  p      n
4     40  p      n
'''

print(df[2:4])
'''
   score PF ReTest
2     30  p      n
3     40  p      n
'''

print(df[df['score']>30])
'''
   score PF ReTest
3     40  p      n
4     40  p      n
'''

'''
    .iloc : integer position
    .loc : label
    .ix : integer position & label, but if label is number than label-based index
'''

#load numpy as np
import numpy as np

example_series = pd.Series(np.nan, index=[49,48,47,46,45,1,2,3,4,5])
'''
49   NaN
48   NaN
47   NaN
46   NaN
45   NaN
1    NaN
2    NaN
3    NaN
4    NaN
5    NaN
dtype: float64
'''

#iloc
print(example_series.iloc[:3])
'''
49   NaN
48   NaN
47   NaN
dtype: float64
'''

#loc
print(example_series.loc[:3])
'''
49   NaN
48   NaN
47   NaN
46   NaN
45   NaN
1    NaN
2    NaN
3    NaN
dtype: float64
'''

#ix
#if it is only numbers, label-based index
example_series = pd.Series(np.nan, index=['c',48,47,46,45,1,2,3,4,5])

print(example_series.ix[:6])
'''
c    NaN
48   NaN
47   NaN
46   NaN
45   NaN
1    NaN
dtype: float64
'''

#apply data frame
print(df.ix[:,:])
'''
   score PF ReTest
0     10  f      y
1     20  f      y
2     30  p      n
3     40  p      n
4     40  p      n
'''

print(df.ix[1:2,:])
'''
   score PF ReTest
1     20  f      y
2     30  p      n  => because label-based index
'''

print(df.ix[:,1:2])
'''
  PF
0  f
1  f
2  p
3  p
4  p  => because integer-based index
'''

print(df.ix[:,['score','PF']])
'''
   score PF
0     10  f
1     20  f
2     30  p
3     40  p
4     40  p
'''

print(df.ix[2,'score'])
## 30