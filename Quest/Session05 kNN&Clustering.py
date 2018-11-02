# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
training_file_list = listdir('C:/users/lg01/desktop/Session05 kNN&Clustering/trainingDigits')
test_file_list = listdir('C:/users/lg01/desktop/Session05 kNN&Clustering/testDigits')

# 1. 파일명을 인자로 받아서 (1, 1024) 백터를 반환하는 함수를 정의하세요.
def return_vector(filename):
    vector = np.zeros((1,1024))
    file = open('c:/users/lg01/desktop/Session05 kNN&Clustering/trainingDigits/'+filename)
    f1 = file.readline()
    f2 = file.readlines()
    for i in range(len(f1)):
        for j in range(len(f2)):
            vector[0,len(f2)*i+j] = int(f1[j])
    return vector
print(return_vector("0_23.txt"))

# 2. 파일명을 인자로 받아서 Y값을 반환하는 함수를 정의하세요.


# 3. 데이터를 X_train, y_train, X_test, y_test로 나누세요.


# 4. 1~10의 k에 대해 KNN을 시행하고 테스트셋에 대한 스코어를 그래프로 그리세요 (sklearn 이용)


# 5. 최적의 K로 testdata에 넣어 정확도 측정
