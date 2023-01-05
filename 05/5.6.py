def isHuiWen(str):
    if(len(str) <2):
        return True
    if str[0] !=str[-1]:
        return False
    return isHuiWen(str[1:-1])

str = input("请输入一个字符串：")
if isHuiWen(str):
    print("该字符串为回文字符串")
else:
    print("该字符串不是回文")

