'''
●确定某起始日期，并已知该起始日期是星期几
●计算某天距离该起始日期的天数
●计算该总天数除以7的余数
●结合该余数与某起始日期是星期几的两方面条件最
终计算出某天是星期几的结果
'''
# 方法1:使用内置函数
'''
from datetime import datetime
#利用num_to_string函数返回中文“星期几”
def num_to_string(num):
    numbers={
        0:"星期日",
        1:"星期一",
        2:"星期二",
        3:"星期三",
        4:"星期四",
        5:"星期五",
        6:"星期六"
        }
    return numbers.get(num,None)
#输入指定的日期（年 月 日 ）
y=int(input("请输入年份(>=1),否则为1:"))
m=int(input("请输入月份(1~12),否则<1为1、>12为12："))
d=int(input("请输入日期(1~31),否则<1为1、>ndays(y,m)为ndays(y,m)："))
#调用内置函数datetime来获取指定日期是星期几
n = datetime(y,m,d).weekday()+1
#获取n的值，用int来提取n的整型值
print("{0} 年 {1} 月 {2} 日是 {3}".format(y,m,d,num_to_string(n)))
'''
#方法2:使用循环结构实现
def num_to_string(num):
    numbers ={
        0: "星期日",
        1: "星期一",
        2: "星期二",
        3: "星期三",
        4: "星期四",
        5: "星期五",
        6: "星期六"
    }
    return numbers.get(num,None)
y = int(input("请输入年："))
m = int(input('请输入月：'))
d = int(input('请输入日：'))
monthDay1=[31,28,31,30,31,30,31,31,30,31,30,31]
days = 0
for i in range(1,y):
    if (y%4==0 and y%100!=0) or y%400==0:
        days += 366
    else:
        days +=365
for j in range(0,m-1):
    if ((y%4==0 and y%100!=0) or y%400!=0) and j==1:
        days += 29
    else:
        days +=monthDay1[j]
days += d
date = days%7
print('%s-%s-%s是%s'%(y,m,d,num_to_string((date))))


