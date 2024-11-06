import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if (n%i==0):
            return 0
    return 1

sum=0
for j in range(2,1001):
    a=is_prime(j)
    if(a==1):
        print(j,",",end='')
        sum=sum+1
print("有素数为：%d个"%sum)
