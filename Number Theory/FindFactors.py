from math import *
num=500
factors=[]
for i in range(2,int(sqrt(num))+1):
    while(num%i==0):
        factors.append(num//i)
        num=num//i
    print(num,i,end='');print(num//(num//i))
    while(num%(num//i)==0):
        factors.append(num//(num//i))
        num=num//(num//i)
print(factors)