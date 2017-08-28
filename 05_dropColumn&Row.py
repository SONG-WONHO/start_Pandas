#load pandas as pd
import pandas as pd
#load numpy as np
import numpy as np

#raw data
raw_data = {'name':['song','park','kim','na','won','jun'],
            'residence':['seoul','seoul','busan','busan','incheon','incheon'],
            'univ':['seoul','chungang','korea','hanyang','seoul','kaist'],
            'score':[90,99,96,78,70,100],
            'student_number':[2000,2001,2002,2003,2004,2005]}

df = pd.DataFrame(raw_data, columns=['name','residence','univ','score','student_number'])
'''
   name residence      univ  score  student_number
0  song     seoul     seoul     90            2000
1  park     seoul  chungang     99            2001
2   kim     busan     korea     96            2002
3    na     busan   hanyang     78            2003
4   won   incheon     seoul     70            2004
5   jun   incheon     kaist    100            2005
'''

#add a column
df['PF'] = np.where(df['score']>=90,'P','F')
'''
   name residence      univ  score  student_number PF
0  song     seoul     seoul     90            2000  P
1  park     seoul  chungang     99            2001  P
2   kim     busan     korea     96            2002  P
3    na     busan   hanyang     78            2003  F
4   won   incheon     seoul     70            2004  F
5   jun   incheon     kaist    100            2005  P
'''

#drop a column
print(df.drop(['PF'],axis=1))
'''
   name residence      univ  score  student_number
0  song     seoul     seoul     90            2000
1  park     seoul  chungang     99            2001
2   kim     busan     korea     96            2002
3    na     busan   hanyang     78            2003
4   won   incheon     seoul     70            2004
5   jun   incheon     kaist    100            2005
'''

#drop a row
print(df.drop([3,5],axis=0))
'''
   name residence      univ  score  student_number PF
0  song     seoul     seoul     90            2000  P
1  park     seoul  chungang     99            2001  P
2   kim     busan     korea     96            2002  P
4   won   incheon     seoul     70            2004  F
'''

#example_1
print(df[df['name']!='song'])
'''
   name residence      univ  score  student_number PF
1  park     seoul  chungang     99            2001  P
2   kim     busan     korea     96            2002  P
3    na     busan   hanyang     78            2003  F
4   won   incheon     seoul     70            2004  F
5   jun   incheon     kaist    100            2005  P
'''

#example_2
print(df.drop(df.index[3]))
'''
   name residence      univ  score  student_number PF
0  song     seoul     seoul     90            2000  P
1  park     seoul  chungang     99            2001  P
2   kim     busan     korea     96            2002  P
4   won   incheon     seoul     70            2004  F
5   jun   incheon     kaist    100            2005  P
'''

#example_3
print(df.drop(df.index[[1,4]]))
'''
   name residence     univ  score  student_number PF
0  song     seoul    seoul     90            2000  P
2   kim     busan    korea     96            2002  P
3    na     busan  hanyang     78            2003  F
5   jun   incheon    kaist    100            2005  P
'''

#example_4
print(df[:3])
'''
   name residence      univ  score  student_number PF
0  song     seoul     seoul     90            2000  P
1  park     seoul  chungang     99            2001  P
2   kim     busan     korea     96            2002  P
'''

#example_5
print(df.drop(df.columns[1],axis=1))
'''
   name      univ  score  student_number PF
0  song     seoul     90            2000  P
1  park  chungang     99            2001  P
2   kim     korea     96            2002  P
3    na   hanyang     78            2003  F
4   won     seoul     70            2004  F
5   jun     kaist    100            2005  P
'''