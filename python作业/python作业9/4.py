def num(x,y):
    for i in range(x,30):
        if((30-i)%(y*2-1)==0):
            print(i)
        
an=int(input("请输入开始数字："))
p=int(input("最多数的个数"))
num(an,p)
