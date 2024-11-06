a=(int(input("please input a data:")))

sum=0
for j in range(2,a):
    flag=1
    a=j
    for i in range(2,a):#计算余数
        if(a%i==0):#遇到0整除停止
            flag=0
            break

    if(flag==1):
        print("%d是素数,"%a,end='')
        sum=sum+1
    else:
        sum=sum
print("有素数为：",sum)

