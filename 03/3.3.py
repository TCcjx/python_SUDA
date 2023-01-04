'''
谁是罪犯？
'''

# candidates = 'ABCD'
# for ch in candidates:
#     count = 0
#     if ch != 'A': count +=1
#     if ch == 'C': count +=1
#     if ch == 'D': count +=1
#     if ch != 'D': count +=1
#     if count == 3:
#         print('罪犯是：',ch)
#         break

'''
2
'''
# values = (0,1) #0表示未参加，1表示参加
# candidates = [(A,B,C,D,E) for A in values for B in values
#               for C in values for D in values for E in values]
# # print(candidates)
# for item in candidates:
#     count  = 0
#     if item[0] + item[1] ==2 or item[0]==0:
#         count += 1
#     if item[1] + item[2] ==1:
#         count += 1
#     if item[2] + item[3] ==2 or item[2] + item[3] ==0:
#         count += 1
#     if item[3] + item[4] >=1:
#         count += 1
#     if item[4] + item[3] + item[0] == 3 or item[4]==0:
#         count += 1
#     if count == 5:
#         print(item)
#         break

'''
思考题
'''

candidates = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
for item in candidates:
    count = 0
    if item[0] + item[2] ==0:
        count += 1
    if item[1] + item[3] == 1:
        count += 1
    if item[0] == 1 and item[1] ==0:
        count += 1
    if item[1] + item[3] == 0:
        count += 1
    if count == 1:
        print(item)
        break