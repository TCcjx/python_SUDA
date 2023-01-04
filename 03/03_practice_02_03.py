'''
计算两日期之差
使用python函数包
'''
import datetime

# import datetime
# birthday="2024-01-03"
# birthday_date=datetime.datetime.strptime(birthday,"%Y-%m-%d")
# curr_datetime=datetime.datetime.now()
# minus_date=curr_datetime-birthday_date
# print(minus_date.days)

'''
计算距离某日期X天是什么日期?
其中X可正可负。
这里以正数为例，负数同理
'''
# 1.获取当前日期
curr_datetime = datetime.datetime.now().strftime('%Y-%m-%d')
curr_datetime = curr_datetime.split('-')
print(curr_datetime)
y = int(curr_datetime[0])
m = int(curr_datetime[1])
d = int(curr_datetime[2])
day_diff = int(input('请输入天数:'))
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,day_diff+1):
    flag = False
    if (y%4==0 and y%100!=0) or y%400==0:
        flag = True
        month_days[1]=29
    else:
        flag = False
        month_days[1]=28
    if d <= month_days[m-1]:
        d += 1
    if d == month_days[m-1]+1:
        m += 1
        d = 1
    if m == 13:
        y += 1
        m = 1
print('%d-%d-%d'%(y,m,d))

