#_*_coding:utf8-
'''
#1.统计正数和负数的个数并计算这些数的平均值
s=0
j=0
o=0
while(1):
    a=int(input("Enter an integer,the input ends if it is 0:"))
    if((a>0)|(a<0)):
        s=s+a
        if(a>0):
            j=j+1
        else:
            o=o+1
    if(a==0):
        print("正数：%d,负数：%d,平均值：%.2f"%(j,o,1.0*s/(j+o)))
        break

'''
'''
#2.计算未来学费
s=10000
for i in range(10):
    s=s+s*0.05
print(s)
n=s
for i in range(4):
    n=n+n*0.05
print(n)

'''
'''
#4.找出同时被5和6整除的数
a=0
for i in range(100,1001):
    if((i%5==0)&(i%6==0)):
        print(i,end=" ")
        a=a+1
        if(a%10==0):
            print(" ")
'''
#4.比较不同利率的贷款
'''
#5.找出最大的n和最小的n
n=1
while(n<12000):
    if(n*n>12000):
        print(n)
        break
    n=n+1
s=1
while(s<12000):
    if(s*s*s>12000):
        print(s-1)
        break
    s=s+1

'''
'''
#7.演示消除错误
n=0
for i in range(1,50001):
    n=n+1/i
print(n)
s=50000
m=0
while(s>0):
    m=m+1/s
    s=s-1
print(m)

'''
'''
#8.数列求和
a=1
n=0
for b in range(3,100,2):
    n=n+a/b
    a=b
print("%.2f"%(n))
'''
'''
#9.计算pai
n=0
for i in range(1,100000):
    n=n+pow((-1),i+1)/(2*i-1)
    if(i%10000==0):
        print(4*n)

'''
'''
#10.完全数
for i in range(1,10001):
    n=0
    for j in range(1,int(i/2+1)):
        if i%j==0:
            n=n+j
    if(n==i):
        print(n)

'''
'''
#11.数学问题：组合
n=0
for i in range(1,8):
    for j in range(i,8):
        if(i!=j):
            print(i,j)
            n=n+1
print(n)
'''



