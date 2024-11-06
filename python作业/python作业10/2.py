import turtle as t

red=[[269,-15,"red"],[296,3,"red"],[296,-33,"red"],[323,-15,"red"],[323,18,"red"],[323,-48,"red"],[354,0,"red"],[354,-33,"red"],[354,-66,"red"],[354,33,"red"],[383,-15,"red"],[383,18,"red"],[383,-48,"red"],[383,50,"red"],[383,-80,"red"]]
white=[-350,-15,"white"]
juce=[-250,-15,"#ffa500"]
green=[-250,85,"#008000"]
yellow=[-250,-115,"#ffa500"]
blue=[10,-15,"blue"]
pink=[200,-15,"pink"]
black=[440,-15,"black"]
def ball(x,y,an):
    t.seth(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(an)
    t.begin_fill()
    t.circle(15,360)
    t.end_fill()


def xian():
    t.seth(0)
    t.penup()
    t.goto(-250,300)
    t.pendown()
    t.color("black")
    t.right(90)
    t.fd(200)
    t.seth(0)
    t.circle(-100,-180)
    t.right(90)
    t.fd(200)
    t.right(180)
    t.fd(400)

def half_circle1():
    t.seth(0)
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.left(90)
    t.color("#808080")
    t.begin_fill()
    t.circle(15,180)
    t.end_fill()

def half_circle2():
    t.seth(0)
    t.penup()
    t.goto(-30,-300)
    t.pendown()
    t.right(90)
    t.color("#808080")
    t.begin_fill()
    t.circle(15,180)
    t.end_fill()

def half_circleall():
    half_circle1()
    half_circle2()

def circle1():
    t.seth(0)
    t.penup()
    t.goto(-600,285)
    t.pendown()
    t.color("#808080")
    t.begin_fill()
    t.circle(15,360)
    t.end_fill()

def circle2():
    t.seth(0)
    t.penup()
    t.goto(600,285)
    t.pendown()
    t.color("#808080")
    t.begin_fill()
    t.circle(15,360)
    t.end_fill()

def circle3():
    t.seth(0)
    t.penup()
    t.goto(-600,-315)
    t.pendown()
    t.color("#808080")
    t.begin_fill()
    t.circle(15,360)
    t.end_fill()

def circle4():
    t.seth(0)
    t.penup()
    t.goto(600,-315)
    t.pendown()
    t.color("#808080")
    t.begin_fill()
    t.circle(15,360)
    t.end_fill()

def circle_all():
    circle1()
    circle2()
    circle3()
    circle4()


def jiao1():
    t.seth(0)
    t.penup()
    t.goto(-600,340)
    t.pendown()
    t.color("black","#a9a9a9")
    t.begin_fill()
    t.circle(-40,-90)
    t.right(90)
    t.fd(40)
    t.left(90)
    t.fd(40)
    t.end_fill()

def jiao2():
    t.seth(0)
    t.penup()
    t.goto(600,340)
    t.pendown()
    t.color("black","#a9a9a9")
    t.begin_fill()
    t.circle(-40,90)
    t.right(90)
    t.fd(40)
    t.right(90)
    t.fd(40)
    t.end_fill()

def jiao3():
    t.seth(0)
    t.penup()
    t.goto(600,-340)
    t.pendown()
    t.color("black","#a9a9a9")
    t.begin_fill()
    t.circle(40,90)
    t.left(90)
    t.fd(40)
    t.left(90)
    t.fd(40)
    t.end_fill()

def jiao4():
    t.seth(0)
    t.penup()
    t.goto(-600,-340)
    t.pendown()
    t.color("black","#a9a9a9")
    t.begin_fill()
    t.circle(40,-90)
    t.left(90)
    t.fd(40)
    t.right(90)
    t.fd(40)
    t.end_fill()

def jiao_all():
    jiao1()
    jiao2()
    jiao3()
    jiao4()
    

def redbian():
    t.seth(0)
    t.penup()
    t.goto(-600,340)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.fd(1200)
    t.circle(-40,90)
    t.fd(600)
    t.circle(-40,90)
    t.fd(1200)
    t.circle(-40,90)
    t.fd(600)
    t.circle(-40,90)
    t.end_fill()
    

def zuobu():
    t.seth(0)
    t.penup()
    t.goto(-600,300)
    t.pendown()
    t.color("#006400")
    t.begin_fill()
    t.fd(1200)
    t.right(90)
    t.fd(600)
    t.right(90)
    t.fd(1200)
    t.right(90)
    t.fd(600)
    t.end_fill()

def qiuzuo():
    t.speed(100)
    redbian()
    zuobu()
    jiao_all()
    circle_all()
    half_circleall()
    xian()
    t.hideturtle()

def red_ball(x1,y1,an1,x2,y2,an2,x3,y3,an3,x4,y4,an4,x5,y5,an5,x6,y6,an6,x7,y7,an7,x8,y8,an8,x9,y9,an9,x10,y10,an10,x11,y11,an11,x12,y12,an12,x13,y13,an13,x14,y14,an14,x15,y15,an15):
    ball(x1,y1,an1)
    ball(x2,y2,an2)
    ball(x3,y3,an3)
    ball(x4,y4,an4)
    ball(x5,y5,an5)
    ball(x6,y6,an6)
    ball(x7,y7,an7)
    ball(x8,y8,an8)
    ball(x9,y9,an9)
    ball(x10,y10,an10)
    ball(x11,y11,an11)
    ball(x12,y12,an12)
    ball(x13,y13,an13)
    ball(x14,y14,an14)
    ball(x15,y15,an15)
    
    
qiuzuo()
ball(-250,-15,"#ffa500")
red_ball(red[0][0],red[0][1],red[0][2],red[1][0],red[1][1],red[1][2],red[2][0],red[2][1],red[2][2],red[3][0],red[3][1],red[3][2],red[4][0],red[4][1],red[4][2],red[5][0],red[5][1],red[5][2],red[6][0],red[6][1],red[6][2],red[7][0],red[7][1],red[7][2],red[8][0],red[8][1],red[8][2],red[9][0],red[9][1],red[9][2],red[10][0],red[10][1],red[10][2],red[11][0],red[11][1],red[11][2],red[12][0],red[12][1],red[12][2],red[13][0],red[13][1],red[13][2],red[14][0],red[14][1],red[14][2])
ball(white[0],white[1],white[2])
ball(juce[0],juce[1],juce[2])
ball(yellow[0],yellow[1],yellow[2])
ball(green[0],green[1],green[2])
ball(blue[0],blue[1],blue[2])
ball(pink[0],pink[1],pink[2])
ball(black[0],black[1],black[2])



