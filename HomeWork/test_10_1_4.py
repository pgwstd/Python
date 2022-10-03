import turtle

turtle.setup(650, 600, 200, 200)
turtle.penup()
turtle.fd(-200)
turtle.pendown()
for i in range(3):
    turtle.fd(100)
    turtle.right(-120)
for i in range(3):
    turtle.fd(-100)
    turtle.right(120)
turtle.done()
