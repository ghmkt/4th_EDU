from numpy import *



def loadDataSet(): #postinglist라는 14개의 리스트를 갖는 리스트 중 2,3,4,11,12,14 는 스팸 임을 나타내는 함수

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
loadDataSet()

def createVocabList(dataSet): #각 문장 하나하나를 합친 후 중복 제거하고 단어 하나씩 일자로 리스트를 만들어주는 친구

    vocabSet = set([])  #create empty set

    for document in dataSet:

        vocabSet = vocabSet | set(document) #union of the two sets

    return list(vocabSet)


a,b=loadDataSet()  #필자가 그냥 실험해본 부분
createVocabList(a)

print(len(a),len(createVocabList(a)))

lst=[]
for i in a[0]:   #필자가 그냥 실험해본 부분
    if i in createVocabList(a):
        print(createVocabList(a).index(i))

def setOfWords2Vec(vocabList, inputSet):#일렬로 된 단어 리스트와 각 메일 한단위씩을 넣는 함수이고 

    returnVec = [0]*len(vocabList) #0을 일렬로 된 단어 리스트의 개수 만큼 (중복제거한 것) 써준다

    for word in inputSet:

        if word in vocabList:#각 메일에 있는 단어 하나하나가 일렬로 된 단어 리스트 안에 있으면 

            returnVec[vocabList.index(word)] = 1 #일렬로 된 리스트 중 해당 단어가 있는 index 부분을 1로 변환해준다.

        else: print ("the word: %s is not in my Vocabulary!" % word)

    return returnVec #전체 단어를 본 딴 리스트 중 결과적으로 각 메일에 있는 단어 부분만 1로 변한 f,t리스트를 반환해줄 것 

def trainNB00(trainMatrix,trainCategory):

    numTrainDocs = len(trainMatrix)#메일 수 인 14개

    numWords = len(trainMatrix[0])# 중복 제거한 단어 수 총 49개

    pSpam = sum(trainCategory)/float(numTrainDocs) #총 실제 스팸 메일의 개수를 14로 나눈 것. 즉 메일 이 스팸일 확률

    p0Num = zeros(numWords); p1Num = zeros(numWords) #단어 수 49개로 0.0 꼴 리스트를 두개 만들었다

    p0Denom = 0.0; p1Denom = 0.0

    for i in range(numTrainDocs):#매우 중요한 부분인데 실제 스팸일 때 스팸에 있는 단어 개수를 총합하고 단어 인덱스를 누적해서 쌓아준다
        #(반복해서 나오면 인덱스 계속 올라감)

        if trainCategory[i] == 1:

            p1Num += trainMatrix[i]

            p1Denom += sum(trainMatrix[i])

        else:

            p0Num += trainMatrix[i]

            p0Denom += sum(trainMatrix[i])

    p1Vect = p1Num/p1Denom #총 단어 개수로 각 단어 등장 횟수 리스트를 나눈 것. 즉, 스팸일 때 각 단어가 등장할 확률을 리스트로 표현 한 것이다. 

    p0Vect = p0Num/p0Denom#스팸 아닐 때 각 단어가 등장할 확률을 리스트로 표현

    return p0Vect,p1Vect,pSpam



def trainNB0(trainMatrix,trainCategory): #위 함수랑 다른 점이 모든 단어 등장 개수 최소 1개로 스무딩 해주고 결과값을 로그취해줌 

    numTrainDocs = len(trainMatrix)

    numWords = len(trainMatrix[0])

    pSpam = sum(trainCategory)/float(numTrainDocs)

    p0Num = ones(numWords); p1Num = ones(numWords)

    p0Denom = 2.0; p1Denom = 2.0 #단어 등장 횟수의 총합에 2를 더해준다 이 역시 k=1인 스무딩의 방법

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



def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):

    p1 = sum(vec2Classify * p1Vec) + log(pClass1)#대입한t,f리스트를 받아 각 단어들의 스팸일때 등장 확률을 더하고 로그스팸 확률을 합

    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)

    if p1 > p0:# 스팸일 때 등장할 확률의 합과 스팸아닐때 등장할 확률의 합의 차이와 스팸일 확률과 스팸 아닐 확률의 차이보다 클 때 1

        return 1

    else: 

        return 0


