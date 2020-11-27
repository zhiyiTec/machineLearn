# import turtle
#
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("purple")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.circle(40, 80 / 2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40 * 2 / 3)
# turtle.done()


# import turtle as t
# t.pensize(2)
# for i in range(4):
#     t.fd(150)
#     t.left(90)


# import turtle as t
#
# t.pensize(2)
# for i in range(6):
#     t.fd(150)
#     t.left(60)


# import turtle as t
#
# t.pensize(2)
# for i in range(9):
#     t.fd(150)
#     t.left(80)  # 720/9


import turtle as t

t.pensize(2)
for i in range(4):
    t.seth(90 * i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0, 0)
