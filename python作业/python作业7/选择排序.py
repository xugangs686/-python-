def sort(ss):
    for j in range(len(ss)-1):
        for i in range(len(ss)-j-1):
            if(ss[j]>ss[j+i+1]):
                #tmp=ls[j]
                #ls[j]=ls[j+i+1]
                #ls[j+i+1]=tmp
                ss[j],ss[j+i+1]=ss[j+i+1],ss[j]
        print(ss)


ls1=[12,0,10,9,8,-1,21,-6]
print(ls1)
sort(ls1)
