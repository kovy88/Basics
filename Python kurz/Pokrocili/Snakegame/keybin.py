from turtle import Turtle, Screen
screen = Screen()

t = Turtle("turtle")

def move_fd():
    t.fd(20)

screen.listen()
screen.onkeypress(move_fd,"w")
screen.exitonclick()