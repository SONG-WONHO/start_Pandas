#load pandas as pd
import pandas as pd

#raw data
raw_data = {'name':['song','park','kim','na','won','jun','song'],
            'residence':['seoul','seoul','busan','busan','incheon','incheon','seoul'],
            'univ':['seoul','chungang','korea','hanyang','seoul','kaist','seoul'],
            'score':[90,99,96,78,70,100,90],
            'student_number':[2000,2001,2002,2003,2004,2005,2000]}

df = pd.DataFrame(raw_data, columns=['name','residence','univ','score','student_number'])
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

print(df.duplicated())
'''
0    False
1    False
2    False
3    False
4    False
5    False
6     True
dtype: bool
'''

print(df.drop_duplicates())
'''
   name residence      univ  score  student_number
0  song     seoul     seoul     90            2000
1  park     seoul  chungang     99            2001
2   kim     busan     korea     96            2002
3    na     busan   hanyang     78            2003
4   won   incheon     seoul     70            2004
5   jun   incheon     kaist    100            2005
'''

print(df.drop_duplicates(keep='last'))
'''
   name residence      univ  score  student_number
1  park     seoul  chungang     99            2001
2   kim     busan     korea     96            2002
3    na     busan   hanyang     78            2003
4   won   incheon     seoul     70            2004
5   jun   incheon     kaist    100            2005
6  song     seoul     seoul     90            2000
'''