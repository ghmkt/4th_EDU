#특정 단어가 메일에 있을 때 그 메일이 스팸일 확률 구하기

from numpy import *


#loadDataSet이라는 함수로, postingList와 classVec을 return하는데
#postingList의 14개의 메일들에 대해 spam인지 아닌지 1,0으로 할당
#예를 들어, 'I', 'got' ~ 'boy', 'friend'는 첫번째 메일 안에 들어 있는 문구들
def loadDataSet():
    postingList=[['I', 'got', 'free', 'two', 'movie', 'ticket', 'from', 'your', 'boy', 'friend'],
                 ['free', 'coupon', 'from', 'xx.com'],
                 ['watch', 'free', 'new', 'movie', 'from', 'freemovie.com'],
                 ['best', 'deal', 'promo', 'code', 'here'],
                 ['there', 'will', 'be', 'free', 'pizza', 'during', 'the', 'meeting'],
                 ['scheduled', 'meeting', 'tomorrow'],
                 ['can','we','have','lunch','today'],
                 ['I','miss','you'],
                 ['thanks','my','friend'],
                 ['it','was','good','to','see','you','today'],
                 ['free','coupon','last','deal'],
                 ['free','massage','coupon'],
                 ['I','sent','the','coupon','you','asked','it','is','not','free'],
                 ['coupon','promo','code','here']]
    classVec = [0,1,1,1,0,0,0,0,0,0,1,1,0,1]    #1 is spam, 0 not
    return postingList,classVec

#후에 분명 createVocabList 함수의 dataSet자리에 postingList의 값들이 들어가게 될 것
#postingList의 14개 메일들의 개별 element들 각각을 모두 뽑아 하나의 리스트로 만드는 과정.
#즉 return 값에는 potingList 안에 있는 모든 개별적 단어들이 하나의 리스트 안에 담기게 된다.
#(합집합이니 예를 들어, 여러 번 등장한 I는 vocabSet에서는 하나의 I로 표시되어 나타남 )
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

#inputSet, 즉 input해준 단어가 vocabList에 있는 경우 해당 vocabList의 숫자를 0에서 1로 바꾸어준다. 
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList) #vacabList의 길이만큼의 자리를 만드는 것. 어차피 0으로 다 채워놓고 1로 바꿀 것들은 나중에 바꾸면 됨.
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

def trainNB00(trainMatrix,trainCategory): 
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0]) 
    pSpam = sum(trainCategory)/float(numTrainDocs) 
    p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Denom = 0.0; p1Denom = 0.0 
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i] [1,...,1](1 10개짜리)
            p1Denom += sum(trainMatrix[i])#그 리스트에서 element들의 합 (1,0이니까 합은 곧 1의 개수일 것)
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom
    p0Vect = p0Num/p0Denom
    return p0Vect,p1Vect,pSpam

def trainNB0(trainMatrix,trainCategory): #rainMatrix 자리에 array(trainMat), trainCategory 자리에 array(listClasses) 가 들어가
    numTrainDocs = len(trainMatrix) #numTrainDocs는 14
    numWords = len(trainMatrix[0])  #numWords는 I got free...즉 전체 단어의 개수: 49개(모든 메일들 총망라, 단 중복되는 것들은 하나로 침에 주의)
    #len(trainMatrix[0])이나 len(trainMatrix[1])이나 그 결과값은 같을 것
    pSpam = sum(trainCategory)/float(numTrainDocs) #spam메일일 확률: 전체 14개 메일 중에서 spam인 메일은 몇 개인가?
    p0Num = ones(numWords); p1Num = ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    #1과 2가 기존값으로 설정된 것을 보니 이 과정은 분명 smooting과정 (Session 18페이지)
    for i in range(numTrainDocs): #14번을 돌아
        if trainCategory[i] == 1: #만약에 spam인 메일이면?
            p1Num += trainMatrix[i] #i번째 메일에서 [1,1...(전체 단어 개수개),...1]에 다가 [0,1...]의 조합으로 표현된 애들 더해 줘~
            #예를 들어, spam메일이 4번 등장했는데, spam 메일들 중'I'라는 단어가 2번 등장했다면 'I'라는 단어에 해당하는 p1Num값은 1+2가 될 것
            p1Denom += sum(trainMatrix[i]) #2 + 스팸메일에 등장한 단어들의 총 개수
        else: #만약에 spam이 아닌 document라면?
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
            #똑같은 과정을 spam메일일 때, spam이 아닌 메일일 때를 분리해서 생각해주는 중
    p1Vect = log(p1Num/p1Denom) #spam메일에서 각 단어들이 1+등장한 횟수를, spam 내의 2+총단어수로 나누어주고 log  (분명 벡터)
    p0Vect = log(p0Num/p0Denom) #spam이 아닌 메일에서 각 단어들이 1+등장한 횟수를, spam이 아닌 메일 내의 2+총단어수로 나누어주고 log
    return p0Vect,p1Vect,pSpam

