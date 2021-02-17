# 제출 시 파일명은 Session12 이름 으로 해주세요.

# 1. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 RandomForest를 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
import numpy as np
import pandas as pd
import seaborn as sns
import xgboost
from sklearn.datasets import load_breast_cancer

#데이터불러오기
cancer = load_breast_cancer()
x = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = pd.DataFrame(cancer.target)

#train set, test set 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, random_state=123456)
# train_test_split(x, y, test_size, stratify, random_state)
# test_size : 테스트 데이터 사이즈
# train_size : 트레인 데이터 사이즈
# stratify : 클래스 라벨
# random_state : 난수 시드

#randomForest 실행, confusion matrix
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
# n_estimators : 생성할 트리의 개수
# oob_score : out-of-bag score, 예측이 얼마나 정확한가에 대한 추정을 수치로 나타낸 것
rf.fit(X_train, y_train)
# rf.fit(features, targets)
predicted_rf = rf.predict(X_test) 
#Confusion matrix 시각화
cm = pd.DataFrame(confusion_matrix(y_test, predicted_rf), columns=cancer.target_names, index=cancer.target_names)
sns.heatmap(cm, annot=True)


# 2. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 Boosting을 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2)
xgb.fit(X_train, y_train)
predicted_xgb = xgb.predict(X_test)

cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb), columns=cancer.target_names, index=cancer.target_names)
sns.heatmap(cm_xgb, annot=True)

#comment: xgboost의 예측정확도가 randomforest와 비교해 살짝 더 높다. 두 모델 모두 대체적으로 양성, 악성 분류가 잘 되었다고 판단된다.
