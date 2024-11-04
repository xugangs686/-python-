def m():
    an=input("请输入明文：")
    for i in an:
        a=(ord(i))
        if(a==88 or a==89 or a==90 or a==120 or a==121 or a==122):
            a=a-26
        elif(a==55 or a==56 or a==57):
            a=a-10
        print(chr(a+3),end='')
        
def n():
    an=input("请输入密文：")
    for i in an:
        a=(ord(i))
        if(a==65 or a==66 or a==67 or a==97 or a==98 or a==99):
            a=a+26
        elif(a==48 or a==49 or a==50):
            a=a+10
        print(chr(a-3),end='')

p=1
while(p!=0):
    #选择
    if(p==1):
        print("请选择：2-解密 3-加密")
        an=input()
        if(an=="2"):
            m()
        elif(an=="3"):
            n()
        else:
            p=1
        print("")

