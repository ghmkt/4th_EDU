from numpy import *

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
# 각 14개의 문장에서 어떤 걸 스팸으로 볼지 안볼지를 1과 0으로 지정해줌.

def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print ("the word: %s is not in my Vocabulary!" )% word
            # 파이썬 3버전이므로 괄호를 입혀줍니다.
    return returnVec
# 삽입하는 데이터를 document에 넣고 word2vec을 실행하여 단어간 유사성을 봅니다.


def trainNB00(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pSpam = sum(trainCategory)/float(numTrainDocs)
    # trainset의 단어의 개수와 스팸일 확률
    p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom #스팸일때(p1일때) 그 단어가 있을 확률
    p0Vect = p0Num/p0Denom #스팸이아닐때(p0일때) 그 단어가 있을 확률
    return p0Vect,p1Vect,pSpam # 위의2개와 스팸일 확률 3개의 확률을 보여줌.


def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pSpam = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect,p1Vect,pSpam
# p0Denom과 p1Denom의 디폴트를 2로올려 모델을 변경

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
# p1과 p0를 위와같은 모델로 설정하고, p1이 p0보다 크면 스팸, 작으면 no 스팸임을 정의해주는 함수


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec
#


def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    #print(str(trainMat))
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(listClasses))

    testEntry = ['free', 'pizza', 'coupon'] #free pizza coupon 이 3가지 단어를 얘네가 있으면 스팸, 없으면 스팸x인 기준으로 설정하고자함.
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))

    if classifyNB(thisDoc, p0V, p1V, pSpam) == 1:
        print (testEntry, 'classified this is a spam')
    else:
        print (testEntry, 'classified this is not a spam')
#그래서 myvocablist에 test entry 세단어가 관련이 되어있으면 스팸이라 print 없으면 스팸이 아니라고 print해줌.
    testEntry = ['I', 'will', 'miss','free', 'pizza']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))

    if classifyNB(thisDoc,p0V,p1V,pSpam) == 1:
        print (testEntry, 'classified this is a spam')
    else:
        print (testEntry, 'classified this is not a spam')
# 만들어진 모델에 free~ classified~ 2개의 문장을 넣어 테스트하여 그것이 spam인지 아닌지 판별.       


testingNB()
