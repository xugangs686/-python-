import random as r

#'\u2665'   #红心，'\u2660'   #黑桃，'\u2666'   #方块，'\u2663'   #梅花

pk=['红心A','红心2','红心3','红心4','红心5','红心6','红心7','红心8', '红心9','红心10','红心J','红心Q','红心K',
    '黑桃A','黑桃2','黑桃3','黑桃4','黑桃5','黑桃6','黑桃7','黑桃8', '黑桃9','黑桃10','黑桃J', '黑桃Q','黑桃K',
    '方块A','方块2','方块3','方块4','方块5','方块6','方块7','方块8', '方块9','方块10','方块J','方块Q','方块K',
    '梅花A','梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8', '梅花9','梅花10','梅花J','梅花Q','梅花K',
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
    

print("农民1的手牌:\n",nm1,"\n")
print("农民2的手牌:\n",nm2,"\n")
print("地主的手牌:\n",dizhu,"\n")

print(pk)

