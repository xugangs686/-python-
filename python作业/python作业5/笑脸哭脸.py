import turtle as t

data=[[-150,0],[150,0]]#数据

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
#哭脸的嘴
def zui2(x,y):
    t.penup()
    t.goto(x,y+70)
    t.pendown()
    t.setheading(0)
    t.color("brown")
    t.circle(-50,80)
    t.penup()
    t.goto(x,y+70)
    t.pendown()
    t.setheading(0)
    t.circle(-50,-80)
    
    

def xiao_lian(x,y):
    t.penup()     #脸
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","yellow")
    t.circle(100,360)
    t.end_fill()
    #左眼睛
    yanjing1(x,y)
    #右眼
    yanjing2(x,y)
    #嘴
    zui1(x,y)

def ku_lian(x,y):
    t.penup()     #脸
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","yellow")
    t.circle(100,360)
    t.end_fill()
    #左眼睛
    yanjing1(x,y)
    #右眼
    yanjing2(x,y)
    #嘴
    zui2(x,y)

t.hideturtle()
xiao_lian(data[0][0],data[0][1])
ku_lian(data[1][0],data[1][1])
