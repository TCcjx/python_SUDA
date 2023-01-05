'''
Base84编码
最常见的用于传输8位字节码的编码方式
是电子邮件中常用的编码方式
●是一种用64个可打印符号来表示二进制数据的方法
”因此被称为“Base64”
'''
'''
***编码方法***
●本质上是3字节转4字节
●3*8=4*6
将3字节中数据每次取6位
●用6位得到的数值(0-63)作为索引去查编码表
'''
'''
参考资料：https://blog.csdn.net/weixin_44983653/article/details/
113800958?ops_request_misc=&request_id=&biz_id=102&utm_term=base64%E7%BC%96%E7%A0%81%20Python%E5
%87%BD%E6%95%B0&utm_medium=distribute.pc_search_result.none-task-blog
2~all~sobaiduweb~default-0-113800958.142^v68^control,201^v4^add_ask,213^v2^t3_esquery_v3&spm=1018.2226.3001.4187
'''
import base64
a = base64.b64encode('ILoveJIAJIA'.encode('utf-8'))
print(str(a,'utf-8'))
print(str(base64.b64decode(a),'utf-8'))