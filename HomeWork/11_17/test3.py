import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 90, -90, -90, 90]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(800, 800)
    turtle.speed(0)  # 画的速度
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 4
    koch(300, level)
    turtle.right(90)
    koch(300, level)
    turtle.right(90)
    koch(300, level)
    turtle.right(90)
    koch(300, level)
    turtle.hideturtle()  # 不要出现箭头
    turtle.done()  # 不要关闭窗口


main()
