'''
判断输入的日期是否为合法的日期
●确定输入的年份是否为闰年
●年份是4的倍数但不是100的倍数
 年份是400的倍数
●根据月份确定日期的上限
●1、3、5、7、8、10、12月最多31天
●4、6、9、11月最多30天
●2月
●闰年最多29天
●平年最多28天
'''
date = input('请输入需要合法检验的日期:')
leap = False #判断是否是闰年的标志位
legal = False #日期是否合法的标志位

month1 = (1,3,5,7,8,10,12)
month2 = (4,6,9,11)
year,month,day = (int(x) for x in date.split('-'))
print('%s-%s-%s'%(year,month,day),end=' ')
if month in month1:
    if day>=1 and day<= 31:
        legal = True
elif month in month2:
    if day>=1 and day<=30:
        legal = True
elif month == 2:
    if (year%4==0 and  year%100!=0) or year%400==0: #判断是否是闰年
        leap = True
    if leap == True:
        if day>=1 and day <=29:
            legal = True
    else:
        if day>=1 and day <=28:
            legal = True

if legal == True:
    print('日期合法！')
else:
    print('日期不合法！')