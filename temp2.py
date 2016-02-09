from  sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import seaborn as sns 
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
import numpy as np

#Learning algorithm 






#Now try to find the most interesting dimensions 






def randomizedData(data):
    np.random.shuffle(data)
    X = data[:,:-1]
    y = data[:,-1]
    t = 0.15 #keep 15 percent for testing
    x_train = X[t*len(X):]
    x_test = X[:t*len(X)]
    y_train = y[t*len(y):]
    y_test = y[:t*len(y)]
    return (x_train,y_train,x_test,y_test)



# df = pd.read_csv('data/learning_ready.csv')
df = pd.read_csv('data/learning_ready.csv',nrows=100000)

dft =  df.iloc[:,1:49]
df = pd.concat([dft, df.iloc[:,-1]],axis=1)
# print df
# quit()

# df.columns = ['r'] + list(df.columns[1:])
#prepare the data
data = df[df.columns[0:]].values
# print data,df
# quit()

r = []
rdummy = []

n=1
for i in range(n):
    xy = randomizedData(data)
    clf = RandomForestClassifier()
    clf.fit(xy[0],xy[1])
    r+=[clf.score(xy[2],xy[3])]
    clf2 = DecisionTreeClassifier()
    clf2.fit(xy[0],xy[1])
    rdummy += [clf2.score(xy[2],xy[3])]        

r = np.array(r)
rdummy = np.array(rdummy)
print r.mean(),r.std()
print rdummy.mean(),rdummy.std()


# sns.distplot(r,bins=8,rug=True)
# sns.distplot(rdummy,bins=8,rug=True)
# sns.plt.show()

from sklearn.externals import joblib
joblib.dump(clf2, 'OneTeamCompCLFDT/OneTeamCompCLFDT.pkl') 