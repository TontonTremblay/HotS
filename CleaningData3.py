import numpy as np
import pandas as pd
df = pd.read_csv('data/learning.csv')
# df = pd.read_csv('data/learning.csv',nrows=100)

#just want to export the data with the binary arrays 

df1 = df[:len(df)/2]
df2 = df[len(df)/2:]

dfchars = pd.read_csv('data/HeroIDAndMapID 2015-12-30 - 2016-01-29.csv')[0:48]




t1=df1[dfchars.Name.values].values
t2=df1[dfchars.Name.values+'.1'].values

a1 = np.concatenate((t1,t2),axis=1)
a1=np.insert(a1, len(a1[0]), 1, axis=1)

t1=df2[dfchars.Name.values+'.1'].values
t2=df2[dfchars.Name.values].values

a2 = np.concatenate((t1,t2),axis=1)
a2=np.insert(a2, len(a2[0]), 2, axis=1)

f=np.concatenate((a1, a2))

np.random.shuffle(f)
result = pd.DataFrame(f,columns = list(dfchars.Name.values) + list(dfchars.Name.values+".2") + ['winner'])


result.to_csv('data/learning_ready.csv')
