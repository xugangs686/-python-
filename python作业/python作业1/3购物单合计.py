print("***神秘商店的收银系统***")
print("欢迎光临")
print("                        ")
import datetime
a=datetime.datetime.now()
print(a)
while(1):
    print("\请输入品名:")
    p1=input()
    print("\请输入数量:")
    s=input()
    s=int(s)
    print("\请输入单价:")
    d=input()
    d=float(d)
    xj=s*d
    print("品名1为:",p1,"数量：",s,"单价：",d,"小计:",xj)
    print("========================")
    print("\请输入品名:")
    p2=input()
    print("\请输入数量:")
    s=input()
    s=int(s)
    print("\请输入单价:")
    d=input()
    d=float(d)
    xj2=s*d
    print("品名2为:",p2,"数量：",s,"单价：",d,"小计:",xj2)
    print("========================")
    hj=xj+xj2
    print("品名1:",p1,"品名2为:",p2,"合计",hj)
    print("欢迎下次光临") 
    print("========================")











    
    
