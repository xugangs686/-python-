def an(n):
    an=[]
    for i in range(n):
        b=[1]*(i+1)
        if(i>1):
            prev_b=an[i - 1]
            for j in range(1, i):
                b[j]=prev_b[j-1]+prev_b[j] #prev_这里表示先前的一行
        print(" "*(n-i),b)
        an.append(b)#将b的值带入a中
    return an

n=int(input("请输入行数"))
an=an(n)
