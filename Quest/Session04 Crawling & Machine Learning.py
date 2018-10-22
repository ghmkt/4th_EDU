# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
import pandas as pd


path = '/Users/daham/downloads/chromedriver'

driver = webdriver.Chrome(path)

original_url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=sh m&sid2=269&sid1=100"
driver.get(original_url)

time.sleep(2)
url = driver.current_url
html = urlopen(url)
soup = BeautifulSoup(html,"lxml",from_encoding='utf-8')

url_list = []

txt = soup.div(class_='paging')
get_max_page_num = max(re.findall('\>([\d])', str(txt)))

for i in range(1, int(get_max_page_num)+1):
    url = driver.current_url
    html = urlopen(url)
    soup = BeautifulSoup(html,"lxml",from_encoding='utf-8')
    articles = soup.find_all("dt")
    
    for link in articles:
        url_list.append(link.find("a")["href"])
    
    current_page = re.findall('strong\>([\d])', str(txt))[0]
    if str(i) == current_page:
        pass
    else:
        driver.find_element_by_link_text(str(i)).click()
    
url_list2 = list(set(map(lambda x : x.replace(' ', ''), url_list)))

result_df = pd.DataFrame(columns=['기사 제목', '내용'])

hangul = re.compile('[^ ㄱ-ㅣ가-힣|0-9.'']+')
for i in range(len(url_list2)):
    html = urlopen(url_list2[i])
    soup = BeautifulSoup(html,"html.parser",from_encoding='utf-8')
    content = soup.find("div",{"id":"articleBodyContents"})
    title = soup.find("h3",{"id":"articleTitle"}).find(text=True)
    result = hangul.sub('',str(content))
    result = re.sub('본문 내용  플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
    result = re.sub('본문 내용  플레이어   동영상 뉴스       영상 플레이어   플레이어    오류를 우회하기 위한 함수 추가','',result)
    
    result_df.loc[i, '기사 제목'] = title
    result_df.loc[i, '내용'] = result

print(result_df)


# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.

import pandas as pd
import numpy as np

def predict(x_i, beta):
    # N * 1 vector
    result = np.dot(x_i, beta)
    return result

def error(x_i, y_i, beta):
    # N * 1 vector
    return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
    # 1 * 1 Matrix
    return np.dot(error(x_i, y_i, beta).T, error(x_i, y_i, beta))

def squared_error_gradient(x_i, y_i, beta):
    # K * 1 vector
    return -2 * np.dot(x_i.T, error(x_i, y_i, beta))

def minimize_stochastic(target_fn, gradient_fn, x, y, beta_0, alpha_0):
    data = np.concatenate((x, y.reshape(-1,1)), axis=1)
    beta = beta_0
    alpha = alpha_0
    min_beta, min_error = None, np.inf
    iterations_with_no_improvement = 0
    
    print('initial error: ', target_fn(x, y, beta))
    while iterations_with_no_improvement < 1000:
        
        error = target_fn(x, y, beta)
        
        if error < min_error:
            min_beta, min_error = beta, error
            iterations_with_no_improvement += 1
            alpha = alpha_0
        else:
            iterations_with_no_improvement += 1
            alpha *= 0.9
            
        print('beta: ', beta)
        print('gradient: ', gradient_fn(x, y, beta))
        print('error: ', error)
        beta = beta - (alpha * gradient_fn(x, y, beta))
        
    return min_beta


def estimate_beta(x, y, alpha):
    beta_initial = [np.random.random() for x_i in x[0]]
    return minimize_stochastic(squared_error, squared_error_gradient, x, y, beta_initial, alpha)

cashschool = pd.read_csv('/Users/daham/Desktop/GrowthHackers/4th-EDU/Session/caschool.csv')
csv_data = cashschool.loc[:, ['str', 'avginc']]
x = np.array(csv_data)
y = np.array(cashschool.read_scr)

print('정답: ', estimate_beta(x,y, 0.000001))

import statsmodels.api as sm
model = sm.OLS(y, x)
results = model.fit()
results.summary()

# OLS 한 것과 같은 Coefficient 출력 확인 완료


# Machine Learning Quest 2
# 앤드류 강의 week1과 week2에서 필요한 강의 듣고 중요 내용 요약해서 올리기
# https://www.coursera.org/learn/machine-learning
