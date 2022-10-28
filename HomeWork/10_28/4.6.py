# 羊车门问题。有3扇关闭的门，其中一扇后面停着汽车，其余门后是山羊，只有主持人知道每扇门后面是什么。参赛者可以选择一扇门，在开启它之前，主持人会地芒另外一扇门，露出门后的山羊，然后问参赛者是否要换另外一扇门。请问参赛者更换选择后能否增加猜中汽车的机会？

from random import *

TIMES = 10000
my_first_choice_n = 0  # 初始化不改选择的次数
my_change_choice_n = 0  # 初始化更改选择的次数
for i in range(TIMES):
    car_inDoor = randint(0, 2)
    my_guess = randint(0, 2)
    if car_inDoor == my_guess:
        my_first_choice_n += 1
    else:
        my_change_choice_n += 1
print("不改选择:{}".format(my_first_choice_n / TIMES))
print("更改选择:{}".format(my_change_choice_n / TIMES))
