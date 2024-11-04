

def num(x):
    sum=0
    for i in range(2024,x+1):
        if(i%4==0 and i%100!=0 or i%400==0):
            sum=sum+1
            print(i,end='\t')

    print("\n共有{}个".format(sum))

an=(int(input("请输入数字：")))

num(an)
