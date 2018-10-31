# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

for i in range(1,6):
    
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2=269&sid1=100&mid=shm&date=20181004&page="+str(i) 
    #네이버 정치 기사 i 페이지로 1부터 5까지 반복.

    html = urlopen(url)
    soup = BeautifulSoup(html,"lxml",from_encoding='utf-8')

    articles = soup.findAll("dt")

    ex_dl = articles[1].find("a")["href"] ## 정치 기사 메인 페이지에서 기사들로 가는 url 
    url_list = []

    for link in articles:
            url_list.append(link.find("a")["href"])
            url_list2 = list(set(url_list))

    for j in list(range(0,len(url_list2))):


        html = urlopen(url_list2[j])
        soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')

        content = soup.find("div",{"id":"articleBodyContents"})
        title = soup.find("h3",{"id":"articleTitle"}).find(text=True)

        hangul = re.compile('[^ ㄱ-ㅣ가-힣.''0-9]+') # # 한글과 띄어쓰기 . ''""를 제외한 모든 글자

        test = str(content.find)

        result = hangul.sub('',test) # 한글과 띄어쓰기를 제외한 모든 글자 제외
        result = re.sub('본문 내용  플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
        result = re.sub('본문 내용  플레이어   동영상 뉴스       영상 플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
        print(title)
        print();
        print(result)
        print()

# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

import pandas as pd
df = pd.read_csv(r'C:\Users\EdwinPark\caschool.csv', engine = 'python', index_col = 0)

def f1(beta):
    cost_function = 0
    for i in range(1,len(df)+1):
        cost_function += (beta[0]*df.str[i]+beta[1]*df.avginc[i]+beta[2]-df.read_scr[i]) ** 2
    return cost_function / (2*len(df))

from scipy import optimize as op
result=op.minimize(f1,(20,15,600))
print(result)

#'read_scr' = -0.95*('str') + 1.88*('avginc') + 644.77 의 관계성을 갖고 있음!
