# 彩色小蛇绘制
# import turtle
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.pencolor("red")
#     turtle.circle(-40, 80)
#     turtle.pencolor("blue")
# turtle.circle(40, 80/2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.circle(40)
# turtle.done()


import turtle
color = ['black', 'grey', 'pink', 'gold']
turtle.setup(650,320,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
for i in range(4):
    turtle.pencolor(color[i])
    turtle.circle(40, 80)
    turtle.pencolor(color[i+1])
    turtle.circle(-40, 80)
turtle.pencolor('purple')
turtle.circle(40, 40)
turtle.fd(40)
turtle.pencolor('red')
turtle.circle(16, 180)
turtle.fd(40)
turtle.done()