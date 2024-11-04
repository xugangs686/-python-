#单循环
'''
for i in range(1,10):
    print("%dx9=%d\t"%(i,i*9))

#双重循环
'''
#正
for j in range(9):
    for i in range(1,j+2):
        print("%dx%d=%d\t"%(i,j+1,i*(j+1)),end='')
    print()

print("")
#倒
for j in range(8,-1,-1): #带’-‘可以倒过来
    for i in range(1,j+2):
        print("%dx%d=%d\t"%(i,j+1,i*(j+1)),end='')
    print()
