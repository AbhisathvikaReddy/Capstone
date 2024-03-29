
pip install mlxtend

import pandas as pd
import numpy as np

pip install --upgrade mlxtend
data = pd.read_csv('projectdataset.csv')
data



import matplotlib.pyplot as plt

data = pd.read_csv('projectdataset.csv')
label = data.groupby('defects').size()
label.plot(kind="bar")
plt.xlabel("Software Defects 0 (Defects),' 1 (Non-Defects)")
plt.ylabel("Count")
plt.title("Software Defects Graph")
unique, count = np.unique(data['defects'], return_counts=True)
print("Number of Non-Defects : "+str(count[0]))
print("Number of Defects  : "+str(count[1]))
plt.show()
plt.savefig("dataset_before_smote.jpeg")
from imblearn.over_sampling import SMOTE
import pandas as pd
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)
df_resampled = pd.concat([pd.DataFrame(X_resampled), pd.DataFrame(y_resampled)], axis=1)
df_resampled.columns = data.columns
data=df_resampled
original=data
data

label = data.groupby('defects').size()
label.plot(kind="bar")
plt.xlabel("Software Defects 0 (Defects),' 1 (Non-Defects)")
plt.ylabel("Count")
plt.title("Software Defects Graph")
unique, count = np.unique(data['defects'], return_counts=True)
print("Number of Non-Defects : "+str(count[0]))
print("Number of Defects  : "+str(count[1]))
plt.show()
plt.savefig("dataset_after_smote.png")
# Print the class distribution after oversampling
print("After oversampling:\n", df_resampled.iloc[:,-1].value_counts())

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.neighbors import KNeighborsClassifier
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
