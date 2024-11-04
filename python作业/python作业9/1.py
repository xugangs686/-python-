day=10
num=1
print("第{}天的桃子数为{}个".format(day,num))

for i in range(9):
    day=day-1
    num=2*(num+1)
    print("第{}天的桃子数为{}个".format(day,num))
