## 하트 모양 출력하기
## 숫자 쓰고 5914 일떄 처음 하트 5개 9개 1개 4개 순서 출력

a, b, c=0,0,0
nStr, ch, hStr = "","",""


##2019038081_황준수
if __name__ == "__main__":
    nStr = input ("숫자를 여러 개 입력하세요 : ")
    print("")
    a = 0
    ch = nStr[a]
    while True:
        c = int(ch)

        hStr=""
        for b in range(0, c):
            hStr += "♥"
            b +=1

        print(hStr)

        a +=1
        if(a > len(nStr)-1):
            break

        ch = nStr[a]
