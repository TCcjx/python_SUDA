'''
****python异常处理****
try:
    <可能出现异常的语句块>
except <异常类名字name1>：
    <异常处理语句块1>  #如果在try部份引发了'name1'异常，执行这部分语句块
except <异常类名字name2> as e1：
    <异常处理语句块2>  #如果在try部份引发了'name2'异常，执行这部分语句块
except < (异常类名字name3, 异常类名字name4, …)> as e2:
    <异常处理语句块3>  #如果引发了'name3'、'name4'、…中任何一个异常，执行该语句块
…
except:
    <异常处理语句块n>   #如果引发了异常，但与上述异常都不匹配，执行此语句块
else:
    <else语句块>         #如果没有上述所列的异常发生，执行else语句块
finally:
    <任何情况下都要执行的语句块>
'''