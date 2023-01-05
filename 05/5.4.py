'''
计算数学圆周率π
'''
#1.牛顿奈布尼茨交错级数法
# 公式等于 π/4 = ∑（-1）**n /(2n +1)
# PI = 3.141592654
# pi=0
# tm=1
# for i in range(0, 10000000) : #计算项数越多，误差越小，越接近
#     pi += tm/(2*i+1)
#     tm = -tm
# pi*=4
# print("pi=%.7f\t误差率(x10000)=%.5f" % (pi,abs(pi - PI) / PI * 10000))

# 2.蒙特卡罗法
import random
PI = 3.141592654
def gen_pi():
    count, max_C = 0,10000000
    for i in range(0,max_C):
        x, y = random.random( ),random.random( )
        if x*x+y*y<=1:
            count += 1
    return(count / max_C * 4)

if __name__ == '__main__':

    sum_dif,k=0,20
    for i in range(k):
        pi = gen_pi()
        dif=abs(pi-PI)/PI*10000
        sum_dif += dif
        print( "%d\tpi=%.7f\t误差率(x10000)=%.3f" % (i+1, pi, abs(pi - PI) / PI * 10000))
    print("平均误差率(x10000)=%.3f" % (sum_dif / k))
