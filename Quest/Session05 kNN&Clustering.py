# 제출 시 제목은 Session05 이름으로 해주세요!
# kNN&Clustering의 퀘스트 코드를 아래에 기입해주세요.

# 1. 파일명을 인자로 받아서 (1, 1024) 백터를 반환하는 함수를 정의하세요.

import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import operator
import os

def vec(x):
    os.chdir("C:\\Users\\승우\\Desktop\\Session05 kNN&Clustering_Quest\\Session05 kNN&Clustering\\trainingDigits")
    
    file = open(x,'r')
    #line = file.readline()
    #print(line[-1])
    #이를 통해, 매 줄의 마지막은 \n 처리되어 있음을 알 수 있습니다.
    #그렇다면 한 줄씩 읽어들이되, 맨 우측의 \n을 지우고 계속하여 붙이는 방식을 택하였습니다.
    
    line=''
    vector = []
    
    for i in range(0, int(1024/32)):
        line += file.readline().rstrip()
    
    for j in range(0, len(line)):
        vector += map(int, line[j])
        
    return vector    

#print(vec('0_0.txt'))   


# 2. 파일명을 인자로 받아서 Y값을 반환하는 함수를 정의하세요.

def yval(y):
    
    y_value = y[0]
    return y_value

#yval('0_0.txt')


# 3. 데이터를 X_train, y_train, X_test, y_test로 나누세요.

dir_path = "C:\\Users\\승우\\Desktop\\Session05 kNN&Clustering_Quest\\Session05 kNN&Clustering\\trainingDigits"
file_X = os.listdir(dir_path) 
#file_X 는 지금 파일 제목들의 리스트들을 담고 있습니다.
file_Y = []

for i in range(0, len(file_X)):
    file_Y += map(int, file_X[i][0])

#file_Y는 file_X로 부터 Y의, 즉 무슨 숫자를 나타내는 지에 관한 정보를 모두 빼낸 자료입니다.
#파일의 맨 앞글자만 따오면 굳이 파일을 열어보지 않더라도 그게 무슨 숫자인지 식별이 가능합니다.

#이제 file_X와 file_Y를 통해서 test split을 해주고자 합니다.
#X에 yet을 붙인 이유는, 전부 아직 파일명일 뿐 vec 함수를 통해 진짜 벡터 데이터셋에는 접근하지 않았기 때문입니다.

X_train_yet, X_test_yet, y_train, y_test = train_test_split(file_X, file_Y, test_size=0.3, random_state=0)
#len(X_train_yet) #1353개
#len(X_test_yet) #581개

X_train = []
X_test = []

for i in range(0, len(X_train_yet)):
    X_train.append(vec(X_train_yet[i]))
    
for j in range(0, len(X_test_yet)):
    X_test.append(vec(X_test_yet[j]))
     
#X_train, y_train, X_test, y_test 모두 도출


# 4. 1~10의 k에 대해 KNN을 시행하고 테스트셋에 대한 스코어를 그래프로 그리세요 (sklearn 이용)

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += (instance1[x] - instance2[x])**2
    return distance**0.5

def getNeighbors(X_train, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(X_train)):
        dist = euclideanDistance(testInstance, X_train[x], length)
        distances.append((x, dist))
    distances.sort(key=operator.itemgetter(1)) 
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
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
        if y_test[x] ==  predictions[x]:
            correct += 1
    return (correct/float(len(y_test))) * 100.0

for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    test_pred = knn.predict(X_test)
    accuracy = np.mean(np.array(y_test).astype(np.int32)== test_pred)
    print(k, ":", accuracy)
    
#최적의 k는 3인 것으로 결정

#http://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#sphx-glr-download-auto-examples-model-selection-plot-learning-curve-py
#내장되어있지는 않으나 learning_curve를 import 해주고, 다시금 함수를 정의해주어야만 그래프를 그릴 수 있었습니다.

from sklearn.model_selection import learning_curve

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    """
    Generate a simple plot of the test and training learning curve.

    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.

    cv : int, cross-validation generator or an iterable, optional
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
          - None, to use the default 3-fold cross-validation,
          - integer, to specify the number of folds.
          - An object to be used as a cross-validation generator.
          - An iterable yielding train/test splits.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : int or None, optional (default=None)
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    train_sizes : array-like, shape (n_ticks,), dtype float or int
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the dtype is float, it is regarded as a
        fraction of the maximum size of the training set (that is determined
        by the selected validation method), i.e. it has to be within (0, 1].
        Otherwise it is interpreted as absolute sizes of the training sets.
        Note that for classification the number of samples usually have to
        be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt

plot_learning_curve(estimator = knn , title = 'Graph', X = np.array(X_train) , y = np.array(y_train))
       
# 5. 최적의 K로 testdata에 넣어 정확도 측정

#최적의 k=3 accroding to #4

#1번에서 vec 함수를 trainingDigits 디렉토리에 한정해서 지정해주는 바람에, 부득이하게 vec2로, testDigits에 대한 함수를 다시 지정해주게 됐습니다.
#5번은, 필요에 따라 1,2, 3, 4번의 함수들을 그대로 사용하거나 조금씩만 변형했습니다. 
#Training, Test set들을, testDigits 파일의 목록에 대해서만 바꾸어주면 나머지 사고 과정은 다 똑같기 때문입니다. 

def vec2(x):
    os.chdir("C:\\Users\\승우\\Desktop\\Session05 kNN&Clustering_Quest\\Session05 kNN&Clustering\\testDigits")
    
    file = open(x,'r')
    
    line=''
    vector = []
    
    for i in range(0, int(1024/32)):
        line += file.readline().rstrip()
    
    for j in range(0, len(line)):
        vector += map(int, line[j])
        
    return vector    

def yval(y):
    
    y_value = y[0]
    return y_value


dir_path = "C:\\Users\\승우\\Desktop\\Session05 kNN&Clustering_Quest\\Session05 kNN&Clustering\\trainingDigits"
file_X_test = os.listdir(dir_path) 
file_Y_test = []

for i in range(0, len(file_X_test)):
    file_Y_test += map(int, file_X_test[i][0])

X_train_yet, X_test_yet, y_train, y_test = train_test_split(file_X_test, file_Y_test, test_size=0.3, random_state=0)

X_train = []
X_test = []

for i in range(0, len(X_train_yet)):
    X_train.append(vec2(X_train_yet[i]))
    
for j in range(0, len(X_test_yet)):
    X_test.append(vec2(X_test_yet[j]))

def main():
    predictions=[]
    k = 3
    for x in range(len(y_test)):
        neighbors = getNeighbors(X_train, X_test[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(y_test[x]))
    accuracy = getAccuracy(y_test, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

main()

