import turtle as t
import time

t1=t.Turtle()
t2=t.Turtle()

#模块程序设计
def move1(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
def move2(x,y):
    t2.penup()
    t2.goto(x,y)
    t2.pendown()

#旗杆
def pole(x,y):
    t1.color("black")
    t1.setheading(0)
    move1(x,y)
    t1.begin_fill()
    t1.forward(10)
    t1.left(90)
    t1.forward(800)
    t1.left(90)
    t1.forward(10)
    t1.left(90)
    t1.forward(800)
    t1.left(90)
    t1.forward(10)
    t1.end_fill()

#旗面
def flag(x,y):
    t2.setheading(0)
    move2(x,y)
    t2.begin_fill()
    t2.color("red","red")
    t2.forward(300)
    t2.left(90)
    t2.forward(200)
    t2.left(90)
    t2.forward(300)
    t2.left(90)
    t2.forward(200)
    t2.left(90)
    t2.forward(300)
    t2.end_fill()
#星星
def star(an,x,y,L):
    t2.setheading(an)
    move2(x,y)
    t2.begin_fill()
    t2.color("yellow","yellow")
    t2.forward(L)
    t2.right(144)
    t2.forward(L)
    t2.right(144)
    t2.forward(L)
    t2.right(144)
    t2.forward(L)
    t2.right(144)
    t2.forward(L)
    t2.right(144)
    t2.forward(L)
    t2.end_fill()
#中国国旗
def china_flag(x,y):
    flag(x,y)
    star(0,-360,160+y,35)
    star(36,-315,180+y,15)
    star(36,-315,130+y,15)
    star(18,-295,165+y,15)
    star(18,-295,145+y,15)
#启动！

t1.speed(0)
t1.hideturtle()
t.tracer(0)
pole(-410,-400)
t.tracer(1)
i=0
while(1):
    time.sleep(0.4)
    t2.clear()
    t2.hideturtle()
    #消除再一起弹出来
    t.tracer(0)
    china_flag(-400,-400+i*10)
    t.tracer(10.1)
    #i+=1表示增加，递增
    i+=1
    if(i==60):
        break        #break表示终止循环
