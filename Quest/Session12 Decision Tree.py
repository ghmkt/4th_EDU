# 제출 시 파일명은 Session12 이름 으로 해주세요.

from sklearn import datasets
import numpy as np
import pandas as pd
import seaborn as sns
import xgboost
from sklearn.model_selection import train_test_split

# 1. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 RandomForest를 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
breast_cancer = datasets.load_breast_cancer()
print(breast_cancer.DESCR)
X_train, X_test, y_train, y_test = train_test_split(breast_cancer.data, breast_cancer.target, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
rf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
predicted = rf.predict(X_test)
accuracy = accuracy_score(y_test, predicted) 
print(f'Out-of-bag score estimate: {rf.oob_score_:.3}')
print(f'Mean accuracy score: {accuracy:.3}')
    Out-of-bag score estimate: 0.958
    Mean accuracy score: 0.965

from sklearn.metrics import confusion_matrix
cm = pd.DataFrame(confusion_matrix(y_test, predicted), columns=breast_cancer.target_names, index=breast_cancer.target_names)
sns.heatmap(cm, annot=True)

# 2. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 Boosting을 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2)
xgb.fit(X_train, y_train)

predicted_xgb = xgb.predict(X_test)
accuracy_xgb = accuracy_score(y_test, predicted_xgb)
print(f'Mean accuracy score: {accuracy_xgb:.3}')
    Mean accuracy score: 0.979

cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb), columns=breast_cancer.target_names, index=breast_cancer.target_names)
sns.heatmap(cm_xgb, annot=True)

## Comment: RandomForest를 썼을 때보다 Boosting을 활용했을 때 정확도가 더 높아진 것을 mean accuracy score(0.965 < 0.979)와 confusion matrix를 통해서 알 수 있다.