def testingNB():

    listOPosts,listClasses = loadDataSet() #각각 처음 데이터셋의 글자 리스트와 스팸여부

    myVocabList = createVocabList(listOPosts)

    trainMat=[] 

    for postinDoc in listOPosts:#첫 데이터셋의 각 메일마다 setof함수에 넣어서 49중 t,f로 변환된 리스트를 trainMat에 붙인다 

        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

    #print(str(trainMat))

    p0V,p1V,pSpam = trainNB0(array(trainMat),array(listClasses))#49개씩 14개 있는 것과 14개 원소를 가진 진실 스팸 여부를 넣어
    #스팸아닐때 각 단어의 등장 확률과 스팸일때 각 단어의 등장 확률 그리고 메일이 스팸일 확률을 할당



    testEntry = ['free', 'pizza', 'coupon']

    thisDoc = array(setOfWords2Vec(myVocabList, testEntry)) #예시 단어가 있냐 없냐로 49 중 t,f 변환된 리스트로 만듦.



    if classifyNB(thisDoc, p0V, p1V, pSpam) == 1:

        print testEntry, 'classified this is a spam'

    else:

        print testEntry, 'classified this is not a spam'



    testEntry = ['I', 'will', 'miss','free', 'pizza']

    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))



    if classifyNB(thisDoc,p0V,p1V,pSpam) == 1:

        print testEntry, 'classified this is a spam'

    else:

        print testEntry, 'classified this is not a spam'





def textParse(bigString):    #input is big string, #output is word list

    import re

    listOfTokens = re.split(r'\W*', bigString) #문자열을 넣고 모든 문자를 제외한 기호가 한번이라도 나오면 그 것을 제외하고 
    #그 것을 기준으로 문자열을 리스트의 각 원소로 분리시켜준다. 

    return [tok.lower() for tok in listOfTokens if len(tok) > 2] 
    #각 단어의 글자수가 3개 이상일 경우 소문자화 시켜주는 처리를 추가해 문자열 리스트를 뱉는다.
    

setOfWords2Vec(createVocabList(a),a[0])

listOPosts,listClasses = loadDataSet() #각각 처음 데이터셋의 글자 리스트와 스팸여부

myVocabList = createVocabList(listOPosts)

trainMat=[]

for postinDoc in listOPosts:#첫 데이터셋의 각 메일마다 setof함수에 넣어서 49중 t,f로 변환된 리스트를 trainMat에 붙인다 

    trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

len(array(trainMat[0])),array(listClasses)


 trainingSet = range(50); testSet=[] #필자가 그냥 실험해본 부분
testSet
int(random.uniform(0,len(trainingSet)))
trainingSet[10]









def bagOfWords2VecMN(vocabList, inputSet):#일렬로 된 단어 리스트에 있는 만큼 더한다 1초과 할 수 있다는 점에서 차이점.

    returnVec = [0]*len(vocabList)

    for word in inputSet:

        if word in vocabList:

            returnVec[vocabList.index(word)] += 1

    return returnVec



def spamTest():

    docList=[]; classList = []; fullText =[]

    for i in range(1,26):#파일이 25개 있고 각각이 한 메일이라 볼 건가 봄 
        wordList = textParse(open('email/spam/%d.txt' % i).read())

        docList.append(wordList) #listO 뭐시기랑 같은 형태임을 유의. 즉, 리스트 안에 단어들 있는 리스트 포함 된 것.

        fullText.extend(wordList) #extend는 append와 달리 리스트 추가가 아니라 하나의 리스트 속에 늘려주는 개념 

        classList.append(1) #스팸이냐 여부를 1,0,1,0 이런식으로 설정해놓음

        wordList = textParse(open('email/ham/%d.txt' % i).read())

        docList.append(wordList)

        fullText.extend(wordList)

        classList.append(0)

    vocabList = createVocabList(docList)#create vocabulary

    trainingSet = range(50); testSet=[]           #create test set

    for i in range(10):

        randIndex = int(random.uniform(0,len(trainingSet))) #0에서 50 사이 랜덤 정수

        testSet.append(trainingSet[randIndex]) #testset을 길이 10의 랜덤 정수 리스트로 만듦

        del(trainingSet[randIndex])  

    trainMat=[]; trainClasses = []

    for docIndex in trainingSet:#train the classifier (get probs) trainNB0

        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))#각 doclist안 메일의 단어들이 포함되있나 아닌가를
        #횟수로 표현한 리스트를 계속 더해준다

        trainClasses.append(classList[docIndex])#클래스 리스트의 순서대로 쭉 클래스 리스트에서 그대로 가져온다

    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))

    errorCount = 0

    for docIndex in testSet:        #classify the remaining items

        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex]) #classifyNB를 통해 예측한 결과와 실제를 비교하여 
        #다를 때마다 에러를 내고 마지막에 에러율을 계산해준다.

        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:

            errorCount += 1

            print "classification error",docList[docIndex]

    print 'the error rate is: ',float(errorCount)/len(testSet)

    #return vocabList,fullText



