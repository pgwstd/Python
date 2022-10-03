import turtle

turtle.setup(900, 900, 200, 200)
turtle.speed(20)

for i in range(200):
    turtle.left(90)
    turtle.fd(2 + 3 * i)
turtle.hideturtle()
turtle.done()