## 거북이 서로 만나게 하기
## 거북이 세마리, 만날 때까지, 화면을 임의로 돌아다님.
## 세 마리 중 서로 만나는 거북이가 있을시, 멈추고 모든 거북이 크기 세 배로 키움

import turtle
import math
import random

t1, t2, t3 = [None] *3
x1,y1,x2,y2,x3,y3 = [0] *6
sw, sh = 300, 300
##2019038081_황준
if __name__ == "__main__" :
    turtle.title('거북이 만나기')
    turtle.setup(width = sw + 50, height = sh + 50)
    turtle.screensize(sw,sh)
    

    t1=turtle.Turtle('turtle'); t1.color('red'); t1.penup()
    t2=turtle.Turtle('turtle'); t2.color('blue'); t2.penup()
    t3=turtle.Turtle('turtle'); t3.color('green'); t3.penup()

    t1.goto(-100,-100); t2.goto(0,0);t3.goto(100,100)

    while True :
        angle = random.randrange(0,360)
        distance = random.randrange(1,10)
        t1.left(angle); t1.forward(distance)
        angle = random.randrange(0,360)
        distance = random.randrange(1,10)
        t2.left(angle); t2.forward(distance)
        angle = random.randrange(0,360)
        distance = random.randrange(1,10)
        t3.left(angle); t3.forward(distance)
        
        x1 =t1.xcor(); y1 = t1.ycor()
        x2 =t2.xcor(); y2 = t2.ycor()
        x3 =t3.xcor(); y3 = t3.ycor()

        if (((math.sqrt((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2))) <=20) or
        ((math.sqrt((x1-x3)*(x1-x3))+((y1-y3)*(y1-y3))) <=20 )or
        ((math.sqrt((x2-x3)*(x2-x3))+((y2-y3)*(y2-y3))) <=20)):
            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
            break

turtle.done()
            
        
