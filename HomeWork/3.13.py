#一周工作5天的
DayUp = 1.0
DayUp2 = 1.0
DayUp3 = 1.0
DayUp4 = 1.0
DayUp5 = 1.0
DayUp6 = 1.0
DayUp7 = 1.0
DayUp8 = 1.0
DayUp9 = 1.0
DayUp10 = 1.0
N = 0.001
N2 = 0.002
N3 = 0.003
N4 = 0.004
N5 = 0.005
N6 = 0.006
N7 = 0.007
N8 = 0.008
N9 = 0.009
N10 = 0.01
for i in range(365):
    #以周日为一周的第一天
    if i % 7 not in [0, 6]:
        # dayup = dayup * (1 + 0.001)
        DayUp *= (1 + N)
        DayUp2 *= (1 + N2)
        DayUp3 *= (1 + N3)
        DayUp4 *= (1 + N4)
        DayUp5 *= (1 + N5)
        DayUp6 *= (1 + N6)
        DayUp7 *= (1 + N7)
        DayUp8 *= (1 + N8)
        DayUp9 *= (1 + N9)
        DayUp10 *= (1 + N10)
print("1.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp))   #保留两位小数
print("2.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp2))
print("3.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp3))
print("4.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp4))
print("5.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp5))
print("6.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp6))
print("7.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp7))
print("8.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp8))
print("9.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp9))
print("10.一年中一周工作连续5天，水平可以上升:{:.2f}" .format(DayUp10))
# for i in range(7):
#     if i % 7 not in [0, 6]:
#         print(i)