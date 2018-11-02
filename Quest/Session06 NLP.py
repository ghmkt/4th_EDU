# 제출시 파일명은 Session06 이름 으로 해주세요.

# 1. LDA 코드를 활용하여 본인이 원하는 텍스트를 넣어 보기 => 텍스트 원본 파일 + LDA 결과 첨부 + 본인 결과 해석

import random
from collections import Counter
import nltk
import konlpy
from konlpy.tag import Kkma;kkma=Kkma()
from konlpy.tag import Twitter;twitter=Twitter()

def txt_to_nouns(txt):
    with open(txt, "r") as raw:
        string=raw.read()
    tag = twitter.pos(string)
    nouns=[]
    for i in range(0,len(tag)):
        if tag[i][1] == 'Noun':
            nouns.append(tag[i])
    # tag가 noun인 것들만 추출!
    nouns_list=[]
    for i in range(0,len(nouns)):
        nouns_list.append(nouns[i][0])
    return nouns_list
    #처음에는 Kkma 로 해보았지만 명사 추출이 Twitter가 더 잘된다고 느껴서 바꾸었습니다.
 
poli_nouns_list=txt_to_nouns("polinews.txt") #크롤링 퀘스트에서 쓴 정치뉴스 텍스트파일
wfb_nouns_list=txt_to_nouns("worldfootball.txt") #spotvnews.com에서 30페이지까지 해외 축구 뉴스 본문을 크롤링한 텍스트
nba_nouns_list=txt_to_nouns("nba.txt") #위와같이 30페이지까지 NBA 뉴스 본문을 크롤링한 텍스트

documents=[poli_nouns_list,wfb_nouns_list,nba_nouns_list]
#위에서 처리한 3개의 명사 리스트를 하나의 딕셔너리
K=3
D=len(documents)
random.seed(0)

document_topic_counts = [Counter() for _ in documents]
topic_word_counts = [Counter() for _ in range(K)] 
topic_counts = [0 for _ in range(K)] 
document_lengths = [len(d) for d in documents]
def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k) for k in range(K)])
# 각 단어를 임의의 토픽에 배정
distinct_words = set(word for document in documents for word in document) 
W = len(distinct_words)
document_topics = [[random.randrange(K) for word in document]
                   for document in documents]
def sample_from(weights):
    total = sum(weights)
    rnd = total * random.random()       # uniform between 0 and total
    for i, w in enumerate(weights):
        rnd -= w                        # return the smallest i such that
        if rnd <= 0: return i           # sum(weights[:(i+1)]) >= rnd
        
def topic_weight(d, word, k):
    # 문서와 문서의 단어가 주어지면
    # k번째 토픽의 weight를 반환
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)
# 랜덤 초기화한 상태에서 AB를 구하는 데 필요한 숫자 계산하기
def p_topic_given_document(topic, d, alpha=0.1):
    # 문서 d의 모든 단어 가운데 topic에 속하는
    # 단어의 비율 (alpha를 더해 smoothing)
    return ((document_topic_counts[d][topic] + alpha) /
            (document_lengths[d] + K * alpha))

def p_word_given_topic(word, topic, beta=0.1):
    # topic에 속한 단어 가운데 word의 비율
    # (beta를 더해 smoothing)
    return ((topic_word_counts[topic][word] + beta) /
            (topic_counts[topic] + W * beta))

for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1
        
# 조건부 확률 분포를 이용하여 (토픽-단어), (문서-토픽)에 대한 깁스 샘플링 실행하기
for iter in range(1000): 
    for d in range(D): 
        for i, (word, topic) in enumerate(zip(documents[d], 
                                              document_topics[d])): 
 
 
           # remove this word / topic from the counts
           # so that it doesn't influence the weights 
            document_topic_counts[d][topic] -= 1 
            topic_word_counts[topic][word] -= 1 
            topic_counts[topic] -= 1 
            document_lengths[d] -= 1 
 
           # choose a new topic based on the weights 
            new_topic = choose_new_topic(d, word) 
            document_topics[d][i] = new_topic 

 
           # and now add it back to the counts 
            document_topic_counts[d][new_topic] += 1 
            topic_word_counts[new_topic][word] += 1 
            topic_counts[new_topic] += 1 
            document_lengths[d] += 1

topic_names = ["스포츠","정치1","정치2"]

for document, topic_counts in zip(documents, document_topic_counts): 
         for topic, count in topic_counts.most_common(): 
            if count > 0: 
                print (topic_names[topic], count)    

#해석: 인풋대로 "해외축구", "NBA", "정치뉴스" 3가지의 토픽대로 그룹핑은 되지 않았고, 스포츠끼리 많이 뭉치고, 정치관련 단어들이 구분돼서 2그룹에 들어감
#     그 이유는 스포츠 관련되어 쓰이는 단어가 비슷하여 농구와 축구간 구별이 되지 않은 것으로 판단됨.
           
# 2. Word2Vec 코드를 활용하여 본인이 원하는 텍스트 넣어 보기 => 텍스트 + 원하는 키워드 5개의 유사 단어 추출한 후 결과 첨부   

import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec# 파일로 출력하기  
txt_file = 'wfb.txt'
with open(txt_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))

with open(r'C:\Users\EdwinPark\worldfootball.txt', "r") as wfb:
    text=wfb.read()

# 텍스트를 한 줄씩 처리하기 
twitter = Okt()
results = []
lines = text.split("\r\n")
for line in lines:
    # 형태소 분석하기 
    # 단어의 기본형 사용
    malist = twitter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 어미/조사/구두점 등은 대상에서 제외 
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)
    
# 파일로 출력하기  
txt_file = 'wfb.txt'
with open(txt_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
    
# Word2Vec 모델 만들기 
data = word2vec.LineSentence(txt_file)
model = word2vec.Word2Vec(data, 
    size=200, window=10, hs=1, min_count=2, sg=1)
model.save("wfb.model")

#이강인이라는 단어가 사용되었을때 가장 많이 근처에서 사용된 단어!
model = word2vec.Word2Vec.load("wfb.model")
model.most_similar("이강인")

#'토트넘'이라는 단어와 '손흥민'의 단어 사용 패턴의 유사의 정도
model.similarity('토트넘','손흥민')



    
