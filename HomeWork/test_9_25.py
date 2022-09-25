#汇率转换
Money = input("请输入带有符号的转换数值:")
if Money[-3:] in ['USD', 'usd']:
    RMB = (eval(Money[0:-3]) * 6)
    print((Money[0:-3]) + "美元转换后的人民币是{:.2f}".format(RMB))
elif Money[-3:] in ['RMB', 'rmb']:
    USD = eval(Money[0:-3]) / 6
    print((Money[0:-3]) + "人民币转换后的美元是{:.2f}".format(USD))
else:
    print("输入有误！！！")