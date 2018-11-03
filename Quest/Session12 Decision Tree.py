# 제출 시 파일명은 Session12 이름 으로 해주세요.

# 1. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 RandomForest를 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
# 2. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 Boosting을 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
#이날 수업을 못가서 코드를 조금씩 바꿔보는 정도에 만족했지만 decision tree는 오늘 강사님께서도 잠깐 언급하셨다 싶이 널리 쓰이는 거같아서 
#개인적으로 조금 더 자습해 배우는 시간을 가질 계획입니다. 마지막 까지 수고 많으셨습니다...! 
import numpy as np
import pandas as pd
import seaborn as sns
!pip3 install xgboost
import xgboost
%matplotlib inline

from sklearn import datasets  
cancer = datasets.load_breast_cancer() 
from sklearn.model_selection import train_test_split 
 
cancer = load_breast_cancer() 

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify = cancer.target, random_state = 0) 
iris = datasets.load_iris()

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


xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2)
xgb.fit(X_train, y_train)
predicted_xgb = xgb.predict(X_test) 
accuracy_xgb = accuracy_score(y_test, predicted_xgb) 

print(f'Mean accuracy score: {accuracy_xgb:.3}')
cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb), columns=cancer.target_names, index=cancer.target_names)
sns.heatmap(cm_xgb, annot=True) 
