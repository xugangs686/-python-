time=11
num=26625
print("过了{}天有{}个细胞".format(time,num))

for i in range(11):
    time=time-1
    num=(num-1)/2+1
    print("过了{}天有{}个细胞".format(time,num))
