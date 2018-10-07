# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.

import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

training_file_list = listdir('trainingDigits')
# print(len(training_file_list))

# 1번 문제
def return_vector(filename):
    filedir = 'C:\\Users\\Yang\\growthhacking\\trainingDigits\\'+filename
    df = pd.read_csv(filedir,sep=" ",header=None)
    vector = np.zeros((1,1024))
    for i in range(32):
        line = df.iloc[i,0]
        for j in range(32):
            vector[0,i*32+j]=line[j]
#    data = np.array(df)
    return vector.reshape(1024)


# 2번 문제
def return_Y(filename):
    f=int(filename[0])
    return f

  
# 3번 문제
X,y = [],[]
for i in range(len(training_file_list)): 
# for i in range(9): 
    filename = training_file_list[i]
    myv = return_vector(filename)
    myY = return_Y(filename)
    X.append(myv)
    y.append(myY)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 4번 문제
total_accuracy=[]
for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)
    total_accuracy.append(accuracy)

plt.plot(total_accuracy)
plt.show()

