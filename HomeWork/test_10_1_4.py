import turtle

# 方式一：
# turtle.setup(650, 600, 200, 200)
# turtle.penup()
# turtle.fd(-200)
# turtle.pendown()
# turtle.right(30)
# for i in range(6):
#     turtle.left(120)
#     turtle.fd(80)
#     turtle.right(60)
#     turtle.fd(80)
#
# turtle.left(120)
# turtle.fd(80)
# for j in range(6):
#     turtle.fd(80)
#     turtle.left(60)
# turtle.done()

# 方式二：
turtle.setup(650, 600, 200, 200)
turtle.penup()
turtle.pensize(2)
turtle.right(30)
turtle.pendown()
for i in range(3):
    turtle.fd(180)
    turtle.right(120)

turtle.penup()
turtle.goto(90, -180)
turtle.pendown()
turtle.left(120)
for i in range(3):
    turtle.fd(180)
    turtle.right(-120)
turtle.done()
