# 제출시 파일명은 Session06 이름 으로 해주세요.

# 0. Konlpy 문제 (안 풀어도 되는데 까먹고 풀었네요...ㅎㅎ)
import konlpy
import nltk

from konlpy.corpus import kolaw
files_ko = kolaw.fileids()
doc_ko = kolaw.open('constitution.txt').read()

from konlpy.tag import Kkma;kkma = Kkma()
nouns = kkma.nouns(doc_ko)

kor = nltk.Text(nouns, name = '대한민국 헌법 조항')
kor.vocab()

결과 ==> FreqDist({'조': 3, '이': 3, '우리': 2, '일': 2, '장': 2, '수': 2, '자': 2, '외': 2, '인': 2, '관': 2, ...})



# 1. LDA 코드를 활용하여 본인이 원하는 텍스트를 넣어 보기 => 텍스트 원본 파일 + LDA 결과 첨부 + 본인 결과 해석
import nltk
import konlpy
from konlpy.tag import Kkma;kkma = Kkma()
from konlpy.corpus import kobill

from os import listdir
file_list = listdir('LDA_txt')
documents = []
for a in file_list:
    file = "C:\\Users\\renoi\\Dropbox\\★★★Growth Hackers\\★Quest\\LDA_txt\\" + a
    f = open(file)
    text = f.read()
    documents.append(kkma.morphs(text))

import random
from collections import Counter

#조건부 확률 분포 정의를 위한 준비

#topic의 개수 (documents에 IT와 관련된 기사 3개와 정치와 관련된 기사 3개가 있으므로 토픽을 2개로 설정하였습니다)
K = 2

#1. 각 토픽이 각 문서에 할당되는 횟수
document_topic_counts = [Counter() for _ in documents]

#2. 각 단어가 각 토픽에 할당되는 횟수
topic_word_counts = [Counter() for _ in range(K)] 

#3. 각 토픽에 할당되는 총 단어 수
topic_counts = [0 for _ in range(K)] 

#4. 각 문서에 포함되는 총 단어의 수
document_lengths = [len(d) for d in documents]

#5. 단어 종류의 수
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
     rnd = total * random.random()      
     for i, w in enumerate(weights):
         rnd -= w                     
         if rnd <= 0: return i      
       
random.seed(0)

#topic의 개수
K = 2

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
       
#각 토픽에 가장 영향력이 높은 (weight)값이 큰 단어 탐색
for k, word_counts in enumerate(topic_word_counts): 
         for word, count in word_counts.most_common(): 
             if count > 0: print (k, word, count) 
       
topic_names = ["정치", "기술"]

for document, topic_counts in zip(documents, document_topic_counts): 
         print (document) 
         for topic, count in topic_counts.most_common(): 
             if count > 0: 
                 print (topic_names[topic], count)
 
### Politics 기사1 : 정치 464 / 기술 109
### Politics 기사2 : 정치 503 / 기술 28
### Politics 기사3 : 정치 797 / 기술 116
### IT Technology 기사1 : 정치 782 / 기술 3
### IT Technology 기사2 : 정치 370 / 기술 80
### IT Technology 기사3 : 정치 902 / 기술 64
######## 결과 해석: 제대로 구분을 못 해내고 있습니다. 아마도 저의 기사 선정에 문제가 있었던 것 같습니다. 같은 주제(정치 or 기술) 안에 있는 3개의 기사들이 같은 카테고리에 속해있긴 하지만 모두 상이한 주제를 다루고 있어서 이런 결과가 나온 것 같습니다.


       
       
# 2. Word2Vec 코드를 활용하여 본인이 원하는 텍스트 넣어 보기 => 텍스트 + 원하는 키워드 5개의 유사 단어 추출한 후 결과 첨부   
import nltk
f = open('Harry_Potter.txt', 'r')
Harry = f.read()
print(Harry)

from nltk.tokenize import word_tokenize
word_tokenize_list = word_tokenize(Harry)

from gensim.models.word2vec import Word2Vec
model = Word2Vec([word_tokenize_list],size=100, window=3, min_count=2, sg=1)
model.init_sims(replace=True)

---결과----

model.most_similar("Harry")
[('had', 0.9995894432067871),
 ('the', 0.9995880722999573),
 ('at', 0.9995788931846619),
 ('was', 0.9995592832565308),
 ('that', 0.9995542168617249),
 ('out', 0.9995530843734741),
 ('they', 0.9995449185371399),
 ('he', 0.9995372891426086),
 ('looked', 0.9995354413986206),
 ('much', 0.999535083770752)]
==> "Harry"와 가장 비슷한 단어로 꼽힌 것들이다. 아무래도 소설작품 텍스트다 보니 맥락을 파악하기가 쉽지 않았나보다. 그나마 'he'가 비슷한 단어로 꼽힌 것이 유일하게 의미 있는 것처럼 보인다.

model.most_similar("Dursleys")
[('cat', 0.9996163845062256),
 ('.', 0.9995356798171997),
 ('glass', 0.9995316863059998),
 ('down', 0.9995315074920654),
 ('of', 0.9995250701904297),
 ('around', 0.999519407749176),
 ('in', 0.9995157122612),
 ('the', 0.9995035529136658),
 ('into', 0.9995008707046509),
 ('street', 0.9994946718215942)]

model.most_similar("Dudley")
[('his', 0.9996232986450195),
 ('head', 0.9996210932731628),
 ('him', 0.9995797872543335),
 ('they', 0.9995718002319336),
 ('here', 0.9995669722557068),
 ('at', 0.9995605945587158),
 ('like', 0.9995596408843994),
 ('with', 0.9995473623275757),
 ('And', 0.9995435476303101),
 ('you', 0.9995414018630981)]

model.most_similar("Petunia")
[('so', 0.9992977380752563),
 ('ever', 0.9992491006851196),
 ('with', 0.9992244243621826),
 ('Dudley', 0.9992172718048096),
 ('her', 0.9992169141769409),
 ('when', 0.9992086291313171),
 ('he', 0.9992083311080933),
 ('dark', 0.99920654296875),
 ('his', 0.9992050528526306),
 ('and', 0.9991910457611084)]

model.most_similar("Vernon")
[('you', 0.9994608163833618),
 ('about', 0.9994537830352783),
 ('Hagrid', 0.9994459748268127),
 ('man', 0.9994446039199829),
 ('then', 0.9994331002235413),
 ('out', 0.9994134902954102),
 ('all', 0.9994131326675415),
 ('their', 0.9994028806686401),
 ('large', 0.9993922710418701),
 ('wanted', 0.9993910789489746)]
