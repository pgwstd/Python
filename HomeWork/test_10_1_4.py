import turtle

turtle.setup(650, 600, 200, 200)
turtle.penup()
# turtle.fd(-200)
turtle.pendown()
for i in range(6):
    turtle.left(120)
    turtle.fd(80)
    turtle.right(60)
    turtle.fd(80)
    
turtle.left(120)
turtle.fd(80)
for j in range(6):
    turtle.fd(80)
    turtle.left(60)
turtle.done()
