# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.


#계속 IndexError: list index out of range가 뜨는데 어디서 잘못된건지 도통 모르겠습니다...
#Index문제를 해결하면 다시금 수정하여 올리도록 하겠습니다...
def solution(n, money):
    money.sort()
    money.reverse()

    def solution2(nn, money2):
        maximum_value = money2[0]
        quo = nn // maximum_value
        another = money2[1:]
        answer = 0
        if maximum_value > nn:
            if money2:
                solution2(nn, another)
            else:
                return 0
        else:
            for i in range(quo, -1, -1):
                nnn = nn - (maximum_value * i)

                if nnn < 0:
                    continue
                elif nnn == 0:
                    answer += 1
                else:
                    if money2:
                        answer += solution2(nnn, another[1:])
                    else:
                        return answer

        return answer % 1000000007
    return solution2(n, money)


print(solution(5, [1,2,5]))

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate


#Way1
import numpy as np

def f4(x):
    x1 = list(enumerate(x))
    x2 = np.array(x1)
    x3 = x2[x2[:, 0] % 2 == 0, ]
    x4 = sum(x3[:, 0])
    print(x4)

f4([1,2,3,4])
f4([1,2,3,4,5])

#Way2
def f4(x):
    x1 = list(filter(lambda x: x[0]%2==0, list(enumerate(x))))
    x2 = (sum(list(map(lambda x: x[0], x1))))
    print(x2)

f4([1,2,3,4])
f4([1,2,3,4,5])

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)


import csv
import pandas as pd

try:
    f = open('C:\\Users\\승우\\Desktop\\diamonds_data.csv', 'r')
    cf = csv.reader(f)
    listed = list(cf)
    f.close()

    df = pd.DataFrame(data=listed, columns=listed[0])
    df2 = df.drop(df.index[0])

    col = list(df2.columns)

    col2 = list(col)
    col2.reverse()

    df3 = df2[col2]

    df3.to_csv('C:\\Users\\승우\\Desktop\\diamonds_data_changed.csv', mode='w')

except WrongFilePath:
    print('wrong file path')
