'''
函数问题分而治之
'''
def read_file(fn):
    f = open(fn,'rt')
    data = f.readlines()
    f.close()
    return data

def legal_date(date):
    year, month, day = (int(x) for x in tuple(date.split("-")))
    if year<=0 or month<=0 or day<=0:
        return False
    month1 = {1, 3, 5, 7, 8, 10,12}
    month2 = {4, 6, 9,11}
    leap,legal = False, False
    if year%4==0 and year%100!=0 or year%400==0:
        leap = True
    if month in month1:
        if 1<=day<=31:
            legal = True
    elif month in month2:
        if 1<=day<=30:
            legal = True
    elif month == 2:
        if not leap and 1<=day<=28: #平年的2月
            legal = True
        elif leap and 1<=day<=29: #闰年的2月
            legal- True
    return legal

def display(data):
    for item in data:
        if legal_date(item):
            print(item, end='')

if __name__ == '__main__':
    display(read_file('date.txt'))

