import pandas as pd
# df = pd.read_csv('data/clean.csv',nrows=100)
df = pd.read_csv('data/clean.csv')


def f(x,i):
    x = eval(str(x))
    # print x[i]
    # quit()
    # print x
    if len(x) is 0 :
        return 0
    return x[i]

def average(x):
    x = eval(str(x))
    if len(x) is 0 :
        return 0
    return (sum(x)*1.0)/len(x)

df['avgmmr1'] = df.mmr1.apply(average)
df['avgmmr2'] = df.mmr2.apply(average)

for i in range(1,6):
    df['mmr1'+str(i)] = df['mmr1'].apply(f,args=(i-1,))
    df['c1'+str(i)] = df['c1'].apply(f,args=(i-1,))
        
for i in range(1,6):
    df['mmr2'+str(i)] = df['mmr2'].apply(f,args=(i-1,))
    df['c2'+str(i)] = df['c2'].apply(f,args=(i-1,))

def applyWin(x):
    return 1
def applyLoose(x):
    return 0




###now create the array of players. 
#binary array 
chars = {}
dfchars = pd.read_csv('data/HeroIDAndMapID 2015-12-30 - 2016-01-29.csv')[0:48]

a1 = [[0 for i in range(48)]for j in range(len(df ))]
a2 = [[0 for i in range(48)]for j in range(len(df ))]

global ii
ii = 0

def getArray(x,a):
    global ii 
    x = eval(str(x))
    if len(x)is 0:
        return 
    for v in x: 
        a[ii][v]=1
    ii+=1

df.c1.apply(getArray,args=(a1,))
ii=0
df.c2.apply(getArray,args=(a2,))

dfc1 = pd.DataFrame(a1,columns=dfchars.Name.values)
dfc2 = pd.DataFrame(a2,columns=dfchars.Name.values)

result = pd.concat([df, dfc1],axis=1)
result['team1win']=result.mmr1.apply(applyWin)

result = pd.concat([result, dfc2],axis=1)
result['team2win']=result.mmr1.apply(applyLoose)


result.to_csv('data/learning.csv')
