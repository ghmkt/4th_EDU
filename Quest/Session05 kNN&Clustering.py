# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.
import numpy as np
import pandas as pd
from os import listdir
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split



def file_vector(filename):
    with open('c:\\GH\\'+filename,'r') as f:
        lst=[]
        for line in f:
            line=line.strip()
            for i in line:
                lst.append(int(i))
           
    return(lst)

def file_y(filename):
    return filename[0] 

tr_h = listdir('c:\\GH\\trainingDigits')
te_h=listdir('c:\\GH\\testDigits')


X_train =[]
y_train =[]
for i in tr_h:
    X_train.append(file_vector('trainingDigits\\'+i))
    y_train.append(file_y(i))
X_test =[]
y_test =[]
for i in te_h:
    X_test.append(file_vector('testDigits\\'+i))
    y_test.append(file_y(i))


print(len(X_train), len(X_test), len(y_train), len(y_test))


for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy = np.mean(np.array(y_test)== test_pred)
    print(k, ":", accuracy)
    plt.scatter(k,accuracy,color='g',marker='x',label='score')
    plt.title('score chart for each k')
    plt.xlabel('score')
    plt.ylabel('accuracy')
    plt.grid(True)
plt.legend()
plt.show()
