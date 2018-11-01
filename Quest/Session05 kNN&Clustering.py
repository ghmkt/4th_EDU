# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.

# 1. 파일명을 인자로 받아서 (1, 1024) 백터를 반환하는 함수를 정의하세요.
# 2. 파일명을 인자로 받아서 Y값을 반환하는 함수를 정의하세요.

def xy_generator(a):
    file = "C:\\Users\\renoi\\Session05 KNN Quest\\Session05 kNN&Clustering\\trainingDigits\\" + "0_23.txt"
    f = open(file)
    data = f.read()
    data = data.replace("\n", "")
    data_arr = np.array(list(data))
    b = int(a[0])
    return (data_arr, b)

 # 3. 데이터를 X_train, y_train, X_test, y_test로 나누세요.

X_train = [xy_generator(a)[0] for a in training_file_list]
X_test = [xy_generator(a)[0] for a in test_file_list]
Y_train = [xy_generator(a)[1] for a in training_file_list]
Y_test = [xy_generator(a)[1] for a in test_file_list]

# 4. 1~10의 k에 대해 KNN을 시행하고 테스트셋에 대한 스코어를 그래프로 그리세요 (sklearn 이용)

import sklearn
from sklearn.neighbors import KNeighborsClassifier      
from matplotlib import pyplot as plt

accuracy_list = []
for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)
    print(k, ":", accuracy)
    accuracy_list = accuracy_list.append(accuracy)
    
k_list = list(range(1,11))
    
plt.plot(k_list, accuracy_list, marker = 'x')
plt.xlabel('k') 
plt.ylabel('accuracy')

# 5. 최적의 K로 testdata에 넣어 정확도 측정

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)
    print(accuracy)
