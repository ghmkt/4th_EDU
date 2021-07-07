# 제출 시 파일명은 Session12 이름 으로 해주세요.

# 1. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 RandomForest를 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부
# 2. 실습 코드를 활용하여 [scikit-learn의 기본 데이터 breast_cancer]에서 Boosting을 활용해 양성, 악성을 예측 => 코드 + confusion matrix 캡쳐본 첨부

#1. import library, load data, check data 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import xgboost

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

origin_data=load_breast_cancer()

df = pd.DataFrame(origin_data.data, columns=origin_data.feature_names)
df['target'] = np.array([origin_data.target_names[i] for i in origin_data.target])

#2. divide data into x, y + 3.split data into train set, test set
#사실 이 안에 divide data into x,y의 사고가 이미 들어가있다고 생각합니다.
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,0:-1], df.iloc[:,-1], 
                                                    test_size=0.3, stratify=df.iloc[:,-1], random_state=123456)

#4. use RandomForestClassifier and show confusion matrix 
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
rf.fit(X_train, y_train)

predicted_rf = rf.predict(X_test)
accuracy_rf = accuracy_score(y_test, predicted)
print(accuracy_rf) #0.9707602339181286 상당히 높은 예측력

ax1=plt.axes()
cm=pd.DataFrame(confusion_matrix(y_test, predicted), columns=origin_data.target_names, index=origin_data.target_names)
sns.heatmap(cm, annot=True)
ax1.set_title('RandomForestClassifier')
plt.show()
plt.clf()








#5. use XGBClassifier and show confusion matrix
xgb = xgboost.XGBClassifier(n_estimators=100, max_depth=2, random_state=123456)
xgb.fit(X_train, y_train)

predicted_xgb = xgb.predict(X_test)
accuracy_xgb = accuracy_score(y_test, predicted_xgb)
print(accuracy_xgb) #0.9473684210526315로 randomforest를 썼을 때보다 더 떨어졌다..?

ax2=plt.axes()
cm_xgb = pd.DataFrame(confusion_matrix(y_test, predicted_xgb), columns=origin_data.target_names, index=origin_data.target_names)
sns.heatmap(cm_xgb, annot=True)
ax2.set_title('XgboostClassifier')
plt.show()


#Xgboost를 사용했을 때보다, RandomForest를 사용했을 때 오히려 예측력이 더 높은데,
#물론 Xgboost를 사용했을 때의 예측력도 약 95%로 낮은 편은 아니지만
#설명력이 높은 변수들의 영향력이 워낙에 높아, 잔차를 줄여나가는 형식보다 RandomForest가 더 효율적이었던 것으로 보입니다. 



