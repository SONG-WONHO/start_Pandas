#load pandas as pd
import pandas as pd

#raw data
raw_data = {'name':['a','b','c','d'],'sex':['male','male','female','female']}

df = pd.DataFrame(raw_data, columns= ['name','sex'])
'''
  name     sex
0    a    male
1    b    male
2    c  female
3    d  female
'''
data_a = pd.get_dummies(df['sex'])
print(data_a)
data_b = {'name':['e','f'], 'sex':['male','female']}
data_b = pd.DataFrame(data_b, columns= ['name','sex'])
print(data_b)

#concat()
#case_1
df_new = pd.concat([df, data_a], axis= 1)
print(df_new)
'''
  name     sex  female  male
0    a    male       0     1
1    b    male       0     1
2    c  female       1     0
3    d  female       1     0
'''

#case_2
df_new = pd.concat([df, data_b], axis= 0)
print(df_new)
'''
  name     sex
0    a    male
1    b    male
2    c  female
3    d  female
0    e    male
1    f  female
'''

#append()
df_new = df.append(data_b)
print(df_new)
'''
  name     sex
0    a    male
1    b    male
2    c  female
3    d  female
0    e    male
1    f  female
'''

#join()
df_new = df.join(data_a)
print(df_new)
'''
  name     sex  female  male
0    a    male       0     1
1    b    male       0     1
2    c  female       1     0
3    d  female       1     0
'''

#merge()
raw_data = {'id':[1,2,3,4], 'name':['a','b','c','d'], 'last_name':['A','B','C','D']}
df_a = pd.DataFrame(raw_data, columns=['id','name','last_name'])

raw_data = {'id':[3,4,5,6], 'name':['e','f','g','h'], 'last_name':['E','F','G','H']}
df_b = pd.DataFrame(raw_data, columns=['id','name','last_name'])

#df_a
'''
   id name last_name
0   1    a         A
1   2    b         B
2   3    c         C
3   4    d         D
'''
#df_b
'''
   id name last_name
0   3    e         E
1   4    f         F
2   5    g         G
3   6    h         H
'''

print(pd.merge(df_a, df_b, on= 'id', how= 'outer'))
'''
   id name_x last_name_x name_y last_name_y
0   1      a           A    NaN         NaN
1   2      b           B    NaN         NaN
2   3      c           C      e           E
3   4      d           D      f           F
4   5    NaN         NaN      g           G
5   6    NaN         NaN      h           H
'''

print(pd.merge(df_a, df_b, on= 'id', how= 'inner'))
'''
   id name_x last_name_x name_y last_name_y
0   3      c           C      e           E
1   4      d           D      f           F
'''

print(pd.merge(df_a, df_b, on= 'id', how= 'left'))
'''
   id name_x last_name_x name_y last_name_y
0   1      a           A    NaN         NaN
1   2      b           B    NaN         NaN
2   3      c           C      e           E
3   4      d           D      f           F
'''

print(pd.merge(df_a, df_b, on= 'id', how= 'right'))
'''
   id name_x last_name_x name_y last_name_y
0   3      c           C      e           E
1   4      d           D      f           F
2   5    NaN         NaN      g           G
3   6    NaN         NaN      h           H
'''

print(pd.merge(df_a, df_b, on= 'id', how= 'outer', suffixes=('_left','_right')))
'''
   id name_left last_name_left name_right last_name_right
0   1         a              A        NaN             NaN
1   2         b              B        NaN             NaN
2   3         c              C          e               E
3   4         d              D          f               F
4   5       NaN            NaN          g               G
5   6       NaN            NaN          h               H
'''

print(pd.merge(df_a, df_b, right_index=True, left_index=True))
'''
   id_x name_x last_name_x  id_y name_y last_name_y
0     1      a           A     3      e           E
1     2      b           B     4      f           F
2     3      c           C     5      g           G
3     4      d           D     6      h           H
'''