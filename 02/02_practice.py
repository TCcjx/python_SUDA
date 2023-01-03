'''
BMI=体重/身高的平方(国际单位kg/m2)
小于 18.5 体重偏轻
18.5~23.0 体重正常
23.0~25.0 体重偏重
25.0~30.0 轻度肥胖
大于 30.0 肥胖
'''
weight = float(input('请输入你的体重(kg):'))
high = float(input('请输入你的身高:(m):'))
BMI = weight/(high**2)
print("BMI为 %.1f"%BMI)
if BMI < 18.5:
    print('体重偏轻')
elif BMI > 18.5 and BMI < 23.0:
    print('体重正常')
elif BMI > 23.0 and BMI < 25.0:
    print('轻度肥胖')
elif BMI > 30.0:
    print('体重肥胖')