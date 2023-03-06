from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


ground = Screen()
ground.setup(600, 600)
ground.bgcolor("black")
ground.title("snake")
ground.tracer(0)
ground.listen()

snake_food = Food()
my_snake = Snake()
watcher = ScoreBoard()

ground.onkey(my_snake.up, "Up")
ground.onkey(my_snake.down, "Down")
ground.onkey(my_snake.left, "Left")
ground.onkey(my_snake.right, "Right")

ground.update
game_on = True
while game_on:
    ground.update()
    time.sleep(0.1)
    my_snake.move()
    watcher.show_score()

    if snake_food.distance(my_snake.snake_head) < 17:
        snake_food.reappear()
        my_snake.grow()
        watcher.add_score()

    if my_snake.snake_head.xcor() < -280 or my_snake.snake_head.ycor() < -280 or my_snake.snake_head.xcor() > 280 or my_snake.snake_head.ycor() > 280 :
        game_on = False
        watcher.game_over()

    for part in my_snake.segments:
        if part == my_snake.snake_head:
            pass
        else:
            if my_snake.snake_head.distance(part) < 15:
                game_on = False
                watcher.game_over()

ground.exitonclick()
