'''
●已知一一个英文文本文件。需要求出其中字母的
使用频度(大小写不敏感)。
'''
f = open("text.txt",'rt')
data = f.readlines()
f.close()

dic = dict()
for line in data:
    line = line.upper()
    for c in line:
        if 'A' <= c <= 'Z':
            dic[c] = dic.get(c,0) + 1

i = 0
print(sorted(dic))
for k in sorted(dic):
    print('%s:%d\t'%(k,dic[k]),end='')
    i += 1
    if i%4 ==0:
        print("")