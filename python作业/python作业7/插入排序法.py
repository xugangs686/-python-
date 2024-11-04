def sort(ss):
    for i in range(1,len(ss)):
        key=ss[i]
        j=i-1
        while j>=0 and ss[j]>key :
            ss[j+1]=ss[j]
            j-=1
        ss[j+1]=key  
    print(ss)


ls1=[12,0,10,9,8,-1,21,-6]
print(ls1)
sort(ls1)
