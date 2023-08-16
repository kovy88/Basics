from turtle import Turtle, Screen
import turtle
import os
import random
from data import colors, rotation

turtle.colormode(255)

tommy = Turtle()
tommy.color("black", "cyan")

#for i in range(4):
#    for j in range(4):
#        tommy.fd(50)
#        tommy.left(90)
#    tommy.right(90)
#tommy.fd(50)
#for i in range (20):
#    tommy.fd(10)
#    tommy.penup()
#    tommy.fd(10)
#    tommy.pendown()
#a = 3
#while a < 10:
#    angel = 360 / a
#    x = random.choice(colors)
#    tommy.pencolor(x)
#    for i in range (a):
#        tommy.fd(100)
#        tommy.rt(angel)
#    a+=1
#
#
#def random_color():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    random_col = (r, g, b)
#    return random_col

#speed = 1
#for i in range (200):
#    tommy.pencolor(random_color())
#    tommy.fd(30)
#    tommy.right(random.choice(rotation))
#    tommy.speed(speed)
#    speed += 1
#    if i < 7:
#        tommy.pensize(i)
#
#tommy.speed(20)
#
#def spinograf(gap):
#    for j in range(int(360/gap)):
#        tommy.pencolor(random_color())
#        tommy.pensize(2)
#        tommy.circle(80)
#        tommy.left(gap)
#
#spinograf(1)
tommy.speed(10)
#for i in range (1000):
#    tommy.pencolor(colors[i%6])
#    tommy.fd(i)
#    tommy.left(60)
#tommy.begin_fill()
#for i in range (4):
#    tommy.fd(88)
#    tommy.lt(90)
#tommy.end_fill()
 
lojza = Turtle()
lojza.pencolor("red")
lojza.pensize(2)
lojza.circle(10)
tommy.pensize(2)

for i in range (15, 80, 10):
    tommy.pencolor("green")
    tommy.circle(i)


my_screen = Screen()
my_screen.bgcolor("grey")
my_screen.exitonclick()
os.system("cls")
 