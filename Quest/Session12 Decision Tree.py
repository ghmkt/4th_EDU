# • 1. import library, load data, check data 
import numpy as np
import pandas as pd
import seaborn as sns
import xgboost
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

bc = datasets.load_breast_cancer()
b_c = pd.DataFrame(bc.data, columns=bc.feature_names)
b_c.head()

# • 2. divide data into x, y 
# • 3. split data into train set, test set 
X_train, X_test, y_train, y_test = train_test_split(b_c[bc.feature_names], bc.target, 
                                                    test_size=0.25, stratify=bc.target, random_state=3)
# • 4. use RandomForestClassifier and show confusion matrix 
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=3)
rf.fit(X_train, y_train)

predicted = rf.predict(X_test)
accuracy = accuracy_score(y_test, predicted)

cm = pd.DataFrame(confusion_matrix(y_test, predicted), columns=bc.target_names, index=bc.target_names)
sns.heatmap(cm, annot=True)

print(f'Out-of-bag score estimate: {rf.oob_score_:.3}')
print(f'Mean accuracy score: {accuracy:.3}')
# malignant와 benign을 혼동하는 경우가 있다.

# • 5. use XGBClassifier and show confusion matrix 
# • 6. make some simple comments about the result

xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2)
xgb.fit(X_train, y_train)
predicted_xgb = xgb.predict(X_test)
accuracy_xgb = accuracy_score(y_test, predicted_xgb)
cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb), columns=bc.target_names, index=bc.target_names)
sns.heatmap(cm_xgb, annot=True)
print(f'Mean accuracy score: {accuracy_xgb:.3}')
# 조그만 차이지만, 예측성능이 더 나빠졌다...(?)
