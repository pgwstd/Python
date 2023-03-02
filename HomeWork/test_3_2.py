# n = input("请输入整数N:")
# sum = 0
# for i in range(int(n)):
#     sum += i + 1
# print("1到N的和为:", sum)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # print("%d*%d=%d" % (i, j, i * j), end="\t")
#         print("{}*{}={:2}" .format(j, i, i * j), end="\t")
#     print('')

# from turtle import *
# fillcolor("red")
# begin_fill()
# while True:
#     forward(200)
#     right(144)
#     if abs(pos()) < 1:
#         break
# end_fill()

# TempStr = input("请输入带有符号的温度值:")
# if TempStr[-1] in ['F', 'f']:
#     C = (eval(TempStr[0:-1]) - 32) / 1.8
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8 * eval(TempStr[0:-1]) + 32
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")


# import turtle
#
# turtle.setup(650, 350, 200, 200)  # 设置窗口大小和位置
# turtle.penup()
# turtle.fd(-250)  # 向前移动250像素
# turtle.pendown()
# turtle.pensize(25)  # 设置画笔宽度
# turtle.pencolor("purple")  # 设置画笔颜色
# turtle.seth(-40)  # 设置画笔方向
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.circle(40, 80 / 2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40 * 2 / 3)


