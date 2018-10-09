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
        self.w=self.__balance-money

    def deposit(self,ins):  #存入金额
        self.d=ins+self.w
        print(self.d)
    def getrate(self):   #月利率
        self.y=self.__annual/100/12
        print(self.y)
    def get(self):  #月利息额
        self.m=self.d*(self.__annual/100/12)
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
    def __init__(self,n=3,side=1,x=0,y=0):
        self.n=int(n)
        self.side=float(side)
        self.x=float(x)
        self.y=float(y)
    def getper(self):
        print("%d"%(self.n*self.side))
    def getarea(self):
        area=(self.n*self.side*self.side)/(4*tan(pi/self.n))
        print("%.2f"%(area))
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

#5.2x2线性方程式

class linear:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f

    def issolvable(self):
        self.o=(self.a*self.d)-(self.b*self.c)
        if(self.o!=0):
            return True
        else:
            print("方程无解")
    def getx(self):
        self.x=((self.e*self.d)-(self.b*self.f))/self.o
        print("x={}".format(self.x))
    def gety(self):
        self.y=((self.a*self.f)-(self.e*self.c))/self.o
        print("y={}".format(self.y))
a,b,c,d,e,f=eval(input(">>"))
k=linear(a,b,c,d,e,f)
if(k.issolvable()==True):
    k.getx()
    k.gety()
