"""
找零问题
100美分，买了34美分的商品
四种硬币进行找零
分别是25、10、5、1美分
"""
money = 100-34

one = money//25
r_money = money%25

two = r_money//10
r_money = r_money%10

three = r_money//5
r_money = r_money%5

four = r_money//1

print(f'找零最优方案为{one}个25美分面值，{two}个10美分面值,{three}个5美分面值,{1}个1美分面值\n')

'''
某奶茶店促销
●
奶茶10元一杯;
●
每买3杯送1杯或每买5杯送2杯;
●小强带了N元钱(N>=0) ;
请问小强最多可以买多少杯? 
'''
N = int(input('请输入你带了多少钱：'))
num = 0
num += (N//50)*7
N = N%50 #贪心原则计算可以进行多少个买5送2
num += (N//30)*4
N = N%30 #贪心原则计算可以进行多少个买3送2
num += N//10
N = N%10 #剩余多少个可以单独买的
print(num)
