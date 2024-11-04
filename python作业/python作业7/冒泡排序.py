def sort(ss):
    for j in range(len(ss)-1):
        for i in range(len(ss)-j-1):
            if(ss[i]>ss[i+1]):
                ss[i],ss[i+1]=ss[i+1],ss[i]
        


ls1=[12,0,10,9,8,-1,21,-6]
print(ls1)
sort(ls1)
