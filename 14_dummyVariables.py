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

#Dummy variable
df_sex = pd.get_dummies(df['sex'])
print(df_sex)
'''
   female  male
0       0     1
1       0     1
2       1     0
3       1     0
'''