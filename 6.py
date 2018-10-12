#_*_coding:utf8-
'''
#1.检测SSN,按照格式ddd-dd-dddd输入,其中d是数字,看格式是否正确
def jiance(n):
   # print(n)
    d=['0','1','2','3','4','5','6','7','8','9']
    m=0
    for i in n:
        if i in d:
            m=m+0
        else:
            m=m+1
    return m

a=list(input("请输入格式ddd-dd-dddd(数字):"))
if(len(a)==11):
    if((a[3]=="-")&(a[6]=="-")):
        m=jiance(a[0:3])
        n=jiance(a[4:6])
        k=jiance(a[7:11])
        if(m+n+k==0):
            print("Valid SSN")
        else:
            print("Invalid SSN")
    else:
        print("Invalid SSN")
else:
    print("Invalid SSN")


'''



'''
#1.对成绩分级

a=input("输入以空格隔开的数组:>>")
b=[int(n) for n in a.split()]
best=max(b)
t=0
for i in b:
    if(i>=best-10):
        print('Student {} score is {} and grade is A'.format(t,i))
    elif(i>=best-20):
        print('Student {} score is {} and grade is B'.format(t,i))
    elif(i>=best-30):
        print('Student {} score is {} and grade is C'.format(t,i))
    elif(i>=best-40):
        print("Student {} score is {} and grade is D".format(t,i))
    else:
        print("Student {} score is {} and grade is F".format(t,i))
    t=t+1
'''




'''
#2.检测子串

a=input("输入第一个字符串:")
b=input("输入第二个字符串:")
if a in b:
    print("True")
else:
    print("False")
'''



'''
#2.逆序读取的数字
a=input("输入以空格隔开的数组:>>")
b=[int(n) for n in a.split()]
b.sort(reverse=True)
print(b)
'''




'''
#3.检测密码

def jiance(a):
    n=list(a)
    if(len(n)>=8):     #密码长度大于8
        b=['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        c=['0','1','2','3','4','5','6','7','8','9']
        s=0
        m=0
        for i in n:
            if(i in b):
                s=s+1
        if(s>=8):            #必须是字母和数字
            for i in n:
                if(i in c):
                    m=m+1 
            if(m>=2):         #数字大于2
                print("valid password")
            else:
                print("invalid password")
        else:
            print("invalid password")
    else:
        print("invalid password")

a=input("输入一串密码，看是否合法:")
jiance(a)
'''

'''
#3.统计数字个数

def tongji(b):
    for i in range(1,101):
        s=0
        for j in b:
            if(j==i):
                s=s+1

        if(s>0):
            print("{} occurs {} times.".format(i,s))


a=input("Enter integers between 1 and 100 :")
b=[int(i) for i in a.split()]
tongji(b)
'''


'''
#4.决定多少个分数是大于等于平均分数，多少个低于平均分数，输入时用空格
def fenxi(b):
    c=sum(b)/len(b)     #求平均数
    s=0
    n=0
    for i in b:
        if(i>=c):
            s=s+1
        else:
            n=n+1
    print("大于平均分数的有{}个，小于平均分数的有{}个.".format(s,n))

a=input("输入一行用空格分隔的数:")
b=[int(i) for i in a.split()]
fenxi(b)
'''

'''
#4.统计字符串中字母的个数
def countletters(s):
    b=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    n=0
    for i in s:
        if(i in b):
            n=n+1
    print("string have {}.".format(n))


a=input("Enter  string:")
countletters(a)
'''

'''
#5.统计单个数字
from random import *
def tongji():
    s=[]
    for j in range(1000):
        a=randint(0,9)
        s.append(a)
       #print(s)
    for i in range(0,10):
        m=0
        for j in s:
            if(j==i):
                m=m+1
        if(m>0):
            print("{} occurs {} times.".format(i,m))

tongji()
'''


'''
#6.找出最小元素的下标
def indexof(lst):
    a=min(lst)
    for i in range(len(lst)):
        if(lst[i]==a):
            print("最小整数的下标为{}.".format(i))
a=input("输入一个数字列表:")
lst=[int(i) for i in a.split()]
indexof(lst)
'''




