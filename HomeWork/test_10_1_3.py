#画一个没有四个角的正方形
import turtle
turtle.setup(650, 450, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pensize(1)

turtle.penup()
turtle.fd(10)
turtle.pendown()
turtle.fd(80)
turtle.penup()
turtle.fd(10)
turtle.seth(90)

turtle.penup()
turtle.fd(10)
turtle.pendown()
turtle.fd(80)
turtle.penup()
turtle.fd(10)
turtle.seth(180)

turtle.penup()
turtle.fd(10)
turtle.pendown()
turtle.fd(80)
turtle.penup()
turtle.fd(10)
turtle.seth(-90)

turtle.penup()
turtle.fd(10)
turtle.pendown()
turtle.fd(80)
turtle.penup()
turtle.fd(10)

turtle.done()