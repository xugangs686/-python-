print("肥胖计算器")
p="y"      #重复
while(p=="y"):
    w=float(input("请输入体重：(Kg)"))  #float小数
    h=float(input("请输入身高：(m)"))
    bmi=w/(h*h)       #%.2f显示俩位小数
    print("体重：%.2f身高：%.2fBMI：%.2f"%(w,h,bmi))

    if(bmi<18):
        print("细狗，该增重喽！")
    elif(bmi<=24):
        print("刚刚好！")
        print("继续保持！")
    elif(bmi<=28):
        print("再吃下去，你就是国服马超了！")
    else:
        print("？？？这么重！你是国服马超吗？")
    p=input("play again?(y/n)")   
