# 제출시 파일명은 Session06 이름 으로 해주세요.

# 1. LDA 코드를 활용하여 본인이 원하는 텍스트를 넣어 보기 => 텍스트 원본 파일 + LDA 결과 첨부 + 본인 결과 해석

# 파일은 올리는 법을 몰라, 주영님께 카톡으로 개인적으로 드렸습니다!!
# file1, file2, file3과 같이 뒤의 숫자만 바뀔 때, 이를 반복문에 포함하는 방법을 잘 모르겠습니다.
# 인덱싱을 해주는 방향이 아니라 반복문 처리를 고민하다 결국 해결책을 못찾았습니다.
import codecs
import os
from konlpy.tag import Kkma;kkma = Kkma()
from collections import Counter
import random

os.chdir("C:\\Users\\승우\\Desktop")

file1=codecs.open('우리 그만하자.txt','r')
file2=codecs.open('사랑을 했다.txt','r')
file3=codecs.open('매일듣는노래.txt','r')
file4=codecs.open('첫째날.txt','r')

f1=''
lines=file1.readlines()
for line in lines:
    f1 += line.rstrip() + ' '

f2=''
lines=file2.readlines()
for line in lines:
    f2 += line.rstrip() + ' '

f3=''
lines=file3.readlines()
for line in lines:
    f3 += line.rstrip() + ' '

f4=''
lines=file4.readlines()
for line in lines:
    f4 += line.rstrip() + ' '

token1 = kkma.morphs(f1)
token2 = kkma.morphs(f2)
token3 = kkma.morphs(f3)
token4 = kkma.morphs(f4)

documents = []
documents.append(token1);documents.append(token2);documents.append(token3);documents.append(token4)

#토픽의 개수
K = 3

document_topic_counts = [Counter() for _ in documents]
topic_word_counts = [Counter() for _ in range(K)] 
topic_counts = [0 for _ in range(K)] 
document_lengths = [len(d) for d in documents]
distinct_words = set(word for document in documents for word in document) 
W = len(distinct_words)
D = len(documents)


#A
def p_topic_given_document(topic, d, alpha=0.1):
    return ((document_topic_counts[d][topic] + alpha) /
            (document_lengths[d] + K * alpha))

#B
def p_word_given_topic(word, topic, beta=0.1):
    return ((topic_word_counts[topic][word] + beta) /
            (topic_counts[topic] + W * beta))

#A*B
def topic_weight(d, word, k):
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)

def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k) for k in range(K)])

def sample_from(weights):
     total = sum(weights)
     rnd = total * random.random()     
     for i, w in enumerate(weights):
         rnd -= w                    
         if rnd <= 0: return i  
            
            
random.seed(0)

document_topics = [[random.randrange(K) for word in document]
                   for document in documents]

for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1

for iter in range(500): 
    for d in range(D): 
        for i, (word, topic) in enumerate(zip(documents[d], 
                                              document_topics[d])): 
 
            document_topic_counts[d][topic] -= 1 
            topic_word_counts[topic][word] -= 1 
            topic_counts[topic] -= 1 
            document_lengths[d] -= 1 
            
            new_topic = choose_new_topic(d, word) 
            document_topics[d][i] = new_topic 

            document_topic_counts[d][new_topic] += 1 
            topic_word_counts[new_topic][word] += 1 
            topic_counts[new_topic] += 1 
            document_lengths[d] += 1
        
for k, word_counts in enumerate(topic_word_counts): 
         for word, count in word_counts.most_common(): 
             if count > 0: print (k, word, count) 
          
topic_names = ['WTH1','WTH2','WTH3']

for document, topic_counts in zip(documents, document_topic_counts): 
         print (document) 
         for topic, count in topic_counts.most_common(): 
             if count > 0: 
                 print (topic_names[topic], count)
              
              
#느낀점 1: 한글은 자연어 처리가 굉장히 어렵다. 의미 단위가 이상하게, 깔끔하지 못하게 끊어지는 경우가 많다...
#느낀점 2: documents들도 어느 정도는 연관성이 있는 document를 써야 한다. 다 사랑 노래라서 썼는데 자기 할말만 하는, 스토리가 없는 노래라 연관성이 하나도 없다.
#느낀점 3: document 하나 하나 당 내포하고 있는 정보가 일정 수준 이상은 돼야 한다. 4분 짜리 노래들로는 어떤 유의미한 단어도 추출 불가...
#어떻게든 topic을 지어줘보려 해도 전혀 연관성이 없는 것들이라 What the Hell 1, 2, 3으로 했습니다...


# 2. Word2Vec 코드를 활용하여 본인이 원하는 텍스트 넣어 보기 => 텍스트 + 원하는 키워드 5개의 유사 단어 추출한 후 결과 첨부   
import codecs
from konlpy.tag import Okt
from gensim.models import word2vec

file=codecs.open("C:\\Users\\승우\\Desktop\\첫째날.txt",'r')
data2 = file.read()
file.close()

# 텍스트를 한 줄씩 처리하기 
twitter = Okt()
results = []
lines = data2.split("\n")
#print(lines)

for line in lines:
    malist = twitter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 어미/조사/구두점 등은 대상에서 제외 
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)

cha = ''

for i in range(0,len(results)):
    cha += results[i] + ' '

quest_2 = 'quest_2.txt'
with open(quest_2, 'w', encoding='utf-8') as q2:
    q2.write(cha)
    q2.close()
    
data = word2vec.LineSentence(quest_2)
model = word2vec.Word2Vec(data, 
    size=200, window=10, hs=1, min_count=2, sg=1)
model.save("quest.2")    
    
model = word2vec.Word2Vec.load("quest.2")
model.most_similar("너")

#이런.. 첫째날은 word2vec에 적합하지 않은 노래인 것 같습니다... 역시, 후렴구가 계속 반복되고, 짧기 때문에 유의미한 정보를 몇 개 찾을 수 없습니다.

model.similarity('너','하루')
#세상에... 12595771 연관성이 거의 없다고 봐도 무방할 것 같습니다.

#자료를 잘못 선택했음에 틀림없습니다..
