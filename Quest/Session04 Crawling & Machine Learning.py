# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#------------------------------기사 제목 얻기-------------------------------#
title_list = []
url_list   = []

for i in range(1,6):
    # 5개 페이지의 링크 받아오기.
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&page="+str(i)
    html = urlopen(url)
    soup = BeautifulSoup(html,"lxml",from_encoding='utf-8')
    
    # 기사 제목이 있는 부분은 dt
    articles = soup.findAll("dt")
    
    # title,url을 하나씩 추가한다.
    for link in articles:
        # 제목은 dt 내 텍스트를 얻어오면 된다.
        title_list.append(link.get_text().strip())
        
        # 링크는 a href= 로 시작
        url_list.append(link.find("a")["href"])


# title, url list 중복 제거
title_list=list(set(title_list))
title_list.remove('동영상기사')
url_list2 = list(set(url_list))

# title_list : 100개의 기사 제목,
# url_list   : 100개의 기사 링크 >> 기사 내용 긁어오기 위한 전처리

#------------------------------기사 본문 얻기-------------------------------#
# 100개의 기사 내용을 구하고 싶으면 for문을 돌리면 됨!
# for i in range(length(url_list)):

html = urlopen(url_list[0])
soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')

title = soup.find("h3",{"id":"articleTitle"}).find(text=True)
content = soup.find("div",{"id":"articleBodyContents"})
text_content = content.get_text().strip()

# 기사 시작!
s = text_content.find('{}\n\n')
text_content=text_content[s+4:]

print(title)
print(text_content)




# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.
import pandas as pd
from scipy import optimize as op
from matplotlib import pyplot as plt

# 파일 읽고, 필요한 부분만 df에 저장
df = pd.read_csv('caschool.csv', engine = 'python', index_col = 0)
df = df[['read_scr', 'str', 'avginc']]

def f1(beta):
    # y = a*x1 + b*x2 + c에서 x1,x2,y는 아니까 a,b,c를 구하는 것임!
    # a = beta[0], b= beta[1], c=beta[2]
    
    cost_function = 0
    for i in range(1,len(df)+1):
        # 비용함수 공식
        cost_function += (beta[0]*df.str[i]+beta[1]*df.avginc[i]+beta[2]-df.read_scr[i]) ** 2
    return cost_function / (2*len(df))

result=op.minimize(f1,(10,20,300))
result.x

