# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

#HW for Session 04: Crawling

from bs4 import BeautifulSoup as bs             
import urllib.request as req                   
import pandas as pd                             
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
import csv

politics = pd.DataFrame(columns = ['제목', '내용'])

path = 'C:\\Users\\승우\\chromedriver_win32\\chromedriver.exe' 
driver = webdriver.Chrome(path)
driver.get("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269")

url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269"
header_ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

request = req.Request(url, headers = {'User-Agent':header_})
html = req.urlopen(request)
page = bs(html.read(), 'lxml')
articles = page.findAll("dt")

url_list = []
for link in articles:
    url_list.append(link.find("a")["href"])
    
url_list2 = list(set(url_list)) 
url_list2

html = urlopen(url_list2[0])
soup = bs(html,"html.parser",from_encoding='utf-8')

title = soup.find('h3', {'id':'articleTitle'}).find(text=True)
content = soup.find('span',{'class':'end_photo_org'}).find(text=True)

title_sum=[]

for i in range(0,20):
    
    html=urlopen(url_list2[i])
    soup = bs(html,"html.parser",from_encoding='utf-8')
    
    title = soup.find('h3', {'id':'articleTitle'}).find(text=True)
    #content = soup.find('span',{'class':'end_photo_org'}).find(text=True)
    title_sum.append(title)
    #if content == None:
        #content = soup.find('div',{'id':'articleBodyContents'}).find(text=True)
    
    #print(title)
    #print(content)

print(title_sum)
    
#soup.find('div', {'class':paging})
#driver.find_element_by_class_name("paging").click() : 클릭 실패

#일단, 첫 페이지의 스무개의 제목을 따오는 데에는 성공을 했으나 온갖 시도 후에도 1.내용 따오기, 그리고 2.페이지 넘어가기에는 실패했습니다.
#크롤링은 아직 많이 생소한 개념이라, 근본적으로 제가 다른 책을 사서라도 차후에 공부를 다시 해야될 것 같습니다.
#Session 04 크롤링 Quest를 능력부족으로 불완전하게 마무리 짓는 대신, Session 05에서 두 가지 방법을 통해 해결해보았습니다.
#차후에 독학을 거친 후, 해결할 능력이 생기면 그 때 다시 파일을 업로드 하겠습니다. 죄송합니다.


# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

# Machine Learning Quest 2
# 앤드류 강의 week1과 week2에서 필요한 강의 듣고 중요 내용 요약해서 올리기
# https://www.coursera.org/learn/machine-learning
#HW for Session 05: Machine Learning
#Way1
import csv
import pandas as pd
from scipy import optimize as op
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('C:\\Users\\승우\\Desktop\\caschool.csv', engine='python')

new = data[['read_scr', 'str', 'avginc']]


def beta(b):
    value = 0
    for i in range(0, len(new)):
        value += ((b[1]*new.iloc[i,1] + b[2]*new.iloc[i,2] + b[0] - new.iloc[i,0])**2) / (2*len(new))
        return value
    

result = op.minimize(beta, (2, 15, 18))
result


#Way 2
#HW for Session 05: Machine Learning
import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('C:\\Users\\승우\\Desktop\\caschool.csv', engine='python')
new = data[['read_scr', 'str', 'avginc']]

#cost function에는, 문제에서 제시했던대로 beta1, beta2, 상수의 순서대로, 하나의 리스트로 넣어줄 것

def cost(beta):
    value = 0
    for i in range(0, len(new)):
        value += ((beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] + beta[0] - new.iloc[i,0])**2) / (2*len(new))
        return value

def costd(beta) :
    J0 = 0
    J1 = 0
    J2 = 0
    for i in range(len(new)):
        J0 += (beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] - new.iloc[i,0]) / len(new)
    for i in range(len(new)):
        J1 += (beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] - new.iloc[i,0])*new.iloc[i,1] / len(new)
    for i in range(len(new)):
        J2 += (beta[1]*new.iloc[i,1] + beta[2]*new.iloc[i,2] - new.iloc[i,0])*new.iloc[i,2] / len(new)
    return [J0, J1, J2]
    
    
alpha = 0.002
ini = [10,10,2]
algo = [ini[1]-alpha*costd(ini)[1], ini[2]-alpha*costd(ini)[2],ini[0]-alpha*costd(ini)[0]]

def result(i, a):
    
    if (cost(algo) > cost(ini)):
        print ("Learning rate is too large")
    
    else:
        while(True):
            ini = algo
            algo = [ini[1]-alpha*costd(ini)[1], ini[2]-alpha*costd(ini)[2], ini[0]-alpha*costd(ini)[0]]
            if (cost(ini)-cost(algo) < 0.005):
                break
                    
    return(ini)
 
print(result(ini, algo), cost(result(ini,algo)))
    
