from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.argument = f"Score : {self.score}"
        self.shape('classic')
        self.penup()
        self.color("black")
        self.goto(0,270)
        self.writeScore()
        self.hideturtle()

    def writeScore(self):
        self.write(f"Score : {self.score}", align="center", font=('Arial', 20, 'normal'))
    def updateScore(self):
        self.score += 1
        self.clear()
        self.writeScore()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=('Arial', 20, 'normal'))