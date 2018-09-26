#_*_ coding:utf8-

#第一部分
'''
#1.五边形的面积
from math import *
r=float(input("Enter the length from the center to a vertex:")) #r为顶点到中心的距离
s=2*r*sin(pi/5)          #求边长
area=5*s*s/(4*tan(pi/5))
print("The area of the pentagon is %.2f"%(area))
'''

'''
#2.大圆距离
from math import *
x1,y1=eval(input("Enter point 1 (latitude and longitude in degrees:"))
x2,y2=eval(input("Enter point 2 (latitude and longitude in degrees:"))
x1=radians(x1)
x2=radians(x2)
y1=radians(y1)
y2=radians(y2)
d=6371.01*acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print("The distance between the two points is {}".format(d))
'''
'''
#3.五角形的面积
from math import *
s=eval(input("Enter the side:"))
area=(5*s*s)/(4*tan(pi/5))
print("The area of the pentagon is {}".format(area))
'''

'''
#4.一个正多方形的面积

from math import *
n=eval(input("Enter the number of sides:"))
s=eval(input("Enter the side:"))
area=(n*s*s)/(4*tan(pi/n))
print("The area of the pentagon is {}".format(area))
'''
'''
#5.输入ascii码输出字符

a=int(input("Enter an ASCII code:"))
a=chr(a)
print("The character is {} ".format(a))
'''
'''

#6.工资表
name=input("Enter employee's name:")
time=eval(input("Enter number of hours worked in a week:"))#一周工作时间
rate=eval(input("Enter hourly pay rate:")) #每小时的报酬
fed=eval(input("Enter federal tax winthholding rate:"))#联邦预扣税率
sta=eval(input("Enter state tax winthholding rate:")) #州预扣税率
print("Employee Name:{}".format(name))
print("Hours Worked:{}".format(time))
print("Pay Rate:${}".format(rate))
print("Gross Pay:$%.1f"%(time*rate))
print("Deductions:")
print("Federal Withholding(%.1f):$%.1f"%(fed*100,time*rate*fed))
print("State Withholding(%.1f):$%.2f"%(sta*100,time*rate*sta))
print("Total Deduction:$%.2f"%(time*rate*fed+time*rate*sta))
print("Net Pay:$%.2f"%(time*rate-time*rate*fed-time*rate*sta))

'''
'''
#7.反向数字

a=str(input("Enter an integer:"))
b=len(a)
for i in range(b):
    print(a[b-1-i],end='')
print()
'''
#第二部分
'''
#1.解一元二次方程
from math import *
a,b,c=eval(input("Enter a,b,c:"))
s=b*b-4*a*c
#r1=(-b+sqrt(s))/2*a
#r2=(-b-sqrt(s))/2*a
if s>0:
    r1=(-b+sqrt(s))/2*a
    r2=(-b-sqrt(s))/2*a
    print("The roots are %.6f and %.6f "%(r1,r2))
elif s==0:
    r1=(-b+sqrt(s))/2*a
    print("The roots is {}".format(r1))
else:
    print("The equation has no real roots")
'''

'''
#2.学习加法
import random
a=random.randint(0,100)
b=random.randint(0,100)
print(a,b)
n=eval(input("Enter sum:"))
if(n==(a+b)):
    print(True)
else:
    print(False)

'''

'''
#3.找未来数据
n=int(input("Enter today's day(0-6):"))
m=int(input("Enter the number of days elapsed since today:"))
a=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if((n+m)%7==0):
    s=a[0]
elif((n+m)%7==1):
    s=a[1]
elif((n+m)%7==2):
    s=a[2]
elif((n+m)%7==3):
    s=a[3]
elif((n+m)%7==4):
    s=a[4]
elif((n+m)%7==5):
    s=a[5]
else:
    s=a[6]
b=a[n]
print("Today is {} and the future day is {}".format(b,s))
'''

'''
#4.对三个整数排序
a,b,c=eval(input("Enter a,b,c:"))
d=[a,b,c]
d.sort()
print(d)
'''
'''
#5.比较价钱

a1,b1=eval(input("Enter weight and price for package:"))
a2,b2=eval(input("Enter weight and price for package:"))
if(a1*b1>a2*b2):
    print("Package 2 has the better price")
else:
    print("Package 1 has the better price")

'''


#6.找出一个月的天数

a,b=eval(input("Enter month and year:"))
if(a==2):
    if((b%4==0&b%100!=0)|b%400==0):
        m=29
    else:
        m=28
else:
    if(a==4)|(a==6)|(a==9)|(a==11):
        m=30
    else:
        m=31

print("The {}year and {}month have {}day".format(b,a,m))

'''
#7.头或尾
import random
b=eval(input("Enter y/n(1/0)"))
a=random.randint(0,1)
if(b!=a):
    print(False)
else:
    print(True)

'''
'''
#8.剪刀、石头、布
import random
a=eval(input("scissor(0),paper(2),rock(1)"))
b=random.randint(0,2)
c=['scissor','rock','paper']
f=c[b]
g=c[a]
if((a==0&b==2)|(a==1&b==0|a==2&b==1)):
    print("The computer is {}.you are {}.you won".format(f,g))
elif(a==b):
    print("The computer is {}.you are {} too.It is a draw".format(f,g))
else:
    print("The computer is {}.you are {}.you lost".format(f,g))


'''
'''
#10.选出一张牌

from random import *
p=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
m=['meihua','hongtao','fangkuai','heitao']
a=choice(p)
b=choice(m)
print("The card you picked is the {} of {}".format(a,b))

'''
from random import *
from math import *

'''
#11.回文数
n=str(input("Enter a three-digit interger:"))
if(n[0]==n[2]):
    print("{} is a palindrome".format(n))
else:
    print("{} is not a palindrome".format(n))

'''
'''
#12.计算三角形周长
a,b,c=eval(input("Enter three edges:"))
if((a+b<=c)|(a+c<=b)|(b+c<=a)):
    print("wrong")
else:
    sum=a+b+c
    print("The perimeter is {}".format(sum))
'''
