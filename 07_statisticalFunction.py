#load pandas as pd
import pandas as pd

#raw data
raw_data = {'name':['a','b','c','d','e'],
            'age':[20,21,22,20,19],
            'finalScore':[90,80,85,88,95],
            'quizScore':[5,5,4,3,5]}

df = pd.DataFrame(raw_data, columns= ['name', 'age', 'finalScore', 'quizScore'])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
4    e   19          95          5
'''

#Sum
print(df['age'].sum()) ## 102

#Mean
print(df['age'].mean()) ## 20.4

#Cumulative sum
print(df['age'].cumsum())
'''
0     20
1     41
2     63
3     83
4    102
Name: age, dtype: int64
'''

#Count
print(df['age'].count()) ## 5

#Minimum
print(df['age'].min()) ## 19

#Maximum
print(df['age'].max()) ## 22

#Variance
print(df['age'].var()) ## 1.3

#Standard deviation
print(df['age'].std()) ## 1.1401754251

#Describe
print(df.describe())
'''
             age  finalScore  quizScore
count   5.000000     5.00000   5.000000
mean   20.400000    87.60000   4.400000
std     1.140175     5.59464   0.894427
min    19.000000    80.00000   3.000000
25%    20.000000    85.00000   4.000000
50%    20.000000    88.00000   5.000000
75%    21.000000    90.00000   5.000000
max    22.000000    95.00000   5.000000
'''