'''
牛顿迭代法就平方根
'''
def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x / y) / 2
    return y
print('%.3f'%sqrt(10))
