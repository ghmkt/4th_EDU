# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.

import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# 1. 파일명을 인자로 받아서 (1, 1024) 백터를 반환하는 함수를 정의하세요.

def file_to_vector(filename):
    v = np.zeros((1,1024))
    ff = open('c:\\trainingDigits\\'+filename)
    for i in range(len(ff.readline())):
        f_line = ff.readline()
        for j in range(len(ff.readlines())):
            v[0,len(ff.readlines())*i+j] = int(f_line[j])
    return v

# 2. 파일명을 인자로 받아서 Y값을 반환하는 함수를 정의하세요.

def file_to_y(filename):
    filename2 = filename.split('.')[0]
    y = int(filename2.split('_')[0])
    return y
    
# 3. 데이터를 X_train, y_train, X_test, y_test로 나누세요.

X = []
Y = []
for i in range(len(training_file_list)):
    X.append(file_to_vector(training_file_list[i]))
    Y.append(file_to_y(training_file_list[i]))
   
X = np.array(X).reshape(-1,1024)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

print(len(X_train), len(X_test), len(y_train), len(y_test))

# 4. 1~10의 k에 대해 KNN을 시행하고 테스트셋에 대한 스코어를 그래프로 그리세요 (sklearn 이용)

accuracy = []
for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy.append(np.mean(np.array(y_test).astype(np.int32)== test_pred))
    
plt.xlabel('k')
plt.ylabel('accuracy')
plt.plot(range(1,11), accuracy)

# 5. 최적의 K로 testdata에 넣어 정확도 측정

testDigits = 'c:\\testDigits'
test_file_list = listdir(testDigits)

X2 = []
Y2 = []
for i in range(len(test_file_list)):
    X2.append(file_to_vector(test_file_list[i]))
    Y2.append(file_to_y(test_file_list[i]))
X2 = np.array(X2).reshape(-1,1024)

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, Y2, test_size=0.3, random_state=0)


k = 9
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X2_train, y2_train)
test_pred = knn.predict(X2_test)
accuracy = np.mean(np.array(y2_test).astype(np.int32)== test_pred)

accuracy
