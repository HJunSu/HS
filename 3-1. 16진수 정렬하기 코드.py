##16진수 저장된 리스트 정렬
##sort()나 sorted() 사용하지 않고 정렬
##실행결과 보니 10개 돌렸다.

import random

data=[]
i,k=0,0
##2019038081_황준수
if __name__ == "__main__":
    for i in range(0,10):
        tmp = hex(random.randrange(0,50000))
        data.append(tmp)

    print('정렬 전 데이터 : ', end=' ')
    [print(num,end=' ')for num in data]

    for i in range(0, len(data)-1):
        for k in range(i+1, len(data)):
            if int(data[i], 16) > int(data[k],16):
                tmp=data[i]
                data[i]=data[k]
                data[k]= tmp

    print('\n정렬 후 데이터 : ', end = '')
    [print(num,end=' ')for num in data]
