def sort(ss):
    for j in range(len(ss)-1):
        for i in range(len(ss)-j-1):
            if(ss[j]<ss[j+i+1]):
                ss[j],ss[j+i+1]=ss[j+i+1],ss[j]
        print(ss)


ls=[[12,0,8,9,6,1,21,46],[3,88,-2,90,100],[6,-3,9,12,44,0,50,70,-23,8]]
print(ls[0])
sort(ls[0])
print(ls[1])
sort(ls[1])
print(ls[2])
sort(ls[2])
