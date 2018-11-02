# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

urls = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181030&page=1", "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181030&page=2", "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181030&page=3", "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181030&page=4", "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181030&page=5"]
for k in urls:
    html = urlopen(k)
    soup = BeautifulSoup(html,"lxml",from_encoding='utf-8')
    articles = soup.findAll("dt")
    url_list = []
    for link in articles:
        url_list.append(link.find("a")["href"])
    for i in url_list:
        html = urlopen(i)
        soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')
        content = soup.find("div",{"id":"articleBodyContents"})
        title = soup.find("h3",{"id":"articleTitle"}).find(text=True)
        hangul = re.compile('[^ ㄱ-ㅣ가-힣.'']+')
        test = str(content.find)
        result = hangul.sub('',test)
        result = re.sub('본문 내용  플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
        result = re.sub('본문 내용  플레이어   동영상 뉴스       영상 플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
        print(title)
        print(result)



# Machine Learning Quest
# 앤드류 강의 week1과 week2에서 필요한 강의 듣고 중요 내용 요약해서 올리기
# https://www.coursera.org/learn/machine-learning

유진님께 갠톡으로 보냈습니다~!


