from turtle import Turtle


class Snake:

    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snakeSquares = []
        self.snakeDisplay()

    def snakeDisplay(self):
        for position in self.positions:
            self.addSegment(position)

    def addSegment(self, position):

        tim = Turtle(shape="square")
        tim.penup()
        tim.goto(position)
        self.snakeSquares.append(tim)

    def extendSnake(self):
        self.addSegment(self.snakeSquares[-1].position())
    def snakeStart(self):
        for seg_num in range(len(self.snakeSquares) - 1, 0, -1):
            x_cor = self.snakeSquares[seg_num - 1].xcor()
            y_cor = self.snakeSquares[seg_num - 1].ycor()
            self.snakeSquares[seg_num].goto(x_cor, y_cor)
        self.snakeSquares[0].forward(20)

    def turnUp(self):
        if self.snakeSquares[0].heading() != 270:
            self.snakeSquares[0].setheading(90)
    def turnDown(self):
        if self.snakeSquares[0].heading() != 90:
            self.snakeSquares[0].setheading(270)
    def turnLeft(self):
        if self.snakeSquares[0].heading() != 0:
            self.snakeSquares[0].setheading(180)
    def turnRight(self):
        if self.snakeSquares[0].heading() != 180:
            self.snakeSquares[0].setheading(0)