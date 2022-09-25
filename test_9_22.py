# TempStr = input("请输入带有符号的温度值:")
# if TempStr[-1] in ['F', 'f']:
#     C = (eval(TempStr[0:-1]) - 32) / 1.8
#     print("转换后的摄氏温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8 * eval(TempStr[0:-1]) + 32
#     print("转换后的华氏温度是{:.2f}F".format(F))
# else:
#     print("输入有误！！！")

#修改后
TempStr = eval(input("请输入带有符号的温度值:"))

# print(TempStr)
C = int((TempStr - 32) / 1.8)
print("转换后的摄氏温度是{:d}C".format(C))

F = int(1.8 * (TempStr + 32))
print("转换后的华氏温度是{:d}F".format(F))
