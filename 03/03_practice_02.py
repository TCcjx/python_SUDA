'''
二分法就平方根
'''
import random
x = random.randint(0,10000)
first = 0
end = x
count = 0
a = 1e-10
while True:
    count += 1
    mid = (first+end)/2
    if abs((mid**2)-x)<a:
        break
    else:
        if abs(mid**2)>x:
            end = (first+end)/2
        elif abs(mid**2) <x:
            first = (first+end)/2
print('%d的平方根是%.3f,求解%d次'%(x,(first+end)/2,count))