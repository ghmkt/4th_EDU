# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.
from bs4 import BeautifulSoup as bs              # 데이터파싱 라이브러리
import urllib.request as req                     # 데이터수신 라이브러리

titles=[]
for i in range(1,6):
    # 5개 페이지의 링크 받아오기.
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181002&page="+str(i)
    # url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=269&sid1=100&date=20181002&page=1"
    header_ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

    request = req.Request(url, headers = {'User-Agent':header_})
    html = req.urlopen(request)
    page = bs(html.read(), 'lxml')
    # print(html.getcode()) # 200이 뜨면 잘 불러온 것!

    
    # 기사 제목이 있는 class가 두 개 있음.
    headlines =page.find_all("ul", {'class':'type06_headline'})
    headlines2=page.find_all("ul", {'class':'type06'})

    for headline in headlines:
        dt_h = headline.find_all("dt")
        for dt in dt_h:
            a_h = dt.find('a').get_text().strip()
            titles.append(a_h)

    for headline in headlines2:
        dt_h = headline.find_all("dt")
        for dt in dt_h:
            a_h = dt.find('a').get_text().strip()
            titles.append(a_h)

# '', '동영상기사' 등을 제외시켜야 함!
print(set(titles))


# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

# Machine Learning Quest 2
# 앤드류 강의 week1과 week2에서 필요한 강의 듣고 중요 내용 요약해서 올리기
# https://www.coursera.org/learn/machine-learning
