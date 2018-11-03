# 제출시 파일명은 Session06 이름 으로 해주세요.
# 1. LDA 코드를 활용하여 본인이 원하는 텍스트를 넣어 보기 => 텍스트 원본 파일 + LDA 결과 첨부 + 본인 결과 해석
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import nltk
import random
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re

documents= []
twitter = Okt()
for page in range(254,259):
    url = "https://www.datascienceweekly.org/newsletters/data-science-weekly-newsletter-issue-%s" % page
    html = urlopen(url) 
    soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')
    content = soup.find("td",{"class":"bodyContent"}).get_text().strip().replace("//",'').replace("()",'').replace("{}",'')
    lines = content.split("\r\n")
    article = []
    for line in lines:
    # 형태소 분석하기 
    # 단어의 기본형 사용
        malist = twitter.pos(line, norm=True, stem=True)
        for word in malist:
        # 어미/조사/구두점 등은 대상에서 제외 
            if word[1] == "Alpha":
                article.append(word[0])
    documents.append(article)
print(documents)
#조건부 확률 분포 정의를 위한 준비

#topic의 개수
K = 4

#1. 각 토픽이 각 문서에 할당되는 횟수
#counter로 구성된 list
#각각의 counter는 각 문서를 의미함
document_topic_counts = [Counter() for _ in documents]
#2. 각 단어가 각 토픽에 할당되는 횟수
# 각각의 counter는 각 토픽을 의미함
topic_word_counts = [Counter() for _ in range(K)] 
#3. 각 토픽에 할당되는 총 단어 수
# 각각의 숫자는 각 토픽을 의미함
topic_counts = [0 for _ in range(K)] 
#4. 각 문서에 포함되는 총 단어의 수
# 각각의 숫자는 각 문서를 의미함
document_lengths = [len(d) for d in documents]

#5. 단어 종류의 수(개별 문서에있는 유니크한 단어의 수)
distinct_words = set(word for document in documents for word in document) 
W = len(distinct_words)

#6. 총 문서의 수
D = len(documents)

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

def topic_weight(d, word, k):
    # 문서와 문서의 단어가 주어지면
    # k번째 토픽의 weight를 반환
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)
def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k) for k in range(K)])

#랜덤으로 생성된 weight로부터 인덱스를 생성함
def sample_from(weights):
     total = sum(weights)
     rnd = total * random.random()       # uniform between 0 and total
     for i, w in enumerate(weights):
         rnd -= w                        # return the smallest i such that
         if rnd <= 0: return i           # sum(weights[:(i+1)]) >= rnd

random.seed(0)

# 각 단어를 임의의 토픽에 배정
document_topics = [[random.randrange(K) for word in document]
                   for document in documents]

# 랜덤 초기화한 상태에서 AB를 구하는 데 필요한 숫자 계산하기
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

for k, word_counts in enumerate(topic_word_counts): 
         for word, count in word_counts.most_common(): 
             if count > 0: print (k, word, count)

          topic_names = ["PyTorch","Science","networks","machine learning"]

for document, topic_counts in zip(documents, document_topic_counts): 
         print (document) 
         for topic, count in topic_counts.most_common(): 
             if count > 0: 
                 print (topic_names[topic], count)
                    
#input으로 넣은 data science weekly newsletters가 주별 topic이 없어서 그런지 토픽 네임을 정하는 것 자체가 힘드네요
#차라리 개별 news 별로 하나의 문서로 만드는게 나았을 것 같습니다.

# 2. Word2Vec 코드를 활용하여 본인이 원하는 텍스트 넣어 보기 => 텍스트 + 원하는 키워드 5개의 유사 단어 추출한 후 결과 첨부   

import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec

fp = codecs.open("C:\\dev\\disruptive-technologies-catching-the-wave.txt", "r", encoding="utf-8")
text = fp.read()
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
    
txt_file = 'disruptive.txt'
with open(txt_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
# Word2Vec 모델 만들기 
data = word2vec.LineSentence(txt_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save("disruptive.model")
model = word2vec.Word2Vec.load("disruptive.model")
print(model.most_similar("technology"))
print(model.most_similar("disruptive"))
# strategic, manager, must, once, tend, can, sustaining 등의 단어는
# 경영자들에게 파괴적 기술(disruptive technology)의 중요성을 알리는 논문의 핵심을 잘 드러내주네요!
print(model.similarity('technology','innovation'))
