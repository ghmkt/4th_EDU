# 제출시 파일명은 Session06 이름 으로 해주세요.

# 1. LDA 코드를 활용하여 본인이 원하는 텍스트를 넣어 보기 => 텍스트 원본 파일 + LDA 결과 첨부 + 본인 결과 해석
import nltk
import random
from collections import Counter
file = open('C:/users/lg01/desktop/Moon_speech.txt')
text = file.read()
documents = []
documents.append(nltk.word_tokenize(text))
print(documents)

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
       

# 2. Word2Vec 코드를 활용하여 본인이 원하는 텍스트 넣어 보기 => 텍스트 + 원하는 키워드 5개의 유사 단어 추출한 후 결과 첨부   
from gensim.models.word2vec import Word2Vec
model = Word2Vec([word_tokenize_list],size=100, window=3, min_count=2, sg=1)
model.init_sims(replace=True)
