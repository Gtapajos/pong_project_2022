import turtle
import winsound
import time

# draw screen
from turtle import Screen, Turtle

screen: Screen = turtle.Screen()
screen.bgcolor("black")
screen.title("My Pong")
screen.tracer(0)
screen.setup(width=800, height=600)

# draw paddle 1
paddle_1: Turtle = turtle.Turtle()
paddle_1.shape("square")
paddle_1.speed(0)
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350, 0)

# draw paddle 2
paddle_2: Turtle = turtle.Turtle()
paddle_2.shape("square")
paddle_2.speed(0)
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350, 0)

# draw ball
ball: Turtle = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# insert the name of player
player_1 = screen.textinput("Player 1", "Name of the player: ")
player_2 = screen.textinput("Player 2", "Name of the player: ")

# score
score_1 = 0
score_2 = 0
score_win = 10

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write(
    str(player_1) + "  0 " + ": 0  " + str(player_2),
    align="center",
    font=("Press Start 2P", 24, "normal")
)


def paddle_1_up():
    y = paddle_1.ycor()
    if paddle_1.ycor() < 250:
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if paddle_2.ycor() < 250:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if paddle_2.ycor() > -250:
        y += -30
    else:
        y = -250
    paddle_2.sety(y)


# keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:

    # bal movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    screen.update()

    # collision with the upper wall
    if 290 < ball.ycor():
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write(
            str(player_1) + f"  {score_1} " + f": {score_2}  " + str(player_2),
            align="center",
            font=("Press Start 2P", 24, "normal")
        )
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = 0.3
        if ball.dy >= 0:
            ball.dy = 0.3
        if ball.dy < 0:
            ball.dy = -0.3
    # collision with right wall
    if ball.xcor() > 390:
        hud.clear()
        score_1 += 1
        hud.write(
            str(player_1) + f"  {score_1} " + f": {score_2}  " + str(player_2),
            align="center",
            font=("Press Start 2P", 24, "normal")
        )
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx = -0.3
        if ball.dy >= 0:
            ball.dy = 0.3
        if ball.dy < 0:
            ball.dy = -0.3

    # collision with the paddle 1
    if (
            -340 < ball.xcor() < -330
            and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50
    ):
        ball.setx(-330)
        # speed 1
        if paddle_1.ycor() + 10 > ball.ycor() > paddle_1.ycor() - 10:
            if ball.dy > 0:
                ball.dy = 0.2
            if ball.dy < 0:
                ball.dy = -0.2
            ball.dx *= -1
        # speed 2
        if paddle_1.ycor() + 40 > ball.ycor() > paddle_1.ycor() + 10 \
                or paddle_1.ycor() - 10 > ball.ycor() > paddle_1.ycor() - 40:
            if ball.dy > 0:
                ball.dy = 0.4
            if ball.dy < 0:
                ball.dy = -0.4
            ball.dx = 0.4
        # speed 3
        if paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() + 40 \
                or paddle_1.ycor() - 40 > ball.ycor() > paddle_1.ycor() - 50:
            if ball.dy > 0:
                ball.dy = 0.7
            if ball.dy < 0:
                ball.dy = -0.7
            ball.dx = 0.6
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # collision with the paddle 2
    if (
            340 > ball.xcor() > 330
            and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50
    ):
        ball.setx(330)
        # speed 1
        if paddle_2.ycor() + 10 > ball.ycor() > paddle_2.ycor() - 10:
            if ball.dy > 0:
                ball.dy = 0.2
            if ball.dy < 0:
                ball.dy = -0.2
            ball.dx *= -1
        # speed 2
        if paddle_2.ycor() + 40 > ball.ycor() > paddle_2.ycor() + 10 \
                or paddle_2.ycor() - 10 > ball.ycor() > paddle_2.ycor() - 40:
            if ball.dy > 0:
                ball.dy = 0.4
            if ball.dy < 0:
                ball.dy = -0.4
            ball.dx = -0.4
        # speed 3
        if paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() + 40 \
                or paddle_2.ycor() - 40 > ball.ycor() > paddle_2.ycor() - 50:
            if ball.dy > 0:
                ball.dy = 0.7
            if ball.dy < 0:
                ball.dy = -0.7
            ball.dx = -0.6
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # winner
    if score_1 >= score_win:
        screen.clear()
        screen.bgcolor("black")
        hud.goto(0, 0)
        hud.color('yellow')
        hud.write(
            str(player_1) + " won the match! ", align="center",
            font=("Press Start 2P", 32, "normal")
        )
        time.sleep(3)
        break

    elif score_2 >= score_win:
        hud.color('yellow')
        screen.clear()
        screen.bgcolor("black")
        hud.goto(0, 0)
        hud.write(
            str(player_2) + " won the match! ", align="center",
            font=("Press Start 2P", 32, "normal")
        )
        time.sleep(3)
        break
