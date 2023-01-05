keyCount,rowCount = map(int,input().split())
keys = [i for i in range(1,keyCount+1)] #[1,2,3,4,5]
datas = []
for i in range(rowCount):
    temp=list(map(int,input().split()))
    datas.append([temp[0],temp[1],1]) #借记录
    datas.append([temp[0],temp[1]+temp[2],2]) #还记录

print(datas)
datas.sort(key=lambda temp:(temp[1],-temp[2],temp[0])) #排序条件：1、首先是借用的时间2、同时借还的时候，是先还再借，所以排序依照-temp[2]
print(datas)
for item in datas:
    if item[2] == 1: #借的记录
        keys[keys.index(item[0])] = 0  #index返回第一个为0的位置
    else:
        keys[keys.index(0)] = item[0]
for item in keys:
    print(item,end='')