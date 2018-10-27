# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.

import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import sklearn
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

training_file_list = listdir('trainingDigits')

# 1. 파일명을 인자로 받아서 (1, 1024) 백터를 반환하는 함수를 정의하세요.
# 2. 파일명을 인자로 받아서 Y값을 반환하는 함수를 정의하세요.

def xy_value(txt_file_name):
    r = open('/Users/daham/Desktop/GrowthHackers/4th-EDU/Quest/Session05 kNN&Clustering/trainingDigits/{}'.format(txt_file_name), mode='rt', encoding='utf-8')
    tmp = r.read()
    r.close()
    return (np.array(list(tmp.replace('\n', ''))), int(txt_file_name[0]))


# 3. 데이터를 X_train, y_train, X_test, y_test로 나누세요.

X = [xy_value(x)[0] for x in training_file_list]
Y = [xy_value(x)[1] for x in training_file_list]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# 4. 1~10의 k에 대해 KNN을 시행하고 테스트셋에 대한 스코어를 그래프로 그리세요 (sklearn 이용)

x_axis = []
y_axis = []
for k in range(1,11):
    neigh = KNeighborsClassifier(n_neighbors=k)
    neigh.fit(X_train, y_train)
    test_pred = neigh.predict(X_test)
    accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)
    x_axis.append(k)
    y_axis.append(accuracy)
    
plt.plot(x_axis, y_axis, 'g')

# 5. 최적의 K로 testdata에 넣어 정확도 측정
neigh = KNeighborsClassifier(n_neighbors=6)
neigh.fit(X_train, y_train)
test_pred = neigh.predict(X_test)
accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)

print(accuracy)
