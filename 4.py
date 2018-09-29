
#_*_ coding:utf8-


'''
#1.数学方面: 五角数
def getpen(n):
    n=n*(3*n-1)/2
    print("%.0f"%(n),end=" ")
s=0
for i in range(1,101):
    getpen(i)
    s=s+1
    if(s%10==0):
        print('')
'''



'''
#2.求一个整数各个数字的和
def sumdigits(n):
    s=0
    while(n%10!=0):
        a=n%10
        b=n//10
        s=s+a
        n=b
    print(s)

a=eval(input("Enter a int:"))
sumdigits(a)

'''



'''
#3.对三个数排序

def displaysort(num1,num2,num3):
    b=[num1,num2,num3]
    b.sort()
    print(b)
    
a,b,c=eval(input("Enter three numbers:"))
displaysort(a,b,c)
'''
from math import *


'''
#4.计算未来投资值
invested=eval(input("The amount inversted:"))
monthly=eval(input("Annual interest rate:"))
print("Annual\tFuture Value")
def funtureinver(invested,monthly,years):
    return invested*pow((1+monthly/100/12),years*12)
for i in range(1,31):
    c=funtureinver(invested,monthly,i)
    print("%d\t%.2f"%(i,c),end="  ")
    print()
'''





'''
#5.显示字符
def printchars(ch1,ch2,number):
    m=0
    a=ord(ch1)
    b=ord(ch2)+1
    for i in range(a,b):
        print(chr(i),end=" ")
        m=m+1
        if(m%number==0):
            print(" ")
a,b=input("Enter start to end ascii:").split(',')
c=eval(input("Enter number:"))
printchars('1','Z',10)
'''


'''
#6.一年的天数

def numberofdays(year):
    if((year%4==0)&(year%100!=0))|(year%400==0):
        print("%d:366"%(i))
    else:
        print("%d:365"%(i))
for i in range(2010,2021):
    numberofdays(i)
'''

'''
#7.几何问题：显示角
def distance(x1,y1,x2,y2):
    print(((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**0.5)
x1,y1=eval(input("Enter x1 and x2 for point1: "))
x2,y2=eval(input("Enter x1 and x2 for point2: "))
distance(x1,y1,x2,y2)
'''



#8.梅森素数
print("p\t2^p-1:")
def s(a):
    c=0
    for j in range(2,int(sqrt(a)+1)):
            if a%j==0:
                c=0
            else:
                c=1
    return c
print("2\t3")
for i in range(1,32):
    c=pow(2,i)-1
    if(s(c)):
        print("%d\t%d"%(i,c))

    


'''
#9.当前时间和日期
from time import *
print(ctime(time()))
'''



'''
#10.游戏：掷骰子

a,b=eval(input("Enter one  and two:"))
if(a+b==2)|(a+b==3)|(a+b==12):
    print("You rolled %d+%d=%d"%(a,b,a+b))
    print("You lose")
elif(a+b==7)|(a+b==11):
    print("You rolled %d+%d=%d"%(a,b,a+b))
    print("You win")
else:
    while(1):
        print("You rolled %d+%d=%d"%(a,b,a+b))
        print("print is %d"%(a+b))
        s=a+b
        a,b=eval(input("Enter one  and two:"))
        if(a+b==7):
            print("You rolled %d+%d=%d"%(a,b,a+b))
            print("You lose")
            break
        elif(a+b==s):
            print("You rolled %d+%d=%d"%(a,b,s))
            print("You win")
            break
        else:
           continue
'''

    

