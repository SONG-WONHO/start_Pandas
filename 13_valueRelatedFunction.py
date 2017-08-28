#load pandas as pd
import pandas as pd

'''
    -Replace values
    -Rank values
    -Count values
    -Cut values
    -Unique values
    -Extension values
'''

#raw data
raw_data = {'name': ['a', 'b', 'c', 'd', 'e'],
            'age': [20, 21, 22, 20, 19],
            'finalScore': [90, 80, 85, 88, 95],
            'quizScore': [5, 5, 4, 3, 5],
            'preTestScore': [80,-1,-1,-1,100]}

df = pd.DataFrame(raw_data, columns= ['name','age','finalScore','quizScore','preTestScore'])
print(df)
'''
  name  age  finalScore  quizScore  preTestScore
0    a   20          90          5            80
1    b   21          80          5            -1
2    c   22          85          4            -1
3    d   20          88          3            -1
4    e   19          95          5           100
'''

#Replace value
print(df['preTestScore'].replace(-1,999))
'''
0     80
1    999
2    999
3    999
4    100
Name: preTestScore, dtype: int64
'''

#Rank value
print(df['finalScore'].rank(ascending=False))
'''
0    2.0
1    5.0
2    4.0
3    3.0
4    1.0
Name: finalScore, dtype: float64
'''

#Count value
print(pd.value_counts(df['quizScore']))
'''
5    3
4    1
3    1
Name: quizScore, dtype: int64
'''

print(df.drop(['name'], axis=1).apply(pd.value_counts).fillna('*'))
'''
     age finalScore quizScore preTestScore
-1     *          *         *            3
 3     *          *         1            *
 4     *          *         1            *
 5     *          *         3            *
 19    1          *         *            *
 20    2          *         *            *
 21    1          *         *            *
 22    1          *         *            *
 80    *          1         *            1
 85    *          1         *            *
 88    *          1         *            *
 90    *          1         *            *
 95    *          1         *            *
 100   *          *         *            1
'''

#Cut value
bins = [0,85,90,95,100]
grade = ['D','C','B','A']
print(pd.cut(df['finalScore'],bins,labels=grade))
'''
0    C
1    D
2    D
3    C
4    B
Name: finalScore, dtype: category
Categories (4, object): [D < C < B < A]
'''

#Find unique value
#method_1
print(df['quizScore'].unique()) ## [5 4 3]
print(type(df['quizScore'].unique())) ## <class 'numpy.ndarray'>

#method_2
print(list(set(df['quizScore']))) ## [3, 4, 5]
print(type(list(set(df['quizScore'])))) ## <class 'list'>

#Find largest value`s index
print(df['finalScore'].idxmax()) ## 4

#Map external values
name_to_nickname = {'a': 'angel',
                    'b': 'bear',
                    'c': 'coil',
                    'd': 'dynamic',
                    'e': 'elephant'}

print(df['name'].map(name_to_nickname))
'''
0       angel
1        bear
2        coil
3     dynamic
4    elephant
Name: name, dtype: object
'''

