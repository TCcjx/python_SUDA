'''
二分查找
'''

def binary_search(L,t,low,high):
    while low <= high:
        mid = (low+high)//2
        if L[mid] == t:
            return mid
        elif L[mid] < t:
            low = mid + 1
        elif L[mid] > t:
            high = mid -1
    return False
L = [2,3,5,7,8,9,10,14,16,23,45]
t = int(input('请输入你要查找的数:'))
x = binary_search(L,t,0,len(L)-1)
if x==False:
    print('没有查找到这个数字。')
elif isinstance(x,int):
    print('查找结果为:该数字下标为%d'%x)

'''
已知n是一一个完全平方数，用二分查找计算n的平方根
'''
n =2
l = 0
r = n
ans = 1e-6
while True:
    mid = (l+r)/2 #不能用//进行整除
    if abs(mid**2-n) < ans:
        print('%.3f'%mid)
        break
    else:
        if mid**2 < n:
            l = mid
        elif mid**2 > n:
            r = mid
