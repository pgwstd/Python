#画出一个等边三角形
import turtle
turtle.setup(650, 600, 200, 200) # 设置窗口大小和位置
turtle.penup()
turtle.fd(-200)
turtle.pendown()
# turtle.speed(1000000000000)
for i in range(3):
    turtle.fd(200)
    turtle.right(-120)
turtle.done()
