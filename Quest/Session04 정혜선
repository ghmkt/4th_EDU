# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from bs4 import BeautifulSoup as bs              # 데이터파싱 라이브러리
import urllib.request as req                     # 데이터수신 라이브러리
from urllib.request import urlopen
import pandas as pd                              # 데이터정리 라이브러리 
import datetime                                  # 날짜데이터 라이브러리
import re   

articles = []
for i in range(1,6):
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&mid=shm&date=20181023&page=" + str(i)
    html = urlopen(url)
    soup = bs(html,"lxml",from_encoding='utf-8')
    articles.extend(soup.findAll("dt"))
     
url_list = []
for link in articles:
    url_list.append(link.find("a")["href"])
    
url_list2 = list(set(url_list)) ##중복 제거
print(url_list2)

news_list = pd.DataFrame(columns = ['Title',
                                    'Article'])    
for i in range(len(url_list2)):
    html = urlopen(url_list2[i])
    soup = bs(html,"html.parser",from_encoding='utf-8')

    title = soup.find("h3",{"id":"articleTitle"}).find(text=True)
    content = soup.find("div",{"id":"articleBodyContents"})

    import re
    hangul = re.compile('[^ ㄱ-ㅣ가-힣.'']+') # # 한글과 띄어쓰기 . ''""를 제외한 모든 글자
    test = str(content.find)

    result = hangul.sub('',test) # 한글과 띄어쓰기를 제외한 모든 글자 제외
    result = re.sub('본문 내용  플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
    result = re.sub('본문 내용  플레이어   동영상 뉴스       영상 플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
    
    news_list = news_list.append(
            {'Title':title,
             'Article':result}, ignore_index = True)

news_list.to_csv("D:/Growth Hackers/NaverNewsList.csv", index=False, encoding = 'euc-kr')

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

import pandas as pd
df = pd.read_csv("D:/Growth Hackers/caschool.csv", engine = 'python', index_col = 0)
print(df.head())

x1 = df["str"]
x2 = df["avginc"]
y = df["read_scr"]
print(len(x1), len(x2), len(y))

import scipy
from scipy import optimize as op

def f1(a):
    for i in range(1,421):
        cost_function = 0
        cost_function += (a[0]*x1[i] + a[1]*x2[i] + a[2] -y[i])**2
    return cost_function
result = op.minimize(f1,(1,1,1))
print(result)
