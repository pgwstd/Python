#猜数字游戏。在程序中预设一个0到100之间的随机数，让用户通过键盘输入一个数字，如果大于预设的数字，则显示“大了”，如果小于预设的数字，则显示“小了”，如此循环，直到用户输入的数字等于预设的数字，显示“预测N次，你猜对了”，并退出程序。
#如果用户输入的不是正整数，则显示“输入内容必须为整数”，并退出程序。
#4.5
import random
num = random.randint(0, 100)
count = 0
while True:
    guess = input("请输入一个数字：")
    if guess.isdigit():
        guess = int(guess)
        count += 1
        if guess > num:
            print("遗憾，太大了")
        elif guess < num:
            print("遗憾，太小了")
        else:
            print("预测{}次，你猜中了！".format(count))
            break
    else:
        print("输入内容必须为整数")
        break