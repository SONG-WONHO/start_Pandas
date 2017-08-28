#load pandas as pd
import pandas as pd

#raw data
raw_data = {'name':['a','b','c','d','e'],
            'age':[20,21,22,20,19],
            'finalScore':[90,80,85,88,95],
            'quizScore':[5,5,4,3,5]}

df = pd.DataFrame(raw_data, columns= ['name','age','finalScore','quizScore'])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
4    e   19          95          5
'''

#example_1
print(df[(df['finalScore'] > 85) & (df['quizScore'] > 3)])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
4    e   19          95          5
'''

#example_2
print(df[df['name'].isin(['a','d'])])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
3    d   20          88          3
'''

print(df[~df['name'].isin(['a','d'])])
'''
  name  age  finalScore  quizScore
1    b   21          80          5
2    c   22          85          4
4    e   19          95          5
'''

#example_3
print(df[df['name'].map(lambda name : 'd' in name)])
'''
  name  age  finalScore  quizScore
3    d   20          88          3
'''

#example_4
print(df['name'].where(df['finalScore'] > 90))
'''
0    NaN
1    NaN
2    NaN
3    NaN
4      e
Name: name, dtype: object
'''

