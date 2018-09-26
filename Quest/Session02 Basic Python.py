# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.
def change(k,coin):
    coin.sort()
    a=[0]*(k+1)
    a[0]=1
    for c in coin:
        for i in range(1,k+1):
            if i>=c:
                a[i]+=a[i-c]
    return a[-1] % 1000000007

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate
 def f4(x):
    a=list(enumerate(x))
    lst=list(filter(lambda x:x[0]%2==0,a))
    b=list(map(lambda y:y[0],lst))
    c=b.pop()/2
    return int(c*(c+1))
                

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)
import pandas as pd
try:
    data1=pd.read_csv('C:\diamonds_data.csv')
except FileNotFoundError as e:
    e="wrong file path"
    print(e)
else:
    data2=data1[['z','y','x','price','table','depth','carat','-']]
    data2.to_csv('diamonds_data2.csv')
