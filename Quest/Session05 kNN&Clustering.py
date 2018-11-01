# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.

import numpy as np
import os
from os import listdir
import matplotlib.pyplot as plt
import sklearn
import operator
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
os.chdir(r'C:\Users\EdwinPark')
training_file_list = listdir('trainingDigits')
print(len(training_file_list))

# 1. 파일명을 인자로 받아서 (1, 1024) 백터를 반환하는 함수를 정의하세요.

#1번 응답
def txt_to_list(x):
    with open(x, 'r') as f:
        mylist = [line.strip() for line in f]
        # 읽은 txt파일을 공백없이 나열!
        mylist=''.join(mylist)
        # 리스트 원소들을 경계없이 하나의 원소로 통합! 
        mylist=list(mylist)
        mylist2=[]
        mylist2.append(mylist)
    return mylist2

def txt_to_vec(x):
    myarray= np.asarray(txt_to_list(x))
    return myarray
  #리스트를 벡터로!
  # 두 함수를 따로 만든 이유는 train, test set 만들 때 리스트들을 모아서 하나의 벡터로 만들기 위함...

# 2. 파일명을 인자로 받아서 Y값을 반환하는 함수를 정의하세요.
#2 번 응답
def y_value(x):
    return x[0]
#파일 이름을 str으로 읽어주기 때문에 파일 이름의 첫글자가 Y값이므로 string의 첫글자를 읽어주면 된다.

# 3. 데이터를 X_train, y_train, X_test, y_test로 나누세요.

#3번 응답

# X train set 만들기
os.chdir(r'C:\Users\EdwinPark')
training_file_list = listdir('trainingDigits')
os.chdir(r'C:\Users\EdwinPark\trainingDigits')
X_train=[]
for i in range(0,len(training_file_list)):
    X_train.extend(txt_to_list(training_file_list[i]))
X_train= np.asarray(X_train).astype(np.int)
#training_file_list의 각 txt파일들을 리스트로 변환한것들을 원소로 하는 벡터 생성
#여기서 txt파일을 읽을때 0,1들을 str_로 읽기 때문에 knn을위해 int로 바꿔줌(.astype(np.int)) 
#밑에 3개도 위와 동일!
        
# Y train set 만들기
y_train=[]
for i in range(0,len(training_file_list)):
    y_train.extend(y_value(training_file_list[i]))
y_train=np.asarray(y_train).astype(np.int)
    
# X test set 만들기
os.chdir(r'C:\Users\EdwinPark')
test_file_list = listdir('testDigits')
os.chdir(r'C:\Users\EdwinPark\testDigits')
X_test=[]
for i in range(0,len(test_file_list)):
    X_test.extend(txt_to_list(test_file_list[i]))
X_test= np.asarray(X_test).astype(np.int)

# Y test set 만들기
y_test=[]
for i in range(0,len(test_file_list)):
    y_test.extend(y_value(test_file_list[i]))
y_test=np.asarray(y_test).astype(np.int)

print(len(X_train), len(X_test), len(y_train), len(y_test))

# 4. 1~10의 k에 대해 KNN을 시행하고 테스트셋에 대한 스코어를 그래프로 그리세요 (sklearn 이용)

#4번 응답

import sklearn
from sklearn.neighbors import KNeighborsClassifier

for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)
knumbers=list(range(1,11))

plt.plot(knumbers, accuracy) 
plt.show() 

# --> K=3 일 때 가장 accuracy가 높다는 것을 알 수 있음!


# 5. 최적의 K로 testdata에 넣어 정확도 측정

#5번 응답

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += (instance1[x] - instance2[x])**2
    return distance**0.5
#거리구하는 함수
  
def getNeighbors(X_train, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(X_train)):
        dist = euclideanDistance(testInstance, X_train[x], length)
        distances.append((x, dist))
    distances.sort(key=operator.itemgetter(1)) # dist를 기준으로 sort하자
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0]) # X_train에서 가까운 원소의 인덱스를 저장
    return neighbors
  
def getResponse(neighbors):
    classVotes = {}
    for x in neighbors:
        response = y_train[x]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(y_test, predictions):
    correct = 0
    for x in range(len(y_test)):
        if y_test[x] == predictions[x]:
            correct += 1
    return (correct/float(len(y_test))) * 100.0

def main():
    predictions=[]
    k = 3
    #아까 구했던 최적의 K =3을 넣음
    for x in range(len(y_test)):
        neighbors = getNeighbors(X_train, X_test[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
    accuracy = getAccuracy(y_test, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

main()
