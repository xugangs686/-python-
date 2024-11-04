import turtle as t

#模块程序设计
def flag(x,y):
    t.setheading(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("red","red")
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(300)
    t.end_fill()

def star(an,x,y,L):
    t.setheading(an)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("yellow","yellow")
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.end_fill()


def china_flag(x0,y0,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    flag(x0,y0)
    star(0,x1,y1,35)
    star(36,x2,y2,15)
    star(36,x3,y3,15)
    star(18,x4,y4,15)
    star(18,x5,y5,15)


china_flag(-400,100,-360,260,-315,280,-315,230,-295,265,-295,245)
china_flag(-400,-400,-360,-250,-315,-280,-315,-230,-295,-265,-295,-245)
china_flag(0,100,40,260,85,280,85,230,105,265,105,245)
china_flag(0,-400,40,-250,85,-280,85,-230,105,-265,105,-245)
t.hideturtle()
