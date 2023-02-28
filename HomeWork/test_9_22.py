# 温度转换
# TempStr = input("请输入带有符号的温度值:")
# if TempStr[-1] in ['F', 'f']:
#     C = (eval(TempStr[0:-1]) - 32) / 1.8
#     print("转换后的摄氏温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8 * eval(TempStr[0:-1]) + 32
#     print("转换后的华氏温度是{:.2f}F".format(F))
# else:
#     print("输入有误！！！")

# 修改后(方式一)
# Symbol = input("请输入你要转换的温度类型('F'、'f'转为摄氏温度,'C'、'c'转为华氏温度):")
# if Symbol in ['F', 'f']:
#     TempStr = eval(input("请输入华氏温度值:"))
#     C = int((TempStr - 32) / 1.8)
#     print("转换后的摄氏温度是{:d}C".format(C))
# elif Symbol in ['C', 'c']:
#     TempStr = eval(input("请输入摄氏温度值:"))
#     F = int(1.8 * (TempStr + 32))
#     print("转换后的华氏温度是{:d}F".format(F))
# else:
#     print("输入有误！！！")


# 修改后（方式二）
TempStr = eval(input("请输入带有符号的温度值:")[0:-1])
Symbol = input("请输入你要转换的温度类型('F'、'f'转为摄氏温度,'C'、'c'转为华氏温度):")
if Symbol in ['F', 'f']:
    C = int((TempStr - 32) / 1.8)
    print("转换后的摄氏温度是{:d}C".format(C))
elif Symbol in ['C', 'c']:
    F = int(1.8 * (TempStr + 32))
    print("转换后的华氏温度是{:d}F".format(F))
else:
    print("输入有误！！！")
