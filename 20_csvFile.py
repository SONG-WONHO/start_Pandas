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

#Save to a csv file
df.to_csv('./samples/example_1.csv')

#Load a csv file
df_new = pd.read_csv('./samples/example_1.csv')
print(df_new)
'''
   Unnamed: 0  student_number  name     sex residence      univ  score
0           0            2000  song    male     seoul     seoul     90
1           1            2001  park    male     seoul  chungang     99
2           2            2002   kim  female     busan     korea     96
3           3            2003    na  female     busan   hanyang     78
4           4            2004   won    male   incheon     seoul     70
5           5            2005   jun    male   incheon     kaist    100
6           6            2000  song    male     seoul     seoul     90
'''

#Load a csv file with no headers
df_new = pd.read_csv('./samples/example_1.csv', header= None)
print(df_new)
'''
     0               1     2       3          4         5      6
0  NaN  student_number  name     sex  residence      univ  score
1  0.0            2000  song    male      seoul     seoul     90
2  1.0            2001  park    male      seoul  chungang     99
3  2.0            2002   kim  female      busan     korea     96
4  3.0            2003    na  female      busan   hanyang     78
5  4.0            2004   won    male    incheon     seoul     70
6  5.0            2005   jun    male    incheon     kaist    100
7  6.0            2000  song    male      seoul     seoul     90
'''

#Load a csv file while specifying column names
df_new = pd.read_csv('./samples/example_1.csv', names= ['index', 'student_number', 'name', 'sex', 'residence', 'univ', 'score'])
print(df_new)
'''
   index  student_number  name     sex  residence      univ  score
0    NaN  student_number  name     sex  residence      univ  score
1    0.0            2000  song    male      seoul     seoul     90
2    1.0            2001  park    male      seoul  chungang     99
3    2.0            2002   kim  female      busan     korea     96
4    3.0            2003    na  female      busan   hanyang     78
5    4.0            2004   won    male    incheon     seoul     70
6    5.0            2005   jun    male    incheon     kaist    100
7    6.0            2000  song    male      seoul     seoul     90
'''

#Load a csv file with setting the original index
df_new = pd.read_csv('./samples/example_1.csv', index_col='index', names= ['index', 'student_number', 'name', 'sex', 'residence', 'univ', 'score'])
print(df_new)
'''
       student_number  name     sex  residence      univ  score
index                                                          
NaN    student_number  name     sex  residence      univ  score
 0.0             2000  song    male      seoul     seoul     90
 1.0             2001  park    male      seoul  chungang     99
 2.0             2002   kim  female      busan     korea     96
 3.0             2003    na  female      busan   hanyang     78
 4.0             2004   won    male    incheon     seoul     70
 5.0             2005   jun    male    incheon     kaist    100
 6.0             2000  song    male      seoul     seoul     90
'''

#Load a csv file by web llink
df_new = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/datasets/iris.csv')
print(df_new.head())
