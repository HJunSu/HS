##거북이로 구구단 출력하기##
##변수설정 거북이 좌표, 구구단 앞에 숫자, 뒤에숫자

import turtle

x=0
y=0
a=0
b=0

swidth =700
sheight = 400

##2019038081_황준수

if __name__ =="__main__":
    turtle.title('거북이 구구단 출력')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    x,y = -500, 200
    turtle.goto(x,y)

    for a in range(1,10):
        for b in range(2,10):
            turtle.goto(x+80*b, y-40*a)
            rnrneks = str(b)+'x'+str(a)+'='+str(b*a)
            turtle.write(rnrneks, font = ('Arial',15,'bold'))

    turtle.done()
