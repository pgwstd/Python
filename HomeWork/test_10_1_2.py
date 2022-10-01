# 画出一个等边三角形里面又有一个等边三角形

import turtle
turtle.setup(650, 600, 200, 200)
turtle.penup()
turtle.fd(-200)
turtle.pendown()
# turtle.speed(1000000000000)
for i in range(3):
    turtle.fd(200)
    turtle.right(-120)
turtle.fd(100)
turtle.seth(60)
turtle.fd(100)
turtle.seth(180)
turtle.fd(100)
turtle.seth(-60)
turtle.fd(100)
turtle.done()
