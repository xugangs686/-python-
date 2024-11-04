import random as r
import turtle as t
#'\u2665'   #红心，'\u2660'   #黑桃，'\u2666'   #方块，'\u2663'   #梅花

#牌库
pk=['\u2665A v47','\u26652 v51','\u26653 v03','\u26654 v07','\u26655 v11','\u26656 v15','\u26657 v19','\u26658 v23', '\u26659 v27','\u266510 v31','\u2665J v35','\u2665Q v39','\u2665K v43',
    '\u2660A v48','\u26602 v52','\u26603 v04','\u26604 v08','\u26605 v12','\u26606 v16','\u26607 v20','\u26608 v24', '\u26609 v28','\u266010 v32','\u2660J v36', '\u2660Q v40','\u2660K v44',
    '\u2666A v45','\u26662 v49','\u26663 v01','\u26664 v05','\u26665 v09','\u26666 v13','\u26667 v17','\u26668 v21', '\u26669 v25','\u266610 v29','\u2666J v33','\u2666Q v37','\u2666K v41',
    '\u2663A v46','\u26632 v50','\u26633 v02','\u26634 v06','\u26635 v10','\u26636 v14','\u26637 v18','\u26638 v22', '\u26639 v26','\u266310 v30','\u2663J v34','\u2663Q v38','\u2663K v42',
    '小王 v53','大王 v54']

#角色
dizhu=[]
nm1=[]
nm2=[]
#for循环随机抽牌
for i in range(17):
    a=r.randint(0,len(pk)-1)
    nm1.append(pk[a])
    del pk[a]
    b=r.randint(0,len(pk)-1)
    nm2.append(pk[b])
    del pk[b]  

for j in range(20):
    num=r.randint(0,len(pk)-1)
    dizhu.append(pk[num])
    del pk[num]

#将牌排序*****先排序再画图
for j in range(len(dizhu)-1):
    for i in range(j+1,len(dizhu)):
        if(int(dizhu[j][-2:])<int(dizhu[i][-2:])):
            dizhu[j],dizhu[i]= dizhu[i],dizhu[j]
for j in range(len(nm1)-1):
    for i in range(j+1,len(nm1)):
        if(int(nm1[j][-2:])<int(nm1[i][-2:])):
            nm1[j],nm1[i]=nm1[i],nm1[j]
for j in range(len(nm2)-1):
    for i in range(j+1,len(nm2)):
        if(int(nm2[j][-2:])<int(nm2[i][-2:])):
            nm2[j],nm2[i]=nm2[i],nm2[j]

#牌
def one_fang_kuai(x,y,an):
    t.speed(100)
    t.setheading(0)    #seth=setheading
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("gray","white")
    t.begin_fill()
    t.fd(60)
    t.circle(10,90)
    t.fd(90)
    t.circle(10,90)
    t.fd(60)
    t.circle(10,90)
    t.fd(90)
    t.circle(10,90)
    t.end_fill()

    an2=an[1:3]
    an1=an[0:1]
    if(an=='小王 v53' or an=='大王 v54'):#将大小王转化成joker
        if(an=='小王 v53'):
            t.pencolor("black")
        else:
            t.pencolor("red")
        an="JOKER"
        for v in range(len(an)):#通过for循环将joker显现出来
            t.penup()
            t.goto(x+5,y+85-v*16)
            t.pendown()
            t.write(an[v],font=("Arial Black",16,"normal"))
    else:
        if(an1=='\u2665'or an1=='\u2666' or an1=='大'):#判断大小王以及牌的颜色
            t.pencolor("red")
        else:
            t.pencolor("black")

        if(an2=='10'):
            t.penup()
            t.goto(x-5,y+85)
            t.pendown()
        else:
            t.penup()
            t.goto(x+5,y+85)
            t.pendown()

        t.write(an2,font=("微软雅黑",15,"normal"))
        t.setheading(0) 
        t.penup()
        t.goto(x+1,y+65)
        t.pendown()
        t.write(an1,font=("微软雅黑",22,"normal"))
        t.setheading(0) 
        t.penup()
        t.goto(x+35,y+25)
        t.pendown()
        t.write(an1,font=("微软雅黑",35,"normal"))
        t.hideturtle()
        t.hideturtle()

#地主边框
def di(x,y):   
    t.color("#FD7926")
    t.penup()
    t.goto(x+600,y+150)      
    t.pendown() 
    t.begin_fill()
    t.goto(x+625,y+150)
    t.goto(x+650,y+125)
    t.goto(x+650,y+100)
    t.end_fill()        
    t.penup()
    t.goto(x+615,y+130)
    t.pendown()
    t.color("white")
    t.write("地",font=("华文琥珀",12,"normal"))
    t.penup()
    t.goto(x+632,y+113)
    t.pendown()
    t.color("white")
    t.write("主",font=("华文琥珀",12,"normal"))

#通过for循环展示
for k in range(17):
        one_fang_kuai(-400+k*35,-200,nm1[k])

for n in range(17):
        one_fang_kuai(-400+n*35,0,nm2[n])

for m in range(20):
        one_fang_kuai(-450+m*35,250,dizhu[m])


di(-366,210)
    
