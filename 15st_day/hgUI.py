# # from turtle import *

# # # 设置笔刷宽度:
# # width(4)

# # # 前进:
# # forward(200)
# # # 右转90度:
# # right(90)

# # # 笔刷颜色:
# # pencolor('red')
# # forward(100)
# # right(90)

# # pencolor('green')
# # forward(200)
# # right(90)

# # pencolor('blue')
# # forward(100)
# # right(90)

# # # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# # done()



# from turtle import *

# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     # set heading: 0
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)

# for x in range(0, 250, 50):
#     drawStar(x, 0)

# done()

###分形树
# from turtle import *
# # 设置色彩模式是RGB:
# colormode(255)
# lt(90)
# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# done()
## 分型桃树
# import turtle
# import random
# from turtle import *
# from time import sleep

# t = turtle.Turtle()
# w = turtle.Screen()


# def tree(branchLen, t):
#     if branchLen > 3:
#         if 8 <= branchLen <= 12:
#             if random.randint(0, 2) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')
#             t.pensize(branchLen / 3)
#         elif branchLen < 8:
#             if random.randint(0, 1) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')
#             t.pensize(branchLen / 2)
#         else:
#             t.color('sienna')
#             t.pensize(branchLen / 10)

#         t.forward(branchLen)
#         a = 1.5 * random.random()
#         t.right(20*a)
#         b = 1.5 * random.random()
#         tree(branchLen-10*b, t)
#         t.left(40*a)
#         tree(branchLen-10*b, t)
#         t.right(20*a)
#         t.up()
#         t.backward(branchLen)
#         t.down()


# def petal(m, t):  # 树下花瓣
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 10 - 20 * random.random()
#         t.up()
#         t.forward(b)
#         t.left(90)
#         t.forward(a)
#         t.down()
#         t.color("lightcoral")
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         t.right(90)
#         t.backward(b)


# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     getscreen().tracer(5, 0)
#     turtle.screensize(bg='wheat')
#     t.left(90)
#     t.up()
#     t.backward(150)
#     t.down()
#     t.color('sienna')
#     tree(60, t)
#     petal(100, t)

#     myWin.exitonclick()


# main()

