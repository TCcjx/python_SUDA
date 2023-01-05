'''
进制转换
'''

'''
****1.python内置函数实现****
'''
# print(bin(19))
# print(bin(-19))
# print(int('10011',2))
# print(int('-0b10011',2))
'''
****2.任意进制转十进制****
'''
# n = int(input('请输入你需要转换的数字:'))
# p = int(input('请输入你需要转换的进制数:'))
# Flag = True#默认为正数
# if n < 0:
#     Flag = False
#     n = abs(n)
# y = 0
# product = 1
# while n!=0:
#     y += (n%10)*product
#     n = n//10
#     product = product*p
# if Flag:
#     print('转换结果为%d'%y)
# else:
#     print('转换结果为-%d'%y)
'''
****3.十进制转换为任意进制****
除基倒取余数法
'''
# L = []
# n = int(input('请输入你需要转换的数字:'))
# p = int(input('请输入你需要转换的进制数:'))
# Flag = True #默认为正数
# if n<0:
#     Flag =False
#     n = abs(n)
# count = 1
# L.append(n%p)
# n=n//p
# while n!=0:
#     count += 1
#     L.append(n%p)
#     n=n//p
# if not Flag:
#     print('-',end='')
# for i in range(0,count):
#     print(L[count-1-i],end='')

'''
思考题
●编写函数my_hex(n),将十进制整数n转换成十六进制数
●编写函数hex2bin(n)，将十六进制数n转换成二进制数
●参数n是一个数值字符串
'''


# 将十进制转换为十六进制
def decimalToHex(decValue):
    hex = ""
    decValue = int(decValue)
    while decValue != 0:
        hexValue = decValue % 16  # 求余数
        hex = toHexChar(hexValue) + hex
        decValue = decValue // 16  # 求商
    if decValue < 0:
        return '-' + hex
    return hex

# 转换字符型
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))  #chr(num) num:an unicode integer return str
                                         #ord(char) char: an unicode character return unicode integer
    else:
        return chr(hexValue - 10 + ord('A'))
def my_hex(n):
    print(decimalToHex(n))
chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def hex2Dec(n):
    n = n[::-1]
    y = 0
    p = 1
    product = 16
    for i in n:
        x = chars.index(i)
        y += x*p
        p = p*product
    return y
def Dec2BIn(n):
    L = []
    p = 2
    L.append(n%2)
    n = n//p
    count = 1
    while n!=0:
        count += 1
        L.append(n % 2)
        n = n // p
    for i in range(count):
        print(L[count-1-i],end='')

def hex2bin(n):
    Dec2BIn(hex2Dec(n))


if __name__ == '__main__':
    hex2bin('A1')




