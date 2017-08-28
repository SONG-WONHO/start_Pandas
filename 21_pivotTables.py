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

#Pivot table
print(pd.pivot_table(df, index= ['sex','residence'], columns=df['student_number'], values=['score'], fill_value='*'))
'''
                 score                         
student_number    2000 2001 2002 2003 2004 2005
sex    residence                               
female busan         *    *   96   78    *    *
male   incheon       *    *    *    *   70  100
       seoul        90   99    *    *    *    *
'''

#example_1
print(pd.pivot_table(df, index='sex', columns='residence', values='score'))
'''
residence  busan  incheon  seoul
sex                             
female      87.0      NaN    NaN
male         NaN     85.0   93.0
'''