def calcMostFreq(vocabList,fullText):

    import operator

    freqDict = {}

    for token in vocabList:

        freqDict[token]=fullText.count(token) #freqdict이란 딕셔너리에 단어 이름과 숫자를 각각 키와 밸류로 넣어준다

    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True) #밸류인 등장 수를 기준으로 높은순정렬

    return sortedFreq[:30]       



def localWords(feed1,feed0):

    import feedparser #feedparser는 파이썬에서 쓸 수 있는 rss파서이다

    docList=[]; classList = []; fullText =[]

    minLen = min(len(feed1['entries']),len(feed0['entries'])) #각각 입력 변수의 entries의 길이 중 작은 것을 선택

    for i in range(minLen): #textParse 내장함수를 이용하여 단어리스트를 뽑아내고  

        wordList = textParse(feed1['entries'][i]['summary'])

        docList.append(wordList) #doctlist는 append로 리스트 단위로 만들었고 

        fullText.extend(wordList) #fulltext는 extend로 합쳐서 하나로 만들었다

        classList.append(1) #NY는 spam이란 것을 말한다

        wordList = textParse(feed0['entries'][i]['summary'])

        docList.append(wordList)

        fullText.extend(wordList)

        classList.append(0)#sf는 spam이 아니란 것을 말한다

    vocabList = createVocabList(docList)# 우리가 잘 아는 중복제거한 일자 단어리스트를 만든다 

    top30Words = calcMostFreq(vocabList,fullText)   #가장 빈번한 단어를 30개 없앤다. 이는 너무 공통적으로 나오는 단어가
    #통계에 영향을 미치는 것을 배제하기 위함이 아닐까 생각한다.

    for pairW in top30Words: #이때 [0]을 쓴 것은 단어:빈도수의 딕셔너리 형태로 되어있기 때문에 단어를 추출한 것

        if pairW[0] in vocabList: vocabList.remove(pairW[0])

    trainingSet = range(2*minLen); testSet=[]           #create test set

    for i in range(20): #마찬가지 방법으로 trainingset을 만든다

        randIndex = int(random.uniform(0,len(trainingSet)))

        testSet.append(trainingSet[randIndex])

        del(trainingSet[randIndex])  

    trainMat=[]; trainClasses = []

    for docIndex in trainingSet:#마찬가지로 스팸아닐때 각 단어의 등장 확률과 스팸일때 각 단어의 등장 확률 그리고 메일이 스팸일 확률구함
        
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))

        trainClasses.append(classList[docIndex])

    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))

    errorCount = 0

    for docIndex in testSet:        #동일한 방법으로 에러일 확률을 구한다

        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])

        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:

            errorCount += 1

    print 'the error rate is: ',float(errorCount)/len(testSet)

    return vocabList,p0V,p1V



def getTopWords(ny,sf): #드디어 마지막 함수이다. 

    import operator

    vocabList,p0V,p1V=localWords(ny,sf) #이때 아까 스무딩했고 로그 함수 취했던 값이라는 것을 기억하자

    topNY=[]; topSF=[]

    for i in range(len(p0V)):#필자가 대충 계산한 값을 통해 볼 때 0.25의 확률이 나오면 top리스트에 추가한다

        if p0V[i] > -6.0 : topSF.append((vocabList[i],p0V[i]))

        if p1V[i] > -6.0 : topNY.append((vocabList[i],p1V[i]))

    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True) #가장 많이 나온 놈 순으로 정렬

    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"

    for item in sortedSF:

        print item[0] #스팸아닌 것에서 가장 많이 나온 단어순으로 리스트 출력

    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)

    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"

    for item in sortedNY:

        print item[0] #스팸에서 가장 많이 나온 단어순으로 리스트 출력 
        
        
        #힘들었다



testingNB()
