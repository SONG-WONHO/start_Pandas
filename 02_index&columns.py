#load pandas as pd
import pandas as pd

'''
Rows => index
Columns => columns
'''

#Raw data
data = {'score':[10,20,30,40,40], 'PF':['f','f','p','p','p'], 'ReTest':['y','y','n','n','n']}

#Create Data Frame
df = pd.DataFrame(data)

'''
  PF ReTest  score
0  f      y     10
1  f      y     20
2  p      n     30
3  p      n     40
4  p      n     40
'''

print(df.columns) ## Index(['PF', 'ReTest', 'score'], dtype='object')
print(df.index) ## RangeIndex(start=0, stop=5, step=1)


'''
  PF ReTest  score => columns
0  f      y     10 => index
1  f      y     20 => index
2  p      n     30 => index
3  p      n     40 => index
4  p      n     40 => index
'''

print(df.columns[0]) ## PF
print(df.columns[1]) ## ReTest
print(df.columns[2]) ## score

print(df.index[0]) ## 0
print(df.index[1]) ## 1
print(df.index[2]) ## 2
print(df.index[3]) ## 3
print(df.index[4]) ## 4

#Reindex
#method_1
df_reindex = pd.DataFrame(df, index = [2,1,0,4,3])
print(df_reindex)
'''
  PF ReTest  score
2  p      n     30
1  f      y     20
0  f      y     10
4  p      n     40
3  p      n     40
'''

df_reindex = pd.DataFrame(df, columns  = ['score','PF','ReTest'])
print(df_reindex)
'''
   score PF ReTest
0     10  f      y
1     20  f      y
2     30  p      n
3     40  p      n
4     40  p      n
'''

#method_2
df_reindex = df.reindex(index = [2,1,0,4,3])
print(df_reindex)
'''
  PF ReTest  score
2  p      n     30
1  f      y     20
0  f      y     10
4  p      n     40
3  p      n     40
'''

df_reindex = df.reindex(columns = ['score','PF','ReTest'])
print(df_reindex)
'''
   score PF ReTest
0     10  f      y
1     20  f      y
2     30  p      n
3     40  p      n
4     40  p      n
'''

#Rename
#method_1
df = df.reindex(columns=['score','PF','ReTest'])

df_rename = df
df_rename.columns = ['SCORE', 'Pass Or Fail', 'Retake']
print(df_rename)
'''
   SCORE Pass Or Fail Retake
0     10            f      y
1     20            f      y
2     30            p      n
3     40            p      n
4     40            p      n
'''

#method_2
df.columns = ['score', 'PF', 'ReTest']

df = df.rename(columns = {'score':'SCORE'})
print(df)
'''
   SCORE PF ReTest
0     10  f      y
1     20  f      y
2     30  p      n
3     40  p      n
4     40  p      n
'''
#method_2 can rename the column name separately