# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from bs4 import BeautifulSoup as bs
import urllib.request as req
from urllib.request import urlopen
import pandas as pd
import re

url_lst=[]
com=pd.DataFrame(columns=('기사제목','기사내용'))
for i in range(1,6):
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181023&page="+str(i)
    header_ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

    request = req.Request(url, headers = {'User-Agent':header_})
    html = req.urlopen(request)
    page = bs(html.read(), 'lxml',from_encoding='utf-8')




    pp=page.findAll('dt')
    
    for i in pp:
      url_lst.append(i.find('a')['href'])
    url_lst=list(set(url_lst))


    for i in range(len(url_lst)):
        html=urlopen(url_lst[i])
        soup=bs(html,'html.parser',from_encoding='utf-8')
        content=soup.find('div',{"id":"articleBodyContents"})
        title=soup.find('h3',{'id':'articleTitle'})
        content=str(content)
        title=str(title)
        d=re.compile('[^ ㄱ-ㅣ가-힣.'']+')
        content=d.sub('',content)
        title=d.sub('',title)
        content = re.sub("본문 내용 플레이어 플레이어 오류를 우회하기 위한 함수 추가 ","",content) 
        content = re.sub("본문 내용  플레이어   동영상 뉴스       영상 플레이어   플레이어    오류를 우회하기 위한 함수 추가",'',content)
        content = re.sub("본문 내용 플레이어 동영상 뉴스 . 영상 플레이어 플레이어 오류를 우회하기 위한 함수 추가",'',content)
        
        com.loc[i]=[title,content]
        
com

# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
A=pd.read_csv('C:\\GH\\caschool.csv')
x1=A[['str','avginc']]
x0=np.ones((420,1))
x0=pd.DataFrame(x0)
x=np.hstack([x0,x1])
y=A[['read_scr']]
def fitmodel_g(x,y):
    N=len(x)
    w=np.ones((x.shape[1],1))
    alpha=0.002
    maxI=500000
    for i in range(maxI):
        error=np.dot(x,w)-y
        gradient=np.dot(x.transpose(),error)/N
        w=w-alpha*gradient
    return w
fitmodel_g(x,y)
x
#비교해보기
import statsmodels.api as sm
model=sm.OLS(y,x).fit()
model.summary()
