from turtle import Turtle, Screen
import time, random

score = 0
highest_score = 0

screen = Screen()
screen.bgcolor("green")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(False)

#Hlava
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Body
body_parts = []

#Potrava
ran_x = random.randint(-280, 280)
ran_y = random.randint(-280, 280)
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(ran_x, ran_y)

#Score
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write(f"Score: 0  Nejvyssi skore = 0", align="center", font=("", 18))

#Funkce

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "stop":
        y = head.ycor()
        head.sety(y)
        x = head.xcor()
        head.setx(x)
def move_up():
    if head.direction != "down":
        head.direction = "up"
def move_down():
    if head.direction != "up":
        head.direction = "down"
def move_right():
    if head.direction != "left":
        head.direction = "right"
def move_left():
    if head.direction != "right":
        head.direction = "left"

screen.listen()

screen.onkeypress(move_up,"w")
screen.onkeypress(move_down,"s")
screen.onkeypress(move_right,"d")
screen.onkeypress(move_left,"a")

#Hlavni cyklus
while True:

    screen.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        for i in body_parts:
            i.goto(10000,10000)
        body_parts.clear()

        score = 0
        score_sign.clear()
        score_sign.write(f"Skore: {score}  Nejvyssi skore: {highest_score}", align="center", font=("",18))

    if head.distance(apple) < 20:
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        apple.goto(ran_x, ran_y)

        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

        score += 10

        if score > highest_score:
            highest_score = score
        score_sign.clear()
        score_sign.write(f"Skore: {score}  Nejvyssi skore: {highest_score}", align="center", font=("",18))

    for i in range(len(body_parts) - 1, 0, -1):
        x = body_parts[i - 1].xcor()
        y = body_parts[i - 1].ycor()
        body_parts[i].goto(x, y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
    move()

    for i in body_parts:
        if i.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            
            for i in body_parts:
                i.goto(10000,10000)
            body_parts.clear()

            score = 0
            score_sign.clear()
            score_sign.write(f"Skore: {score}  Nejvyssi skore: {highest_score}", align="center", font=("",18))

    time.sleep(0.1)

screen.exitonclick()