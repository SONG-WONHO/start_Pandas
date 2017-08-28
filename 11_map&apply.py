# load pandas as pd
import pandas as pd

# raw data
raw_data = {'name': ['a', 'b', 'c', 'd', 'e'],
            'age': [20, 21, 22, 20, 19],
            'finalScore': [90, 80, 85, 88, 95],
            'quizScore': [5, 5, 4, 3, 5]}

df = pd.DataFrame(raw_data, columns=['name', 'age', 'finalScore', 'quizScore'])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
4    e   19          95          5
'''

# apply() can apply a function along any axis of the dataframe
print(df['name'].apply(lambda name: name.upper()))
'''
0    A
1    B
2    C
3    D
4    E
Name: name, dtype: object
'''

# map() applies an operation over each element of a series
print(df['name'].map(str.upper))
'''
0    A
1    B
2    C
3    D
4    E
Name: name, dtype: object
'''

# applymap() applies a function to every single element in the entire dataframe
df = df.drop(['name'], axis=1)
'''
   age  finalScore  quizScore
0   20          90          5
1   21          80          5
2   22          85          4
3   20          88          3
4   19          95          5
'''

print(df.applymap(lambda x: x ** 2))
'''
   age  finalScore  quizScore
0  400        8100         25
1  441        6400         25
2  484        7225         16
3  400        7744          9
4  361        9025         25
'''

# example_1
df = pd.DataFrame(raw_data, columns=['name', 'age', 'finalScore', 'quizScore'])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
4    e   19          95          5
'''


def set_grade(in_score):
    score = in_score[0] + in_score[1]
    if score > 95:
        return 'A'
    elif score > 90:
        return 'B'
    elif score > 85:
        return 'C'
    else:
        return 'D'

df['grade'] = list(map(set_grade, zip(df['finalScore'],df['quizScore'])))
print(df)
'''
  name  age  finalScore  quizScore grade
0    a   20          90          5     B
1    b   21          80          5     D
2    c   22          85          4     C
3    d   20          88          3     B
4    e   19          95          5     A
'''

#example_2
df = pd.DataFrame(raw_data, columns=['name', 'age', 'finalScore', 'quizScore'])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
4    e   19          95          5
'''


def set_grade(score):
    if score > 95:
        return 'A'
    elif score > 90:
        return 'B'
    elif score > 85:
        return 'C'
    else:
        return 'D'

df['score'] = df['finalScore'] + df['quizScore']
'''
  name  age  finalScore  quizScore  score
0    a   20          90          5     95
1    b   21          80          5     85
2    c   22          85          4     89
3    d   20          88          3     91
4    e   19          95          5    100
'''

df['grade'] = df['score'].map(set_grade)
'''
  name  age  finalScore  quizScore  score grade
0    a   20          90          5     95     B
1    b   21          80          5     85     D
2    c   22          85          4     89     C
3    d   20          88          3     91     B
4    e   19          95          5    100     A
'''

print(df.drop(['score'],axis= 1))
'''
  name  age  finalScore  quizScore grade
0    a   20          90          5     B
1    b   21          80          5     D
2    c   22          85          4     C
3    d   20          88          3     B
4    e   19          95          5     A
'''

#example_4
df = pd.DataFrame(raw_data, columns=['name', 'age', 'finalScore', 'quizScore'])
'''
  name  age  finalScore  quizScore
0    a   20          90          5
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
4    e   19          95          5
'''

df.columns = map(str.upper, df.columns)
print(df)
'''
  NAME  AGE  FINALSCORE  QUIZSCORE
0    a   20          90          5
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
4    e   19          95          5
'''