
sum=0
for i in range(10000,100000):
    a=i%10
    b=(i//10)%10
    c=(i//100)%10
    d=(i//1000)%10
    e=(i//10000)%10
    if((a==e)and(b==d)):
        print(i,",",end=(""))
        sum=sum+1
print("回文数共有%d个"%sum)    

