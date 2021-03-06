## 문자열에서 문자의 발생 빈도 세기
## 긴 장문에서 각 문자의 발생 빈도 세기
## 출력은 빈도수가 높은 글자부터 출력
## 단 한글만 빈도수를 세고 나머지는 무시
import operator

countDic={}
countList=[]

##2019038081_황준수
if __name__ == "__main__":
    a = '''원문
 내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸시에 지나지 않았다.
내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다.
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.'''
    print(a)    
    print("\n--------------------")
    print("\n문자\t빈도수      ")
    print("\n--------------------\n")

    for ch in a:
        if 'ㄱ' <=ch and ch<= '힣' :
            if ch in countDic:
                countDic[ch] +=1
            else :
                countDic[ch] = 1

    countList = sorted(countDic.items(), key = operator.itemgetter(1),reverse = True)
    for i in range(0, len(countList)):
        print(countList[i][0], '\t', countList[i][1])
    
