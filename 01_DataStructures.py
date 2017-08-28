#load pandas as pd
import pandas as pd

'''
Pandas Data Structure
    -Series : 1 dimension
    -DataFrame : 2 dimension
'''

#Series
score = [10, 20, 30, 40, 40]

score_series = pd.Series(score)
print(score_series)
'''
0    10
1    20
2    30
3    40
4    40  => 1 dimension
'''

#Data Frame
score = [10, 20, 30, 40, 40]

df = pd.DataFrame(score)
print(df)
'''
    0
0  10
1  20
2  30
3  40
4  40  => 2 dimension
'''

#Example_1
score = [10, 20, 30, 40, 40]
score_index = ['korean', 'math', 'english', 'physics', 'biology']

score_series = pd.Series(score, score_index)
print(score_series)

#Example_2
score = {'korean':10, 'math':20, 'english':30, 'physics':40, 'biology':40}

score_series = pd.Series(score)
print(score_series)

#Example_3
score = {'korean':10, 'math':20, 'english':30, 'physics':40, 'biology':40}

score_series = pd.Series(score, ['korean','math','english','physics','biology'])
print(score_series)

#Example_4
score = {'korean':10, 'math':20, 'english':30, 'physics':40, 'biology':40}

score_series = pd.Series(score, ['korean','math','english','physics','biology'])

score_series.index = ['KOREAN', 'MATH', 'ENGLISH', 'PHYSICS', 'BIOLOGY']
print(score_series)

#Example_5
score = {'korean':10, 'math':20, 'english':30, 'physics':40, 'biology':40}

score_series = pd.Series(score, ['korean','math','english','physics','biology'])

print(score_series[0])
print(score_series['korean'])

#Example_6
score = {'korean':10, 'math':20, 'english':30, 'physics':40, 'biology':40}

score_series = pd.Series(score, ['korean','math','english','physics','biology'])

print(score_series[score_series>=30])

#Example_7
score = [10,20,30,40,40]

df = pd.DataFrame(score, columns=['score'])
print(df)

#Example_8
score = [10,20,30,40,40]

df = pd.DataFrame(score, index=['korean','math','english','physics','biology'])
print(df)

#Example_9
data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p'], 'ReTest':['y','y','n','n','n']}

df = pd.DataFrame(data)
print(df)

#Example_10
data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p'], 'ReTest':['y','y','n','n','n']}

df = pd.DataFrame(data, columns=['score','PF','ReTest'])
print(df)

#Example_11
data = [[10,20,30,40,40],['f','f','p','p','p'],['y','y','n','n','n']]

df = pd.DataFrame(data)
print(df)

#T means transpose
df = df.T
print(df)

df.columns = ['score','PF','ReTest']
df.index = ['korean','math','english','physics','biology']
print(df)

#Example_12
data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p'], 'ReTest':['y','y','n','n','n'], 'Name':['song','park','kim','hyun','jin']}

df = pd.DataFrame(data)

#set_index
df = df.set_index('Name')
print(df)

#Example_13
data = {'name':['song','park','kim','na','won','jun','song'],
            'residence':['seoul','seoul','busan','busan','incheon','incheon','seoul'],
            'univ':['seoul','chungang','korea','hanyang','seoul','kaist','seoul'],
            'score':[90,99,96,78,70,100,90],
            'student_number':[2000,2001,2002,2003,2004,2005,2000]}

df = pd.DataFrame(data, columns= ['name','residence','univ','score','student_number'])
print(df)

df = df.set_index(['name','residence'])
print(df)

#Swap the levels in the index
df = df.swaplevel('residence','name')
print(df)


#Result
'''
-Example_1
    korean     10
    math       20
    english    30
    physics    40
    biology    40

-Example_2
    biology    40
    english    30
    korean     10
    math       20
    physics    40

-Example_3
    korean     10
    math       20
    english    30
    physics    40
    biology    40

-Example_4
    KOREAN     10
    MATH       20
    ENGLISH    30
    PHYSICS    40
    BIOLOGY    40

-Example_5
    10
    10 => same results

-Example_6
    english    30
    physics    40
    biology    40

-Example_7
       score
    0     10
    1     20
    2     30
    3     40
    4     40

-Example_8
              0
    korean   10
    math     20
    english  30
    physics  40
    biology  40

-Example_9
      PF ReTest  score
    0  f      y     10
    1  f      y     20
    2  p      n     30
    3  p      n     40
    4  p      n     40

-Example_10
       score PF ReTest
    0     10  f      y
    1     20  f      y
    2     30  p      n
    3     40  p      n
    4     40  p      n

-Example_11
        0   1   2   3   4
    0  10  20  30  40  40
    1   f   f   p   p   p
    2   y   y   n   n   n
    
        0  1  2
    0  10  f  y
    1  20  f  y
    2  30  p  n
    3  40  p  n
    4  40  p  n

            score PF ReTest
    korean     10  f      y
    math       20  f      y
    english    30  p      n
    physics    40  p      n
    biology    40  p      n
    
-Example_12
         PF ReTest  score
    Name                 
    song  f      y     10
    park  f      y     20
    kim   p      n     30
    hyun  p      n     40
    jin   p      n     40
    
-Example_13
                        univ  score  student_number
    name residence                                 
    song seoul         seoul     90            2000
    park seoul      chungang     99            2001
    kim  busan         korea     96            2002
    na   busan       hanyang     78            2003
    won  incheon       seoul     70            2004
    jun  incheon       kaist    100            2005
    song seoul         seoul     90            2000
    
                        univ  score  student_number
    residence name                                 
    seoul     song     seoul     90            2000
              park  chungang     99            2001
    busan     kim      korea     96            2002
              na     hanyang     78            2003
    incheon   won      seoul     70            2004
              jun      kaist    100            2005
    seoul     song     seoul     90            2000
'''