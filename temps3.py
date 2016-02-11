#want to see the tree

import numpy as np
import pandas as pd
import seaborn as sns 
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
import numpy as np

# from sklearn.externals import joblib
# clf = joblib.load('OneTeamCompCLFDT/OneTeamCompCLFDT.pkl') 


df = pd.read_csv('data/learning_ready.csv',nrows=100)

dft =  df.iloc[:,1:49]
df = pd.concat([dft, df.iloc[:,-1]],axis=1)

print df
quit()
t=[ df.iloc[95,0:48].values]

print clf.predict_proba(t)
print df.iloc[1,-1]



#visualize the decision tree

# from sklearn import tree
# tree.export_graphviz(clf,out_file='tree.dot') 