#각 argument들에 순서대로 thisDoc, p0V, p1V, pSpam가 들어가게 될 것
#thisDoc은 전체 vocab list에서 free, pizza, coupon 가 있는 부분만 1, 나머지는 0으로 나타난 것
#스팸이고 아니고의 판단 기준
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

#아래에서 실행해주는 부분은 testingNB 이부분 (testingNB())
def testingNB():
    listOPosts,listClasses = loadDataSet() #list0Posts는 postingList(:각 메일)를, listClasses는 classVec(1,0으로 스팸 여부 표시)을 객체로 받는다.
    myVocabList = createVocabList(listOPosts) #list0Posts 내 14개의 메일내의 모든 단어들을 하나의 리스트로 만든다.
    #myvocbList는 49개의 단어들을 포함하고 있음
    #words=set([])
    #for i in range(0, len(postingList)):
        #words = words | set(postingList[i])
    #len(words)
    trainMat=[] #trainMat이라는 빈 리스트를 하나 만들어 주고, (이 리스트 안에 집어넣을 것) 
    for postinDoc in listOPosts: #list0Posts 안에 있는 모든 단어
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    #list0Posts를 구성하고 있는 14개의 리스트들(메일 목록)을 iterate.
    #return값은 14개의 리스트이며, 각 리스트는, 각 인덱스의 postinDoc 내의 단어들이 myVocabList에 있는 자리만 1로 바뀌어 나타남.
    #예를들어, myVocabList는 ['I', 'got', ... 'here']로 이루어지는데
    #trainMat의 첫번째 리스트에서는 'I'가 포함된 해당 index의 0이 1로 바뀌어 나타나

    #지금 trainMat은 14개의 list를 포함하고 있다.
    #지금 listClasses는 각 메일마다 0혹은 1을 대응시킨, 총 14개의 개별 value로 구성된 하나의 리스트이다. (spam인지 아닌지를 구분하는 역할)
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(listClasses))
    #p0V: spam메일에서 각 단어들이 1+등장한 횟수를, spam 내의 2+총단어수로 나누어주고 log  (분명 벡터)
    #P1v: spam이 아닌 메일에서 각 단어들이 1+등장한 횟수를, spam이 아닌 메일 내의 2+총단어수로 나누어주고 log (역시 벡터)
    #PsPAM: 스팸메일일 확률

    testEntry = ['free', 'pizza', 'coupon'] #이 단어들이 메일을 스팸으로 분류하는 기준.
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry)) #전체 vocab list에서 free, pizza, coupon 가 있는 부분만 1, 나머지는 0으로 나타남

    if classifyNB(thisDoc, p0V, p1V, pSpam) == 1:
        print testEntry, 'classified this is a spam'
    else:
        print testEntry, 'classified this is not a spam'

    testEntry = ['I', 'will', 'miss','free', 'pizza'] #또, 이 단어들로 테스트
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))

    if classifyNB(thisDoc,p0V,p1V,pSpam) == 1:
        print testEntry, 'classified this is a spam'
    else:
        print testEntry, 'classified this is not a spam'
        
        
#testingNB 함수 안에 들어있지 않은 부분은 데이터 전처리 부분이며,
#testingNB 안에 해당되는 함수들과 관련해서만 작성하면 된다고 들었습니다!
