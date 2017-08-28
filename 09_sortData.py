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

print(df.sort_values(by='finalScore',ascending=True))
'''
  name  age  finalScore  quizScore
1    b   21          80          5
2    c   22          85          4
3    d   20          88          3
0    a   20          90          5
4    e   19          95          5

'''

print(df.sort_values(by='finalScore',ascending=False))
'''
  name  age  finalScore  quizScore
4    e   19          95          5
0    a   20          90          5
3    d   20          88          3
2    c   22          85          4
1    b   21          80          5
'''