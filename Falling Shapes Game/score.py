from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align = 'center', font = ("Courier", 24, "normal"))
    
    
    def increase_score(self, points):

        self.score += points
        self.update_scoreboard()

    
    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.screen.bgcolor("darkred")
        self.goto(0, 0)
        self.write(f"Game Over \nFinal Score: {self.score}", align = "center", font = ("Arial", 24, 'normal'))
        
