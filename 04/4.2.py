'''
正则表达式
匹配188开头的所有电话号码
'''
import re
pa=re.compile('188\d{8}')
res=pa.findall('''Mr. Johnson had never been up in an
18812314567 aerophane before and he had read a lot about air
accidents,13861322188s0 one day when a friend offered to
218812311887 take him for 188123456a ride in his own small
phane, Mr. Johnson was very worried about accepting. Finally,
18812311887 however, his friend persuaded him that it was very
safe, and Mr. Johnson boarded the plane.''')
print(res)
'''
基于正则表达式搜索
字符串问题的小结
●应用领域
文本搜索
●文本处理
●优点:
方法简单和直接
●灵活、功能强大
'''