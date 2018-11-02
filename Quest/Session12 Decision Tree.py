# 제출 시 파일명은 Session12 이름 으로 해주세요.

# 1. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 RandomForest를 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부

import numpy as np
import pandas as pd
import seaborn as sns
import xgboost
from sklearn import datasets
from sklearn.metrics import confusion_matrix
#기본적인 breast cancer 데이터 로드하기
breast_cancer= datasets.load_breast_cancer()
x= pd.DataFrame(breast_cancer.data)
y=pd.DataFrame(breast_cancer.target)

#로드한 데이터를 train set과 test set으로 스플릿하기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, stratify=y, random_state=123)

# RandomForest 실행
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
rf.fit(X_train, y_train)
predicted = rf.predict(X_test) 

# 실행 결과를 Confusion matrix로 표현하기
cm = pd.DataFrame(confusion_matrix(y_test, predicted), columns=['negative','positive'], index=['negative','positive'])
sns.heatmap(cm, annot=True)

# 2. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 Boosting을 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부

#xgb 실행하기
xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2)
xgb.fit(X_train,y_train)
predicted_xgb = xgb.predict(X_test)

# 실행 결과를 Confusion matrix로 표현하기
cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb),columns=['negative','positive'], index=['negative','positive'])
sns.heatmap(cm_xgb, annot=True)
