from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Screen setup || اعداد الشاشة
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('Falling Shapes Game')
screen.tracer(0)

# Create the racket, the falling shape, and the scoreboard. || انشاء المضرب ، الشكل المتساقط، ولوحة النتائج
player_paddle = Paddle((0, -250))
falling_shape = Ball()
scoreboard = Scoreboard()


# Keyboard control || التحكم عبر لوحة المفاتيح
screen.listen()
screen.onkey(player_paddle.go_left, "Left")
screen.onkey(player_paddle.go_right, "Right")


# Game variables || متغيرات اللعبة
game_on = True
shape_speed = 0.1

while game_on:
    screen.update()
    time.sleep(shape_speed)
    falling_shape.move()

    # Detect collision with the bat || اكتشاف التصادم مع المضرب
    if falling_shape.distance(player_paddle) < 50 and falling_shape.ycor() < -230:
        # Identify points based on shape and color. || تحديد النقاط بناء علي الشكل واللون
        shape_type = falling_shape.shape()
        shape_color = falling_shape.color()[0]


        if shape_type == 'turtle':
            if shape_color =='white':
                # Hit the white turtle: game over || ضرب سلحفاء بيضاء: انتهاء اللعبة
                game_on = False
                scoreboard.game_over()
            
            else:
                # Hit a turtle of any other color: +5 points || ضرب سلحفاء بأي لون اخر : +5  نقاط
                points = 5
                scoreboard.increase_score(points)
            
        elif shape_type == 'circle':
            # Hit ball (circle): +1 point || ضرب كرة (دائرة): +١ نقطة
            points = 1
            scoreboard.increase_score(points)

        elif shape_type == 'square':
            # Square hit: +2 points || ضرب مربع: +2  نقطة
            points = 2
            scoreboard.increase_score(points)

        elif shape_type == 'triangle':
            # Triangle hit: reset the result to zero || ضرب مثلث: اعادة النتيجة الي الصفر
            scoreboard.reset_score()
        

        # Reset the falling shape || اعادة تعيين الشكل المتساقط
        falling_shape.reset_position()

        # Increase the speed of falling || زيادة سرعة السقوط
        shape_speed *= 0.9

    # Detect shape miss || اكتشاف تفويت الشكل
    if falling_shape.ycor() < -300:
        # Reset the falling shape without affecting the result. || اعادة تعيين الشكل المتساقط دون تاثير علي النتيجة
        falling_shape.reset_position()

screen.exitonclick()
 