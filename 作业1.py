'''
#1.摄氏温度转换为华式温度
c=float(input("Enter a degree in Celsius:"))
f=(9/5)*c+32
print('{} Celsius is {} Fathrenheit'.format(c,f))
'''

'''
#2.园柱体的体积
r,h=eval(input("Enter the radius and length of a cylinder:"))
area=r*r*3.1415
volume=area*h
print("The area is %.4f,the volume %.1f"%(area,volume))
'''


'''
#3.英尺数转换为米数
a=eval(input("Enter a value for feet："))
print(a*0.305)
'''


'''
#4.科学：计算能量
w,a,b=eval(input("Enter the amount of water,temperature and temperature:"))
s=float(w*(b-a)*4184)
print("The energy needed is :%.1f"%(s))
'''

'''
#5.计算利息
c,a=eval(input("Enter balance and interest rate："))
s=c*(a/1200.0)
print("The interest is:%.5f"%(s))
'''
'''
#6.加速度
v,v0,t=eval(input("Enter v1,v0,and t:"))
a=float((v0-v)/t)
print("The avarage acceleration is%.4f"%(a))
'''
'''
#7.复利值
c=eval(input("Enter the monthly saving amount:"))
b=1+0.00417
s=0
for i in range(6):
    s=float((c+s)*b)
print("After the six month,the account value is %.2f"%(s))
'''

#8.对一个整数中的各位数字求和
n=eval(input("Enter a number between 0 and 1000:"))
a=n%10
b=(n//10)%10
c=n//100
print("The sum of the digits is %d"%(a+b+c))

