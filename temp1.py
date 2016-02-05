import numpy as np
import pandas as pd
import seaborn as sns 
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
import numpy as np

from sklearn.externals import joblib
clf = joblib.load('OneTeamCompCLF/filename.pkl') 


df = pd.read_csv('data/learning_ready.csv',nrows=100)

dft =  df.iloc[:,1:49]
df = pd.concat([dft, df.iloc[:,-1]],axis=1)

t=[ df.iloc[1,0:48].values]

print clf.predict_proba(t)
print df.iloc[1,-1]

print "----"
for i in range(0,len(df.columns.values)-1):
    print df.columns.values[i], clf.feature_importances_[i]
# print clf.feature_importances_