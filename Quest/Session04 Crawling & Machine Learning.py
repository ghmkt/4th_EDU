# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경
# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re

url_list = []
for page in range(1,6):
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&date=20181103&page=%d" % page #네이버 정치 기사 페이지
    html = urlopen(url)
    soup = BeautifulSoup(html,"lxml",from_encoding='utf-8')
    articles = soup.findAll("dt")
    ex_dl = articles[1].find("a")["href"] ## 정치 기사 메인 페이지에서 기사들로 가는 url 
    for link in articles:
        url_list.append(link.find("a")["href"])
    url_list2 = list(set(url_list)) ##중복 제거

    
title_list = []
for article in range(len(url_list2)):
    html = urlopen(url_list2[article])
    soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')
    content = soup.find("div",{"id":"articleBodyContents"}).get_text().strip().replace("flash 오류를 우회하기 위한 함수 추가",'').replace("function _flash_removeCallback",'').replace("//",'').replace("()",'').replace("{}",'')
    title = soup.find("h3",{"id":"articleTitle"}).find(text=True)
    if title not in title_list:
        title_list.append(title)
        number_article = article + 1
        print("\n\n%s번째 기사 / 링크 바로가기 --> %s" % (number_article, url_list2[article]))
        print("제목 : " + title)
        print("본문 : " + content)
    

# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모델의 Cost function을 minimize해보세요.
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as op

caschool = pd.read_csv("C:\\dev\\4th-EDU\\Quest\\caschool.csv")

# a * cashcool.str + b * cashcool.avginc + c = cashool.read_csr 이라고 가정.
# c 를 최대한 줄여야함.
# x = [a,b,c]
def f(x):
    sqrs = 0
    for i in range(len(caschool)):
        sqrs += (x[0]*caschool.str[i] + x[1]*caschool.avginc[i] + x[2] - caschool.read_scr[i])**2
    return sqrs/(2*len(caschool)) #미분쉽게하려고..
result=op.minimize(f,(10,10,100))
print(result)
