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
==> Dursleys와 가장 비슷한 단어로 꼽힌 것들이다.

print(model.similarity('Dursleys', 'Dudley'))
print(model.similarity('Harry', 'Dudley'))
0.99936867
0.99947006
==> Dursleys&Dudley의 유사성과 Harry&Dudley의 유사성이 거의 비슷하게 나왔다. 아무래도 소설 텍스트의 특성 상 비슷한 단어를 찾기 어려웠나보다ㅠㅠㅠ  
