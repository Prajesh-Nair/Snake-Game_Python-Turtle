from turtle import *
import time
from Snake import Snake
from food import Food
from ScoreBoard import ScoreB

colormode(255)
src = Screen()
src.setup(600,600)
bgcolor(0,0,0)
src.title("Snake Game")
src.tracer(0)
src.listen()
snake = Snake()
food = Food()
sb = ScoreB()

src.onkeypress(snake.left,"a")
src.onkeypress(snake.right,"d")
src.onkeypress(snake.up,"w")
src.onkeypress(snake.down,"s")

game_is_on = True
while game_is_on:
    src.update()
    snake.move()
    time.sleep(0.125)

    #detct collision
    if snake.head.distance(food) < 15:
        food.shift()
        sb.score_inc()
        snake.Grow()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        snake.reset()
        sb.reset()
    for snakess in snake.snakes[1:]:
        if snakess.distance(snake.head) < 9:
            snake.reset()
            sb.reset()



src.exitonclick()