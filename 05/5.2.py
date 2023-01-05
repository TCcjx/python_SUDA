'''
证明哥德巴赫猜想
***************
任一大于2的偶数都可写成2个质数之和
a+b版本:任一-充分大的偶数都可以表示为两个
整数之和，其中一个整数的质因子不超过a，另
一个整数的质因子不超过b
如果a和b都是1，那么这两个整数显然都是质数,
所以哥德巴赫猜想也可以认为就是证明1+1
1966年，我国数学家陈景润证明了1+2
'''
'''
●函数is_ prime(n)
    参数n是一个正整数
    如果n是质数，返回True,否则返回False
●函数goldbach(n)
    参数n是一个正整数
    如果n不是大于2的偶数，输出相关提示信息
    如果n可以写成2个质数p和q的和，输出
    n=p+q，否则输出相关提示信息
'''
import math
def is_prime(n): # 判断是否是质数
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i ==0:
                return False
    return True

def gold_batch(n):
    if n<2 or n%2==1:
        print('n不是一个大于2的偶数')
        return
    for p in range(2,n):
        if is_prime(p) and is_prime(n-p):
            print(n,'=',p,'+',n-p)
            return
    print('哥德巴赫猜想可能有问题！')
if __name__ == '__main__':
    x = int(input('请输入你想要验证哥德巴赫猜想的整数(请输入大于2的偶数):'))
    gold_batch(x)

'''
***思考题***
编写函数fast_ _goldbach来验证哥德巴赫猜想,
该函数利用sympy包中的isprime函数来进行质
数的判定
使用goldbach和fast_ goldbach来验证
1234567890是否满足哥德巴赫猜想，比较两者
的结果和运行时间
'''

# import sympy
# print(sympy.isprime(5))