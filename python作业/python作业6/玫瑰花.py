sum=0
for i in range(1000,10000):
    a=i%10
    b=(i//10)%10
    c=(i//100)%10
    d=(i//1000)%10
    if(i==a**4+b**4+c**4+d**4):
        print(i,",",end=(""))
        sum=sum+1
print("玫瑰花数共有%d个"%sum)
