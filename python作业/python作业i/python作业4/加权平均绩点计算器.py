print("绩点加权平均计算器")
#上学期成绩
def get_cj1():
    x=float(input("形式与政策1："))
    z=float(input("军事技能："))
    c=float(input("心理健康教育（第二课堂）："))
    v=float(input("中国近代史纲要："))
    b=float(input("大学英语（上）："))
    n=float(input("大学英语听说（上）："))
    m=float(input("职业发展规划："))
    a=float(input("计算机学科概论："))
    s=float(input("体育（1）："))
    d=float(input("军事理论："))
    f=float(input("高等数学B（上）："))
    g=float(input("心理健康教育："))
    h=float(input("人文素质教育："))
    #上学期必修加权绩点
    pj=float((((x-50)/10)*0.5)+(((v-50)/10)*2.5)+(((b-50)/10)*5)+(((n-50)/10)*2)+(((a-50)/10)*2)+(((s-50)/10)*1)+(((d-50)/10)*2)+(((f-50)/10)*4))
    return pj

#下学期成绩
def get_cj2():
    x=float(input("高等数学B（下）："))
    z=float(input("形式与政策2："))
    c=float(input("思想道德与法治："))
    v=float(input("大学生创业基础："))
    b=float(input("大学物理B（上）："))
    n=float(input("大学英语听说（下）："))
    m=float(input("大学英语（下）："))
    a=float(input("C语言程序设计："))
    d=float(input("体育（乒乓球）："))
    
#计算加权平均绩点
def jd1(pj):
    jd1=float(pj/(19))
    return jd1
             

an="y"
while(an=="y"):
    name=input("请输入你的名字：")
    cj1=get_cj1()
    print("\n")
    cj2=get_cj2()
    print(name,"你的上学期加权平均绩点：%.2f"%jd1(cj1))
    jd1(cj1)   #输入数据
    an=input("play again?(y/n)")
