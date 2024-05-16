from turtle import Turtle,Screen,colormode

import snake
from scoreBoard import ScoreBoard
import food
from food import Food
from snake import Snake
import time
gameOn = True


screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(600,600)
snaky = Snake()
sb = ScoreBoard()
foof = Food()
screen.onkey(key="Up",fun=snaky.turnUp)
screen.onkey(key="Down",fun=snaky.turnDown)
screen.onkey(key="Left",fun= snaky.turnLeft)
screen.onkey(key="Right",fun= snaky.turnRight)
while gameOn == True:
    screen.update()
    time.sleep(0.1)
    snaky.snakeStart()
    if snaky.snakeSquares[0].distance(foof) < 15:
        foof.refresh()
        snaky.extendSnake()
        sb.updateScore()

    if snaky.snakeSquares[0].xcor() > 280 or snaky.snakeSquares[0].xcor() < -280 or snaky.snakeSquares[0].ycor() > 280 or snaky.snakeSquares[0].ycor() < -280:
        gameOn = False
        sb.gameOver()

    for segment in snaky.snakeSquares[1:]:
        if snaky.snakeSquares[0].distance(segment) < 10:
            gameOn = False
            sb.gameOver()











screen.exitonclick()