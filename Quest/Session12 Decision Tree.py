# 제출 시 파일명은 Session12 이름 으로 해주세요.

# 1. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 RandomForest를 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부

##1. import library, load data, check data
import numpy as np
import pandas as pd
import seaborn as sns
import xgboost

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
cancer

##2. divide data into x,y
x = pd.DataFrame(cancer.data, columns=cancer.feature_names)
x.head()
y = pd.DataFrame(cancer.target)
y.head()

##3. split data into train set, test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

##4. use RandomForestClassifier and show confusion matrix
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
rf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

predicted = rf.predict(X_test) 
accuracy = accuracy_score(y_test, predicted) 

print(f'Out-of-bag score estimate: {rf.oob_score_:.3}')
print(f'Mean accuracy score: {accuracy:.3}')

from sklearn.metrics import confusion_matrix

cm = pd.DataFrame(confusion_matrix(y_test, predicted), columns=cancer.target_names, index=cancer.target_names)

sns.heatmap(cm, annot=True)


# 2. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 Boosting을 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부

##5. use XGBClassifier and show confusion matrix

xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2)
xgb.fit(X_train, y_train)

predicted_xgb = xgb.predict(X_test)
accuracy_xgb = accuracy_score(y_test, predicted_xgb)

print(f'Mean accuracy score: {accuracy_xgb:.3}')

cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb), columns=cancer.target_names, index=cancer.target_names)
sns.heatmap(cm_xgb, annot=True)

##6. make some simple comments about the results

Random Forest 예측모델의 accuracy는  0.959, XGBoost 예측모델의 accuracy는 0.965로 XGBoost의 예측 성능이 더 높지만 두 모델의 예측력에 큰 차이는 없다.
두 모델의 confusion matrix를 보면 악성, 양성 여부가 대체로 잘 분류되지만 정확하게 

