from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.y_move = -10
        self.shapes_list = ['turtle', 'circle', 'triangle', 'square']
        self.colors_list = ['red', 'green', 'blue', 'yellow', 'purple']
        self.reset_position()

    
    def move(self):
        self.goto(self.xcor(), self.ycor() + self.y_move)

    def reset_position(self):
        # Set random location at top || تعيين موقع عشوائي في الاعلي
        random_x = random.randint(-350, 350)
        self.goto(random_x, 250)

        
        # Choose a random shape || اختيار شكل عشوائي

        random_shape = random.choice(self.shapes_list)
        self.shape(random_shape)        

        # Random color choice || اختيار لون عشوائي
        if random_shape == 'turtle' and random.randint(1, 10) == 1:
          # 10% chance of the turtle being white || فرصة 10 % لتكون السلحفاة بيضاء
            self.color('white')
        else:
            self.color(random.choice(self.colors_list))

        
        # Random size adjustment || ضبط حجم عشوائي
        random_size = random.uniform(0.5, 2)
        self.shapesize(stretch_wid = random_size, stretch_len = random_size)
