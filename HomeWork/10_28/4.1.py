#猜数字游戏。在程序中预设一个0到9之间的随机数，让用户通过键盘输入一个数字，如果大于预设的数字，则显示“大了”，如果小于预设的数字，则显示“小了”，如此循环，直到用户输入的数字等于预设的数字，显示“猜对了”，并退出程序。
import random
num = random.randint(0, 9)
count = 0
while True:
    guess = int(input("请输入一个数字："))
    count += 1
    if guess > num:
        print("遗憾，太大了")
    elif guess < num:
        print("遗憾，太小了")
    else:
        print("预测{}次，你猜中了！".format(count))
        break