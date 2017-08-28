import pandas as pd
import numpy as np

#raw data
raw_data = {'name':['a','b','c','d','e'],
            'age':[20,21,np.nan,np.nan,19],
            'finalScore':[90,80,85,np.nan,95],
            'quizScore':[np.nan,5,4,3,5]}

#example_1
df = pd.DataFrame(raw_data, columns= ['name','age','finalScore','quizScore'])
'''
  name   age  finalScore  quizScore
0    a  20.0        90.0        NaN
1    b  21.0        80.0        5.0
2    c   NaN        85.0        4.0
3    d   NaN         NaN        3.0
4    e  19.0        95.0        5.0
'''

#example_2
df_no_null = df.dropna()
print(df_no_null)
'''
  name   age  finalScore  quizScore
1    b  21.0        80.0        5.0
4    e  19.0        95.0        5.0
'''

#example_3
df.ix[5] = np.nan
'''
  name   age  finalScore  quizScore
0    a  20.0        90.0        NaN
1    b  21.0        80.0        5.0
2    c   NaN        85.0        4.0
3    d   NaN         NaN        3.0
4    e  19.0        95.0        5.0
5  NaN   NaN         NaN        NaN
'''

#example_4
df_no_null = df.dropna(how='all')
print(df_no_null)
'''
  name   age  finalScore  quizScore
0    a  20.0        90.0        NaN
1    b  21.0        80.0        5.0
2    c   NaN        85.0        4.0
3    d   NaN         NaN        3.0
4    e  19.0        95.0        5.0
'''

#example_5
df['temp'] = np.nan
print(df)
'''
  name   age  finalScore  quizScore  temp
0    a  20.0        90.0        NaN   NaN
1    b  21.0        80.0        5.0   NaN
2    c   NaN        85.0        4.0   NaN
3    d   NaN         NaN        3.0   NaN
4    e  19.0        95.0        5.0   NaN
5  NaN   NaN         NaN        NaN   NaN
'''

#example_6
df_no_null = df.dropna(how= 'all', axis=1)
print(df_no_null)
'''
  name   age  finalScore  quizScore
0    a  20.0        90.0        NaN
1    b  21.0        80.0        5.0
2    c   NaN        85.0        4.0
3    d   NaN         NaN        3.0
4    e  19.0        95.0        5.0
5  NaN   NaN         NaN        NaN
'''

#example_7
print(df.fillna('*'))
'''
  name age finalScore quizScore temp
0    a  20         90         *    *
1    b  21         80         5    *
2    c   *         85         4    *
3    d   *          *         3    *
4    e  19         95         5    *
5    *   *          *         *    *
'''

#example_8
df['quizScore'].fillna(df['quizScore'].mean(), inplace=True)
print(df)
'''
  name   age  finalScore  quizScore  temp
0    a  20.0        90.0       4.25   NaN
1    b  21.0        80.0       5.00   NaN
2    c   NaN        85.0       4.00   NaN
3    d   NaN         NaN       3.00   NaN
4    e  19.0        95.0       5.00   NaN
5  NaN   NaN         NaN       4.25   NaN
'''

#example_9
#Have to know groupby
df["finalScore"].fillna(df.groupby("quizScore")["finalScore"].transform("mean"), inplace=True)
print(df)
'''
  name   age  finalScore  quizScore  temp
0    a  20.0        90.0       4.25   NaN
1    b  21.0        80.0       5.00   NaN
2    c   NaN        85.0       4.00   NaN
3    d   NaN         NaN       3.00   NaN
4    e  19.0        95.0       5.00   NaN
5  NaN   NaN        90.0       4.25   NaN
'''

#example_10
#Same result
df["finalScore"].fillna(df['finalScore'].groupby(df['quizScore']).transform("mean"), inplace=True)
'''
  name   age  finalScore  quizScore  temp
0    a  20.0        90.0       4.25   NaN
1    b  21.0        80.0       5.00   NaN
2    c   NaN        85.0       4.00   NaN
3    d   NaN         NaN       3.00   NaN
4    e  19.0        95.0       5.00   NaN
5  NaN   NaN        90.0       4.25   NaN
'''
