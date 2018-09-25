# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.

#n 원을 1~m 까지 m가지 돈이 있을 때 이를 거슬러 줄 수 있는 방법의 수를 구하는 상황
for n in range(1,100001):
    # n이 100000원 이하의 자연수라는 가정
    for m in range(0,101):
    # m이 최대 100이라는 가정
        def solution(n, m):
            if n<0 or m<=0:
                return 0
            # n<m인 경우 n-m<0이 되는 경우 고려.
            elif n==0:
                return 1 
            # n=0인 경우 0원을 표현하는 방법은 m값에 관계없이 항상 0
            answer = (solution(n, m-1) + solution(n-m, m))%1000000007
            return answer
            # 이 함수는 가장 큰 화폐 m이 방법에 포함 되는지 안되는지로 나누어 생각
            # 포함되지 않는 것들은 solution(n,m-1)과 같음
            # 포함되는 것들은 이미 n원에 m원을 포함한 상태이니 빼고 생각해 solution(n-m,m)

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate

def f4(x):
    xlist=list(enumerate(x))
    #x의 (인덱스 넘버,원소)형태의 집합 'xlist' 생성
    even_set= list(filter(lambda x: x[0]%2==0,xlist))
    #'xlist'집합에서 인덱스 넘버가 짝수인 것들만 필터링한 집합 'even_set' 생성
    return(sum(list(map(lambda x: x[0], even_set))))
    #'even_set'집합의 각 원소들의 첫번째 숫자들이 인덱스 넘버. 이들만 뽑아서 합함.

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

import pandas as pd
try:
    dia = pd.read_csv(r'C:\Users\EdwinPark\diamonds_data.csv')
except FileNotFoundError:
    print('"Wrong File Path"')
    # csv파일을 불러오는 코드를 생성하고 경로 or 파일명 오류 시 발생하는 FileNotFoundError 발생 시 예외 처리하는 코드 생성
reversed_dia= list(dia.columns[0:8])
# dia라는 데이터의 열을 나타내는 리스트
reversed_dia.reverse()
# 위의 리스트의 원소들을 뒤집어서 배열한 리스트를 생성
dia=dia[reversed_dia]
# 뒤집은 리스트의 열의 순서대로 column들을 재배열
dia.to_csv('new_diamonds_data.csv')
# 새로 생성된 csv파일을 new_diamonds_data.csv로 저장!
