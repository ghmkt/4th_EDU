# 제출 시 파일명은 Session12 이름 으로 해주세요.

# 1. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 RandomForest를 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
# 2. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 Boosting을 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부

import numpy as np
import pandas as pd
import seaborn as sns
# 
import xgboost
%matplotlib inline

from sklearn.datasets import load_breast_cancer

bc = load_breast_cancer()

# breast_cancer 데이터를 pandas의 dataframe으로 만들고, 데이터 형태를 살펴보자.
df = pd.DataFrame(bc.data, columns=bc.feature_names)
df.head()

# breast_cancer 데이터의 target은 classification을 위해 정수 형태(0, 1)로 되어 있음
# 시각화를 위해 target을 병 여부로 바꾼 새로운 열('yesno')을 df에 추가
# benign : 1, malignant : 0
df['yesno'] = np.array([bc.target_names[i] for i in bc.target])


# sklearn에서 train_test_split 함수 불러오기
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[bc.feature_names], bc.target, 
                                                    test_size=0.3, stratify=bc.target, random_state=123)

# train_test_split(x, y, test_size, stratify, random_state)
# test_size : 테스트 데이터 사이즈
# train_size : 트레인 데이터 사이즈
# stratify : 클래스 라벨
# random_state : 난수 시드

# sklearn에서 RandomForestClassifier 함수 불러오기
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
# n_estimators : 생성할 트리의 개수
# oob_score : out-of-bag score, 예측이 얼마나 정확한가에 대한 추정을 수치로 나타낸 것

rf.fit(X_train, y_train)
# rf.fit(features, targets)

# sklearn에서 accuracy_score 함수 불러오기
from sklearn.metrics import accuracy_score

predicted = rf.predict(X_test) # rf 모델에 X_test를 넣고 그 예측값을 predicted에 저장
accuracy = accuracy_score(y_test, predicted) # 실제 데이터와 예측값이 일치하는 비율

print(f'Out-of-bag score estimate: {rf.oob_score_:.3}')
print(f'Mean accuracy score: {accuracy:.3}')

# sklearn에서 confusion_matrix 함수 불러오기
from sklearn.metrics import confusion_matrix

cm = pd.DataFrame(confusion_matrix(y_test, predicted),
columns=bc.target_names, index=bc.target_names)
# confusion_matrix는 라벨이 있는 경우 분류 모델을 평가하는 방법
# column은 predicted, row는 y_test
sns.heatmap(cm, annot=True) # sns 라이브러리에 있는 heatmap으로 cm을 시각화

# benign은 정확히 분류해 내고 있지만, malignant 는 비율이 낮다.

xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2)
xgb.fit(X_train, y_train)

predicted_xgb = xgb.predict(X_test) # xgb 모델에 X_test를 넣고 그 예측값을 predicted에 저장
accuracy_xgb = accuracy_score(y_test, predicted_xgb) # 실제 데이터와 예측값이 일치하는 비율

print(f'Mean accuracy score: {accuracy_xgb:.3}')

cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb), 
                      columns=bc.target_names, index=bc.target_names)
sns.heatmap(cm_xgb, annot=True) # sns 라이브러리에 있는 heatmap으로 cm_xgb를 시각화

# 랜덤포레스트보다 예측 성능이 좋아질 줄 알았는데 이 데이터에서는 RF보다 성능이 낮다.
# malignant에서 예측률이 더 낮아졌다.

