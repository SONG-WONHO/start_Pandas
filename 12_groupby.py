#load pandas as pd
import pandas as pd

#raw data
raw_data = {'name':['song','park','kim','na','won','jun','song'],
            'residence':['seoul','seoul','busan','busan','incheon','incheon','seoul'],
            'univ':['seoul','chungang','korea','hanyang','seoul','kaist','seoul'],
            'score':[90,99,96,78,70,100,90],
            'student_number':[2000,2001,2002,2003,2004,2005,2000]}

df = pd.DataFrame(raw_data, columns= ['name','residence','univ','score','student_number'])
'''
   name residence      univ  score  student_number
0  song     seoul     seoul     90            2000
1  park     seoul  chungang     99            2001
2   kim     busan     korea     96            2002
3    na     busan   hanyang     78            2003
4   won   incheon     seoul     70            2004
5   jun   incheon     kaist    100            2005
6  song     seoul     seoul     90            2000
'''

group = df['name'].groupby(by= df['residence'])
print(list(group))
'''
[('busan', 2    kim
           3     na
Name: name, dtype: object), 
('incheon', 4    won
            5    jun
Name: name, dtype: object), 
('seoul', 0    song
          1    park
          6    song
Name: name, dtype: object)]
'''

group = df['name'].groupby(by= [df['residence'],df['univ']])
print(list(group))
'''
[(('busan', 'hanyang'), 3    na
Name: name, dtype: object), 
(('busan', 'korea'), 2    kim
Name: name, dtype: object), 
(('incheon', 'kaist'), 5    jun
Name: name, dtype: object), 
(('incheon', 'seoul'), 4    won
Name: name, dtype: object), 
(('seoul', 'chungang'), 1    park
Name: name, dtype: object), 
(('seoul', 'seoul'), 0    song
                     6    song
Name: name, dtype: object)]
'''

#example_1
group = df['score'].groupby(by= [df['univ']])
print(group.mean())
'''
univ
chungang     99.000000
hanyang      78.000000
kaist       100.000000
korea        96.000000
seoul        83.333333
Name: score, dtype: float64
'''

#example_2
group = df['name'].groupby(by= df['residence'])

#same
group = df.groupby(by= df['residence'])['name']
print(list(group))
'''
[('busan', 2    kim
           3     na
Name: name, dtype: object), 
('incheon', 4    won
            5    jun
Name: name, dtype: object), 
('seoul', 0    song
          1    park
          6    song
Name: name, dtype: object)]
'''