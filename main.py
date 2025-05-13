from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width = 800,height = 600)
screen.bgcolor('black')
screen.title("Ping Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0 ))
l_paddle= Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

default_sleep = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(default_sleep)
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    # Detect collision with upper and lower wall || اكتشاف التصادم مع الحائط العلوي والسفلي
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1
    
    # Collision detection with bats || اكتشاف التصادم مع المضارب
    if( ball.xcor() >= 330 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= -330 and ball.distance(l_paddle) <= 50):
        ball.x_move *= -1
        default_sleep *= 0.9

    # If you exit from the right || اذا خرجت من جهة اليمين
    if ball.xcor() > 400:
        ball.goto((0,0))
        ball.x_move *= -1
        default_sleep = 0.1
        scoreboard.l_point()
    
    # If you exit from the left || اذا خرجت من جهة اليسار
    if ball.xcor() < -400:
        ball.goto((0,0))
        ball.x_move *= -1
        default_sleep = 0.1
        scoreboard.r_point()
     
    if scoreboard.left_score == 7 or scoreboard.right_score == 7:
        scoreboard.game_over()
        game_on = False

  




screen.exitonclick()
