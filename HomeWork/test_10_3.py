import turtle

turtle.setup(800, 600, 200, 200)
turtle.speed(20)

for i in range(200):
    turtle.left(90)
    turtle.fd(2 * i)

turtle.done()