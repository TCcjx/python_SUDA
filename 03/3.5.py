'''
百钱百鸡问题
公鸡/5
母鸡/3
小鸡 1/每三只
*穷举法*
'''
# for cock in range(0,21):
#     for hen in range(0,34):
#         chick = 100 -cock -hen
#         if chick%3==0 and cock*5 + hen*3 + chick//3 == 100:
#             print("cock{0:2d}，母鸡{1:2d},小鸡{2:2d}".format(cock,hen,chick))

'''
穷举法求 100 以内的勾股数
'''
for i in range(1,101):
    for j in range(i+1,101):
        for x in range(j+1,101):
            if i**2 + j**2 == x**2:
                print('{0:2d} {1:2d} {2:2d}'.format(i,j,x))