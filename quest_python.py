# 문제 1
def solution(n, money):
    items = []
    for i in money:
        lst = list(range(n//i+1))
        items.append(lst)
    from itertools import product
    cases = list(product(*items))
    sslst = []
    for t in cases:
        ss = 0
        i = 0
        while i <= len(t)-1:
            ss += t[i]*money[i]
            i += 1
            if i == len(t):
                sslst.append(ss)
                break
    count = 0
    for e in sslst:
        if e == n:
            count += 1
    return(count/1000000007)



# 문제 2
def f4(k):
    lst1 = list(enumerate(k))
    lst2 = list(map(lambda i: i[0], lst1))
    lst3 = list(filter(lambda x: x%2 == 0, lst2))
    from functools import reduce
    lst4 = reduce(lambda x, y: x + y, lst3)
    print(lst4)



# 문제 3
import pandas as pd
try:
    f = pd.read_csv("C:\\Users\\renoi\\Documents\\diamonds_data2.csv")
except FileNotFoundError:
    print('wrong file path')
df = pd.DataFrame(f)
df = pd.DataFrame(f, columns=['z','y','x','price','table','depth','carat','-'])
df
df.to_csv("C:\\Users\\renoi\\Documents\\diamonds_data3.csv")
