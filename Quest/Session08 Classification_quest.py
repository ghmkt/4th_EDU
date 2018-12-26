from numpy import *

def loadDataSet(): # 데이터 로드
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
                                  
def createVocabList(dataSet): # 데이터의 각 단어들을 중복없이 list형태로 반환
    vocabSet = set([])  # create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet): 
    # inputSet에 있는 word가 있으면 1 없으면 0인 vocabList길이의 벡터 반환
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

''' 안쓰임
def trainNB00(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pSpam = sum(trainCategory)/float(numTrainDocs)
    p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom
    p0Vect = p0Num/p0Denom
    return p0Vect,p1Vect,pSpam
'''

def trainNB0(trainMatrix,trainCategory): 
    # trainMatrix: 각 문장별 1,0 vec인 2차원 matrix / trainCategory: spam여부 1,0
    numTrainDocs = len(trainMatrix) # 문장 개수
    numWords = len(trainMatrix[0])  # 단어 개수
    pSpam = sum(trainCategory)/float(numTrainDocs) # Spam일 확률. 전체 문장 중 Spam인 문장 개수
    p0Num = ones(numWords); p1Num = ones(numWords) 
    # 0Num : ones * 전체 문장수, 1Num : ones * 전체 단어개수.
    p0Denom = 2.0; p1Denom = 2.0
    
    for i in range(numTrainDocs):
        # spam여부에서 한개씩 꺼냄.
        if trainCategory[i] == 1:          # spam이면
            p1Num += trainMatrix[i]        # p1Num에 i번째문장의 모든단어위치에 +1
            p1Denom += sum(trainMatrix[i]) # i번째문장의 모든단어수 합을 더함.
        else:                              # spam 아니면
            p0Num += trainMatrix[i]        # p0Num에 i번째문장의 모든단어위치에 +1
            p0Denom += sum(trainMatrix[i]) # i번째문장의 모든단어수 합을 더함.
    p1Vect = log(p1Num/p1Denom)            # log(스팸인 문장에서 나온 단어들의 빈도 정도 )
    p0Vect = log(p0Num/p0Denom)            # log(스팸아닌 문장의 단어들 빈도)

    # p0V,p1V는 음수. 절대값이 클 수록 빈도 낮다.
    return p0Vect,p1Vect,pSpam

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    # 사용 용도 :    if classifyNB(thisDoc, p0V, p1V, pSpam) == 1:
    
    # element-wise mult
    # 스팸일지 아닌지 비교할 때 쓰이는 수식
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)         
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    
'''안쓰임    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec
'''

def testingNB():
    listOPosts,listClasses = loadDataSet() # 데이터 불러오기
    myVocabList = createVocabList(listOPosts) # 위에서 불러온 데이터를 바탕으로 vocab List 만들기

    # trainMat에 데이터를 문장별로 전체 단어set중에서 해당되는 단어들이 1로 이루어진 벡터로 반환.
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    # print(str(trainMat)+'\n')

    # spam, not spam인 단어들 빈도 계산! & 전체중 spam인 문장의 비율
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(listClasses))
    
    # test1 문장 설정
    testEntry = ['free', 'pizza', 'coupon']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    
    #thisDoc, 즉, 내 테스트 문장은 스팸일까요?
    if classifyNB(thisDoc, p0V, p1V, pSpam) == 1:
        print(testEntry, 'classified this is a spam')
    else:
        print(testEntry, 'classified this is not a spam')

    # test2 문장 설정
    testEntry = ['I', 'will', 'miss','free', 'pizza']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))

    if classifyNB(thisDoc,p0V,p1V,pSpam) == 1:
        print(testEntry, 'classified this is a spam')
    else:
        print(testEntry, 'classified this is not a spam')

''' 여기부터 쭉 안쓰임
def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] 
    
def spamTest():
    docList=[]; classList = []; fullText =[]
    for i in range(1,26):
        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)#create vocabulary
    trainingSet = range(50); testSet=[]           #create test set
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error",docList[docIndex]
    print 'the error rate is: ',float(errorCount)/len(testSet)
    #return vocabList,fullText

def calcMostFreq(vocabList,fullText):
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True) 
    return sortedFreq[:30]       

def localWords(feed1,feed0):
    import feedparser
    docList=[]; classList = []; fullText =[]
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1) #NY is class 1
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)#create vocabulary
    top30Words = calcMostFreq(vocabList,fullText)   #remove top 30 words
    for pairW in top30Words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])
    trainingSet = range(2*minLen); testSet=[]           #create test set
    for i in range(20):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ',float(errorCount)/len(testSet)
    return vocabList,p0V,p1V

def getTopWords(ny,sf):
    import operator
    vocabList,p0V,p1V=localWords(ny,sf)
    topNY=[]; topSF=[]
    for i in range(len(p0V)):
        if p0V[i] > -6.0 : topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -6.0 : topNY.append((vocabList[i],p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    for item in sortedNY:
        print item[0]
'''

testingNB()
