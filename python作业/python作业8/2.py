import random as r
import turtle as t
#'\u2665'   #红心，'\u2660'   #黑桃，'\u2666'   #方块，'\u2663'   #梅花

pk=['\u2665A','\u26652','\u26653','\u26654','\u26655','\u26656','\u26657','\u26658', '\u26659','\u266510','\u2665J','\u2665Q','\u2665K',
    '\u2660A','\u26602','\u26603','\u26604','\u26605','\u26606','\u26607','\u26608', '\u26609','\u266010','\u2660J', '\u2660Q','\u2660K',
    '\u2666A','\u26662','\u26663','\u26664','\u26665','\u26666','\u26667','\u26668', '\u26669','\u266610','\u2666J','\u2666Q','\u2666K',
    '\u2663A','\u26632','\u26633','\u26634','\u26635','\u26636','\u26637','\u26638', '\u26639','\u266310','\u2663J','\u2663Q','\u2663K',
    '小王','大王']

dizhu=[]
nm1=[]
nm2=[]

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
'''
print("农民1的手牌:\n",nm1,"\n")
print("农民2的手牌:\n",nm2,"\n")
print("地主的手牌:\n",dizhu,"\n")
'''
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

    an2=an[1:]
    an1=an[0:1]

    if(an2=='10'):
        t.penup()
        t.goto(x,y+85)
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
    t.hideturtle()

    
for k in range(17):
        one_fang_kuai(-400+k*35,-200,nm1[k])

for n in range(17):
        one_fang_kuai(-400+n*35,0,nm2[n])

for m in range(20):
        one_fang_kuai(-450+m*35,250,dizhu[m])
