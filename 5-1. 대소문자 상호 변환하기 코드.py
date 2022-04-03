##대 소문자 상호 변환하기
##1.swapcase() 함수 사용 x 대문자는 소문자로 변환 소문자는 대문자로 변환
##2.lower()과 upper()함수는 일괄적으로 소문자나 대문자로 변환해 바로 사용 x
##3. 즉 단어하나씩 추출해 대문자면 lower() 소문자면 upper()을 쓰도록해야함

##2019038081_황준수
if __name__ == "__main__":
    a = ""
    b = ""
    c = ""
    i = 0
    long = ""
    ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","N","M","O","P","Q"
           ,"R","S","T","U","V","W","X","Y","Z"]
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q"
           ,"r","s","t","u","v","w","x","y","z"]
    a = input("문자열을 입력하세요 : ")
    long = len(a)
    for i in range(0, long):
        if (a[i] in ABC):
            b = a[i].lower()
        elif (a[i] in abc):
            b = a[i].upper()
        else:
            b = a[i]

        c += b

    print("대소문자 변환 결과 --> %s"%c)
        
