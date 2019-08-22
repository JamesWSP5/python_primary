a = 1  # 整数
f = 0xff00  # 十六进制
g = 1.23e9  # e代表10的n此方
b = 1.0  # 小数
c = 'str'  # 字符串
d = 'I\'m \"ok\"'  # 转义字符串,如果是特殊字符需要转义可以在字符前面加\,转义即是废弃特殊字符的功能，使其代表一个普通字符
e = 'I\'m "ok"'  # 双引号在这里可以不用转义
h = r'\t'  # 在字符串前面加r则标识字符串内的内容全部不转义
i = '''        
i am a progamer,
i love program 
'''  # ''' '''保留字符之间的换行字符，不用加\n去换行。，前面可加r，使字符串内特殊字符全部转义

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
# 布尔值
data1 = 1
data2 = 2
if (data1 > data2):#if会根据判断布尔值选择要走的分支
    print("data1>data2")
else:
    print("data1<data2")


