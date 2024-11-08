time=0
num=27
print("过了{}小时有{}个细胞".format(time,num))

for i in range(100000):
    time=time+1
    num=(num-1)*2+1
    print("过了{}小时有{}个细胞".format(time,num))
    if(num>=100000):
        break
    
