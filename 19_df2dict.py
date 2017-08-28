#load pandas as pd
import pandas as pd

#raw_data
raw_data = {'name':['song','park','kim','na','won','jun','song'],
            'residence':['seoul','seoul','busan','busan','incheon','incheon','seoul'],
            'univ':['seoul','chungang','korea','hanyang','seoul','kaist','seoul'],
            'score':[90,99,96,78,70,100,90],
            'student_number':[2000,2001,2002,2003,2004,2005,2000],
            'sex':['male','male','female','female','male','male','male']}

df = pd.DataFrame(raw_data, columns= ['student_number','name','sex','residence','univ','score'])
'''
   student_number  name     sex residence      univ  score
0            2000  song    male     seoul     seoul     90
1            2001  park    male     seoul  chungang     99
2            2002   kim  female     busan     korea     96
3            2003    na  female     busan   hanyang     78
4            2004   won    male   incheon     seoul     70
5            2005   jun    male   incheon     kaist    100
6            2000  song    male     seoul     seoul     90
'''

#df2dict

#orient: dict
print(df.to_dict())
'''
{'student_number': {0: 2000, 1: 2001, 2: 2002, 3: 2003, 4: 2004, 5: 2005, 6: 2000}, 
 'name': {0: 'song', 1: 'park', 2: 'kim', 3: 'na', 4: 'won', 5: 'jun', 6: 'song'}, 
 'sex': {0: 'male', 1: 'male', 2: 'female', 3: 'female', 4: 'male', 5: 'male', 6: 'male'}, 
 'residence': {0: 'seoul', 1: 'seoul', 2: 'busan', 3: 'busan', 4: 'incheon', 5: 'incheon', 6: 'seoul'}, 
 'univ': {0: 'seoul', 1: 'chungang', 2: 'korea', 3: 'hanyang', 4: 'seoul', 5: 'kaist', 6: 'seoul'}, 
 'score': {0: 90, 1: 99, 2: 96, 3: 78, 4: 70, 5: 100, 6: 90}}
'''

#orienct:list
print(df.to_dict('list'))
'''
{'student_number': [2000, 2001, 2002, 2003, 2004, 2005, 2000], 
 'name': ['song', 'park', 'kim', 'na', 'won', 'jun', 'song'], 
 'sex': ['male', 'male', 'female', 'female', 'male', 'male', 'male'], 
 'residence': ['seoul', 'seoul', 'busan', 'busan', 'incheon', 'incheon', 'seoul'], 
 'univ': ['seoul', 'chungang', 'korea', 'hanyang', 'seoul', 'kaist', 'seoul'], 
 'score': [90, 99, 96, 78, 70, 100, 90]}
'''