import numpy as np
from numpy import *
from os import listdir
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import operator
import pandas as pd
training_file_list = listdir('trainingDigits')

# 1. 파일명을 인자로 받아서 (1, 1024) 백터를 반환하는 함수를 정의하세요.
def file_to_vector(file):
    file_path = "trainingDigits\\" + file
    with open(file_path, 'r') as f:
        numbers = f.read()
        numbers = numbers.replace("\n","")
        number_list = [int(i) for i in numbers]
        vector = number_list
        return vector
    
# 2. 파일명을 인자로 받아서 Y(숫자 몇이니?)값을 반환하는 함수를 정의하세요.
def file_to_y(file):
    return int(list(file)[0])

X = []
Y = []
for file in training_file_list:
    Y.append(file_to_y(file))
    X.append(file_to_vector(file))
# 3. 데이터를 X_train, y_train, X_test, y_test로 나누세요.
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
# 4. 1~10의 k에 대해 KNN을 시행하고 테스트셋에 대한 스코어를 그래프로 그리세요 (sklearn 이용)
accuracy = {}
import sklearn
from sklearn.neighbors import KNeighborsClassifier
k_accuracy = []
for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)
    print(k, ":", accuracy)
    k_accuracy.append((k, accuracy))
    
    print(k_accuracy)
k_list = []
accuracy_list = []
for x,y in k_accuracy:
    k_list.append(x)
    accuracy_list.append(y)
print(k_list, accuracy_list)
    
plt.scatter(k_list, accuracy_list, color = 'skyblue', label = 'accuracy')
plt.title('how accuracy change by # of k' )
plt.xlabel('number of k')
plt.ylabel('accuracy')
plt.ylim(0.95, 0.98)
plt.legend()
plt.show()
test_file_list = listdir('testDigits')

def file_to_vector_2(file):
    file_path = "testDigits\\" + file
    with open(file_path, 'r') as f:
        numbers = f.read()
        numbers = numbers.replace("\n","")
        number_list = [int(i) for i in numbers]
        vector = number_list
        return vector
X = []
Y = []

for file in test_file_list:
    Y.append(file_to_y(file))
    X.append(file_to_vector_2(file))
    
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)
test_pred = knn.predict(X)
accuracy = np.mean(np.array(Y).astype(np.int32)== test_pred)
print(accuracy)
