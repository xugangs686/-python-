import turtle as t

def star(x,y):
    t.penup()
    t.goto(x-80,y+176)
    t.pendown()
    t.setheading(0)
    t.color("white")
    t.begin_fill()
    t.forward(164)
    t.right(144)
    t.forward(164)
    t.right(144)
    t.forward(164)
    t.right(144)
    t.forward(164)
    t.right(144)
    t.forward(164)
    t.end_fill()
    t.hideturtle()

#左眼
def yanjing1(x,y):
    t.penup()
    t.goto(x-30,y+130)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","white")
    t.circle(15,360)
    t.end_fill()
    t.penup()
    t.goto(x-30,y+130)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("black")
    t.circle(10,360)
    t.end_fill()

#右眼
def yanjing2(x,y):
    t.penup()
    t.goto(x+30,y+130)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","white")
    t.circle(15,360)
    t.end_fill()
    t.penup()
    t.goto(x+30,y+130)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("black")
    t.circle(10,360)
    t.end_fill()
#笑脸的嘴
def zui1(x,y):
    t.penup()
    t.goto(x,y+30)
    t.pendown()
    t.setheading(0)
    t.color("brown")
    t.circle(50,80)
    t.penup()
    t.goto(x,y+30)
    t.pendown()
    t.setheading(0)
    t.circle(50,-80)

def xiao_lian(x,y):
    t.penup()     #脸
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","yellow")
    t.circle(90,360)
    t.end_fill()
    #左眼睛
    yanjing1(x,y)
    #右眼
    yanjing2(x,y)
    #嘴
    zui1(x,y)


def meiguoguizhang(x,y):
    #红色
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("red")
    t.circle(150,360)
    t.end_fill()
    #
    t.penup()
    t.goto(x,y+20)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("white")
    t.circle(130,360)
    t.end_fill()
    #
    t.penup()
    t.goto(x,y+40)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("red")
    t.circle(110,360)
    t.end_fill()
    #
    t.penup()
    t.goto(x,y+60)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("blue")
    t.circle(90,360)
    t.end_fill()
    #
    star(x,y)
#升级版
def meiguoguizhang111(x,y):
    #红色
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("red")
    t.circle(150,360)
    t.end_fill()
    #
    t.penup()
    t.goto(x,y+20)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("white")
    t.circle(130,360)
    t.end_fill()
    #
    t.penup()
    t.goto(x,y+40)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("red")
    t.circle(110,360)
    t.end_fill()
    #
    xiao_lian(x,y+60)

    
t.hideturtle()
meiguoguizhang(150,-200)
meiguoguizhang111(-150,-200)
