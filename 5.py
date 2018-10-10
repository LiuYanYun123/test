# _*_ coding:utf8-

'''
#1.矩形的面积和周长

class juxing:
    def __init__(self,kuan,gao):
        self.width=kuan
        self.height=gao
    def getarea(self):
        s=self.width*self.height
        print("kuan {}, gao {}\nmianji:{}".format(self.width,self.height,s))
    def getperimeter(self):
        n=2*self.width+2*self.height
        print("zhouchang:{}\n".format(n))

juxing(4,40).getarea()
juxing(4,40).getperimeter()

juxing(3.5,35.7).getarea()
juxing(3.5,35.7).getperimeter()

'''
'''
#2.利息
class account:
    def __init__(self,id=0,balance=100,annual=0):
        self.__id=int(id)
        self.__balance=float(balance)
        self.__annual=float(annual)
        print(self.__id)

    def withdraw(self,money):  #取出的金额
        if (money<self.__balance):
            self.w=self.__balance-money
            print("余额:{}".format(self.w))
        else:
            print("没有那么多钱")
    def deposit(self,ins):  #存入金额
        self.d=ins+self.__balance
        print("共有{}".format(self.d))
    def getrate(self):   #月利率
        self.y=self.__annual/100/12
        print(self.y)
    def get(self):  #月利息额
        self.m=self.__balance*(self.__annual/100/12)
        print(self.m)

m=account(1122,20000,4.5)
m.withdraw(2500)
m.deposit(3000)
m.get()
m.getrate()
'''
'''
#3.几何：正n边形
from math import *
class regular:
    #输入正多边形的边数，长度，x轴的坐标，y轴的坐标，求出它的周长和面积
    def __init__(self,n=3,side=1,x=0,y=0):
        self.n=int(n)
        self.side=float(side)
        self.x=float(x)
        self.y=float(y)
    def getper(self):
        print("周长为：%d"%(self.n*self.side))
    def getarea(self):
        area=(self.n*self.side*self.side)/(4*tan(pi/self.n))
        print("面积为：%.2f"%(area))
regular().getper()
regular().getarea()
regular(6,4).getper()
regular(6,4).getarea()
regular(10,4,5.6,7.8).getper()
regular(10,4,5.6,7.8).getarea()
'''
'''
#4.fan(风扇)
class fan:
    def __init__(self,speed=1,on=False,radius=5,color='blue'):
        self.speed=int(speed)
        self.on=bool(on)
        self.radius=float(radius)
        self.color=str(color)
        print("speed is {},radius is {},color is {} and on is {}.".format(self.speed,self.radius,self.color,self.on))
slow=1
medium=2
fast=3
fan(fast,True,10,'yellow')
fan(medium,False,5,'blue')
'''
'''
#5.2x2线性方程式
#输入a,b,c,d,e,f,根据公式求出x,y两个解
class linear:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f

    def issolvable(self):
        self.o=(self.__a*self.__d)-(self.__b*self.__c)
        if(self.o!=0):
            return True
        else:
            print("方程无解")
    def getx(self):
        self.x=((self.__e*self.__d)-(self.__b*self.__f))/self.o
        print("x={}".format(self.x))
    def gety(self):
        self.y=((self.__a*self.__f)-(self.__e*self.__c))/self.o
        print("y={}".format(self.y))
a,b,c,d,e,f=eval(input(">>"))
k=linear(a,b,c,d,e,f)
if(k.issolvable()==True):
    k.getx()
    k.gety()
'''

#6.几何：交叉线
#kx+b+y=0
class jiaocha:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
        self.__x3=x3
        self.__y3=y3
        self.__x4=x4
        self.__y4=y4
    def result(self):
        k1=(self.__y2-self.__y1)/(self.__x2-self.__x1)*1.0
        b1=self.__y1*1.0-self.__x1*k1*1.0
        if(self.__x4-self.__x3)==0:
            k2=None
            b2=0
        else:
            k2=(self.__y4-self.__y3)*1.0/(self.__x4-self.__x3)
            b2=self.__y3*1.0-self.__x3*k2*1.0
        if k2==None:
            x=self.__x3
        else:
            x=(b2-b1)*1.0/(k1-k2)
        y=k1*x*1.0+b1*1.0
        print(x,y)

jiaocha(2,2,0,0,0,2,2,0).result()
        

            
    