'''
#5.手机键盘(大写字母返回对应的数字)
def getnumber(a):
    a=a.lower()
    for i in range(len(a)):
        if((a[i]=='a')|(a[i]=='b')|(a[i]=='c')):
            a=a.replace(a[i],'2')
        elif((a[i]=='d')|(a[i]=='e')|(a[i]=='f')):
            a=a.replace(a[i],'3')
        elif((a[i]=='g')|(a[i]=='h')|(a[i]=='i')):
            a=a.replace(a[i],'4')
        elif((a[i]=='j')|(a[i]=='k')|(a[i]=='l')):
            a=a.replace(a[i],'5')
        elif((a[i]=='m')|(a[i]=='n')|(a[i]=='o')):
            a=a.replace(a[i],'6')
        elif((a[i]=='p')|(a[i]=='q')|(a[i]=='r')|(a[i]=='s')):
            a=a.replace(a[i],'7')
        elif((a[i]=='t')|(a[i]=='u')|(a[i]=='v')):
            a=a.replace(a[i],'8')
        elif((a[i]=='w')|(a[i]=='x')|(a[i]=='y')|(a[i]=='z')):
            a=a.replace(a[i],'9')

    print(a)
a=input("Enter a string:")
getnumber(a)
'''

'''
#6.反向字符串
def rever(s):
    n=len(s)-1
    while(n>=0):
        print(s[n],end='')
        n=n-1
    print()
a=input("输入一个字符串:")
rever(a)
'''



#7.信用卡号合法性
def check(a):
    sum=0
    n=0
    for i in range(len(a)):
        s=int(a[i])*2
        if s>=10:
            s1=s%10
            s2=s//10
            s3=s1+s2
            sum+=s3
        else:
            sum+=s
        if i % 2 !=0:
            n+=int(a[i])
    if((sum+n)%10==0):
        print("合法")
    else:
        print("不合法")            
a=input("输入卡号:")
a=list(a)
check(a)

'''
#7.随机数字选择器(输入一个列表,打乱顺序后输出)
import random
def shuffles(lst):
    lst_1=[]
    for i in range(len(lst)):
        n=random.randint(0,len(lst)-1)
        a=lst.pop(n)
        lst_1.append(a)
    print("乱序为:{}".format(lst_1))
a=input("输入一个列表(空格隔开):")
b=[int(i) for i in a.split()]
shuffles(b)
'''


'''
#8.商业：检测ISBN-13

def check(a):
    a_1=list(a)
    sum=0
    for i in range(len(a_1)):
        if(i%2==0):
            sum=sum+int(a_1[i])*3
        else:
            sum=sum+int(a_1[i])
    sum_1=10-sum%10
    if(sum_1==10):
        sum_1=0
    else:
        sum_1=sum_1
    a_1.append(sum_1)     
    a=[str(i) for i in a_1]   #将列表转换为字符串
    a_1=''.join(a)              #字符串无缝连接
    print("The ISBN-13 number is {}".format(a_1))
a=input("Enter the first 12 digits of an ISBN-13 as a string:") 
check(a)
'''


'''
#8.消除重复

def eliminate(lst):
    lst1=[]
    for i in lst:
        if i not in lst1:
            lst1.append(i)
    print("The distinct number are:{}".format(lst1))
a=input("Enter ten numbers:")
b=[int(n) for n in a.split()]
eliminate(b)
'''


'''
#9.列表是否是升序(有序吗？)
def issorted(lst):
    a=sorted(lst)
    if(a==lst):
        print("The list is already sorted")
    else:
        print("The list is not sorted")


a=input("Enter list:")
b=[int(n) for n in a.split()]
issorted(b)
'''

'''
#10.冒泡排序
def maopao(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]<a[j]):
                a[i],a[j]=a[j],a[i]
    print(a)
a=input("输入10个数(空格隔开:)")
a=[int(n) for n in a.split()]
maopao(a)
'''

'''
#11.优惠券收集问题
import random
def youhuiquan():
    lis=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    lis1=['红桃','黑桃','梅花','方块']
    res=[]
    coun=0
    while(len(res)!=4):
        coun+=1
        random1=random.randint(0,13)
        random2=random.randint(0,3)
        if(lis1[random2] not in res):
            print('获得 {}{}'.format(lis1[random2],lis[random1]))
            res.append(lis1[random2])
        print('Pick:'+str(coun))
youhuiquan()
'''



'''
#12.是否是四个连续的相同的数
def isconsecut(s):
    n=list(str(s))
    if(len(n)>=4):
        for i in range(len(n)-3):
            if(n[i]==n[i+1] and n[i]==n[i+2] and n[i]==n[i+3]):
                print('True')
                break
        else:
            print('False')
a=input("输入一串数字(空格隔开):")
a=a.split()
isconsecut(a)
'''


