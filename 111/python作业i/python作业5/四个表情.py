import turtle as t

data=[[-150,100],[-150,-150],[150,100],[150,-150]]#数据

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
    
#死鱼眼左（无精打采）
def siyu_yan1(x,y):
    t.penup()
    t.goto(x-50,y+110)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","white")
    t.forward(30)
    t.circle(5,90)
    t.forward(10)
    t.circle(5,90)
    t.forward(30)
    t.circle(5,90)
    t.forward(10)
    t.circle(5,90)
    t.end_fill()
    t.penup()
    t.goto(x-50,y+130)
    t.pendown()
    t.setheading(-90)
    t.begin_fill()
    t.color("black")
    t.circle(10,90)
    t.forward(10)
    t.circle(10,90)
    t.end_fill()
    t.hideturtle()
#死鱼眼右（无精打采）
def siyu_yan2(x,y):
    t.penup()
    t.goto(x+40,y+110)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","white")
    t.forward(30)
    t.circle(5,90)
    t.forward(10)
    t.circle(5,90)
    t.forward(30)
    t.circle(5,90)
    t.forward(10)
    t.circle(5,90)
    t.end_fill()
    t.penup()
    t.goto(x+40,y+130)
    t.pendown()
    t.setheading(-90)
    t.begin_fill()
    t.color("black")
    t.circle(10,90)
    t.forward(10)
    t.circle(10,90)
    t.end_fill()
    t.hideturtle()

#表情4的嘴
def zui3(x,y):
    t.penup()
    t.goto(x,y+30)
    t.pendown()
    t.setheading(0)
    t.color("brown")
    t.circle(30,70)
    t.penup()
    t.goto(x,y+30)
    t.pendown()
    t.setheading(0)
    t.circle(30,-70)

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




#死鱼脸（无精打采）
def siyu_lian(x,y):
    t.penup()     #脸
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","yellow")
    t.circle(100,360)
    t.end_fill()
    #左眼睛
    siyu_yan1(x,y)
    #右眼
    siyu_yan2(x,y)
    #嘴
    t.penup()     
    t.goto(x-25,y+50)
    t.pendown()
    t.setheading(0)
    t.color("brown")
    t.forward(50)
    
#表情4（看不出来是什么表情）
def lian4(x,y):
    t.penup()     #脸
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.color("brown","yellow")
    t.circle(100,360)
    t.end_fill()
    #左眼睛
    siyu_yan1(x,y)
    #右眼
    siyu_yan2(x,y)
    #嘴
    zui3(x,y)

xiao_lian(data[0][0],data[0][1])
siyu_lian(data[1][0],data[1][1])
ku_lian(data[2][0],data[2][1])    
lian4(data[3][0],data[3][1])
t.hideturtle()
