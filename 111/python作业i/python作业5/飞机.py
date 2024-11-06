import turtle as t

data=[0,100,50,150,-300,-50,-85,-125,-80,-30,120,-200,10,100,-150,-5,250,200,250,75,25]
def plane(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14, x15, y15, x16, y16, x17, y17, x18, y18, x19, y19, x20, y20):
    # 飞机
    t.pensize(5)
    t.color("black", "blue")
    t.begin_fill()
    t.goto(x1, y1)
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.end_fill()
    t.color("black")
    t.goto(x4, y4)
    t.goto(x5, y5)
    t.goto(x6, y6)
    t.color("black", "blue")
    t.begin_fill()
    t.goto(x7, y7)
    t.goto(x8, y8)
    t.end_fill()
    t.goto(x9, y9)
    t.color("black", "blue")
    t.begin_fill()
    t.goto(x10, y10)
    t.goto(x11, y11)
    t.end_fill()
    # 线
    t.pensize(2)
    t.penup()
    t.goto(x12, y12)
    t.pendown()
    t.color("black")
    t.goto(x13, y13)

    t.penup()
    t.goto(x14, y14)
    t.pendown()
    t.color("black")
    t.goto(x15, y15)

    t.penup()
    t.goto(x16, y16)
    t.pendown()
    t.color("black")
    t.goto(x17, y17)

    t.penup()
    t.goto(x18, y18)
    t.pendown()
    t.color("black")
    t.goto(x19, y19)

    t.penup()
    t.goto(x20, y20)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(50, 360)
    t.end_fill()

t.hideturtle()
plane(data[1],data[2],data[4],data[3],data[0],data[0],data[9],data[7],data[5],data[5],data[4],data[3],data[7],data[7],data[5],data[5],data[6],data[6],data[9],data[7],data[5],data[5],data[8],data[7],data[7],data[11],data[12],data[8],data[13],data[14],data[2],data[15],data[16],data[9],data[19],data[20],data[17],data[0],data[16],data[17])

    

