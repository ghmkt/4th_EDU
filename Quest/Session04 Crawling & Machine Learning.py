# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url_list = []
for i in range(1,6):
    url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid2=269&sid1=100&date=20181101&page="+str(i)
    html = urlopen(url)
    soup = BeautifulSoup(html,"lxml",from_encoding='utf-8')
    articles = soup.findAll("dt")
for link in articles:
    url_list.append(link.find("a")["href"])
    
url_list = list(set(url_list))
url_list

content,title=[],[]
for i in range(len(url_list)):
    html = urlopen(url_list[i])
    soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')
    content.append(soup.find("div",{"id":"articleBodyContents"}))
    title.append(soup.find("h3",{"id":"articleTitle"}).find(text=True))
    
test,text=[],[]
for i in range(len(content)):
    test.append(str(content[i].find))
    result = hangul.sub('',test[i]) 
    result = re.sub('본문 내용  플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
    result = re.sub('  .        .      영상 플레이어  앵커','',result )
    result = re.sub('  .    본문 내용  플레이어   동영상 뉴스 .      영상 플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
    text.append(result)
    
data = [title, text]

# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

import pandas as pd
import numpy as np
from scipy import optimize as op

df = pd.read_csv('c:\\project\\caschool.csv')

x1 = df['str']
x2 = df['avginc']
y = df['read_scr']

def f(b):
    fn = 0
    for i in range(len(y)):
        fn += (b[0]+b[1]*x1[i]+b[2]*x2[i]-y[i])**2
    fn = fn/(2*len(y))
    return fn
  
result = op.minimize(f,(10,10,10))
print(result)

# Machine Learning Quest 2
# 앤드류 강의 week1과 week2에서 필요한 강의 듣고 중요 내용 요약해서 올리기
# https://www.coursera.org/learn/machine-learning
