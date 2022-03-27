##기차의 수송량 목록 예제에 나와있는대로
##같은 순위 여러번나올시 같은 순위만큼 건너뛰고 다음 순위 출력
##튜플은 딕셔너리로 변경한 후 다시 딕셔너리를 튜플로 정렬
import operator

##2019038081_황준수

traintnthd= [('토마스', 5),('헨리',8),('에드워드',9),('에밀리',5),('토마스',4),('헨리',7),('토마스',3),('에밀리',8),('퍼시',5),('고든',13)]
traindic, trainlist={},[]
traintup = None
total, rank=1,1

if __name__ == "__main__":
    for traintup in traintnthd :
        tName = traintup[0]
        tWeight = traintup[1]
        if tName in traindic:
            traindic[tName] += tWeight
        else:
            traindic[tName] = tWeight

    print('기차 수송량 목록 ==> ', traintnthd)
    print('------------------------------------')
    trainlist = sorted(traindic.items(), key=operator.itemgetter(1),
                       reverse = True)
    print('기차\t      총 수송량\t        순위')
    print('------------------------------------')
    print(trainlist[0][0],  '   \t', trainlist[0][1], '     \t', rank)
    for i in range(1,len(trainlist)) :
        total +=1
        if trainlist[i][1]==trainlist[i-1][1]:
            pass
        else:
            rank = total
        print(trainlist[i][0],'   \t',trainlist[i][1],'     \t', rank)
            
