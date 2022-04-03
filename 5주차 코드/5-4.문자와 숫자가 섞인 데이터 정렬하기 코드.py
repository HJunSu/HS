##문자와 숫자가 섞인 데이터 정렬하기
##1. 문자와 숫자가 섞인 데이터에서 숫자 기준으로 데이터 정렬
##2. 16진수 취급했던 수를 문자로 취급

import random

def getNumber(strData):
    numStr = ''
    for ch in strData:
        if ch.isdigit():
            numStr += ch

    return int(numStr)

##2019038081_황준수
data =[]
i,j = 0,0

if __name__ == "__main__" :
    for i in range(0, 10) :
        tmp = hex(random.randrange(0, 100000))
        tmp =tmp[2:]
        data.append(tmp)
    print('정렬 전 데이터 : ', end = ' ')
    [print(num, end = ' ') for num in data]

    for i in range(0, len(data) -1):
        for j in range(i +1, len(data)):
            if getNumber(data[i])>getNumber(data[j]):
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
    print('\n정렬 후 데이터 : ',end = ' ')
    [print(num, end=' ') for num in data]
