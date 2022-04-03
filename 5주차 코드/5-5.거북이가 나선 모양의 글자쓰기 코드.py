## [프로그램1]변경 글자가 나선형으로 안쪽으로 써지도록
## 1. 화면을 500x500 정도로, 중심에서 반지름 200 글자 크기 20고정
## 2. 2바퀴를 돌리면 360*2도에서 물자열의 개수만큼 나눠 각도 회전하며 글자쓰기
## 3. 거리와 각도로 좌표 구하기
## 3-1. x 좌표 = 거리 * cos(각도), y 좌표 = 거리 * sin(각도)
## 4. cos(), sin()각도는 라디안값으로 처리 3.14 * 각도 / 180
import turtle
import random
import math
from tkinter.simpledialog import *


#2019038081_황준수
inStr =''
sw,sh=300,300
x,y, txtSize = 0, 0,20
radius, angle, radian= 200, 360 , 0
    
turtle.title('거북이가 나선 모양의 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=sw+50, height=sh+50)
turtle.screensize(sw,sh)
turtle.penup()

inStr=askstring('문자열 입력','거북이가 쓸 문자열을 입력')
angle = 360*2/ len(inStr)

for ch in inStr:
    radian = 3.14*angle/180
    x = radius*math.cos(radian)
    y = radius*math.sin(radian)
    r= random.random(); g=random.random(); b=random.random()

    turtle.goto(x,y)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))
    
    radius *=((len(inStr)-len(ch))/len(inStr))
    angle += 720 / len(inStr)
            
turtle.done()

