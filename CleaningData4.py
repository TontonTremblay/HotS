import numpy as np
import pandas as pd
dff = pd.read_csv('data/learning.csv')
# dff = pd.read_csv('data/learning.csv',nrows=100)

#just want to export the data with the binary arrays 
#This is a more complete ready to learn data set 
#with the MMR on top of the char used. 




for value in dff['mode'].unique():

    df = dff[dff['mode'] == value]
    
    mmr1 = [[0 for i in range(5)]for j in range(len(df ))]
    mmr2 = [[0 for i in range(5)]for j in range(len(df ))]


    global ii
    ii = 0

    def getArray(x,a):
        global ii 
        x = eval(str(x))
        if len(x)is 0:
            return 
        # for v in x: 
        a[ii]= x
        ii+=1

    df.mmr1.apply(getArray,args=(mmr1,))
    ii=0
    df.mmr2.apply(getArray,args=(mmr2,))

    # print mmr1
    df = pd.concat([df, pd.DataFrame(mmr1,columns=['11','12','13','14','15'])],axis=1) 
    df = pd.concat([df, pd.DataFrame(mmr2,columns=['21','22','23','24','25'])],axis=1) 

    # print df

    mmrNames = ['11','12','13','14','15','21','22','23','24','25']



    df1 = df[:len(df)/2]
    df2 = df[len(df)/2:]
    dfchars = pd.read_csv('data/HeroIDAndMapID 2015-12-30 - 2016-01-29.csv')[0:48]


    t1=df1[dfchars.Name.values].values
    t2=df1[dfchars.Name.values+'.1'].values

    a1 = np.concatenate((t1,t2),axis=1)
    a1 = np.concatenate((a1,df1[mmrNames].values),axis=1)

    a1=np.insert(a1, len(a1[0]), 1, axis=1)

    t1=df2[dfchars.Name.values+'.1'].values
    t2=df2[dfchars.Name.values].values

    a2 = np.concatenate((t1,t2),axis=1)
    a2 = np.concatenate((a2,df2[mmrNames].values),axis=1)

    a2=np.insert(a2, len(a2[0]), 2, axis=1)

    f=np.concatenate((a1, a2))

    np.random.shuffle(f)
    result = pd.DataFrame(f,columns = list(dfchars.Name.values) + list(dfchars.Name.values+".2") + mmrNames + ['winner'])

    dfmode = {3:'Quick_Match', 4:'Hero_League', 5:'Team_League'}

    # print result
    result.to_csv('data/learning_ready_with_mmr_'+dfmode[int(value)]+'.csv')


#All of the them

# df = dff[dff['mode'] == value]
df = dff

mmr1 = [[0 for i in range(5)]for j in range(len(df ))]
mmr2 = [[0 for i in range(5)]for j in range(len(df ))]


global ii
ii = 0

def getArray(x,a):
    global ii 
    x = eval(str(x))
    if len(x)is 0:
        return 
    # for v in x: 
    a[ii]= x
    ii+=1

df.mmr1.apply(getArray,args=(mmr1,))
ii=0
df.mmr2.apply(getArray,args=(mmr2,))

# print mmr1
df = pd.concat([df, pd.DataFrame(mmr1,columns=['11','12','13','14','15'])],axis=1) 
df = pd.concat([df, pd.DataFrame(mmr2,columns=['21','22','23','24','25'])],axis=1) 

# print df

mmrNames = ['11','12','13','14','15','21','22','23','24','25']



df1 = df[:len(df)/2]
df2 = df[len(df)/2:]
dfchars = pd.read_csv('data/HeroIDAndMapID 2015-12-30 - 2016-01-29.csv')[0:48]


t1=df1[dfchars.Name.values].values
t2=df1[dfchars.Name.values+'.1'].values

a1 = np.concatenate((t1,t2),axis=1)
a1 = np.concatenate((a1,df1[mmrNames].values),axis=1)

a1=np.insert(a1, len(a1[0]), 1, axis=1)

t1=df2[dfchars.Name.values+'.1'].values
t2=df2[dfchars.Name.values].values

a2 = np.concatenate((t1,t2),axis=1)
a2 = np.concatenate((a2,df2[mmrNames].values),axis=1)

a2=np.insert(a2, len(a2[0]), 2, axis=1)

f=np.concatenate((a1, a2))

np.random.shuffle(f)
result = pd.DataFrame(f,columns = list(dfchars.Name.values) + list(dfchars.Name.values+".2") + mmrNames + ['winner'])

dfmode = {3:'Quick_Match', 4:'Hero_League', 5:'Team_League'}

# print result
result.to_csv('data/learning_ready_with_mmr_'+dfmode[int(value)]+'.csv')