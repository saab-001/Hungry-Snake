from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def create_screen(pablo):
    pablo.goto(0, 290)
    pablo.pensize(2)
    pablo.color("white")
    pablo.setheading(180)
    pablo.forward(290)
    pablo.setheading(270)
    pablo.forward(580)
    pablo.setheading(0)
    pablo.forward(580)
    pablo.setheading(90)
    pablo.forward(580)
    pablo.setheading(180)
    pablo.forward(290)
    pablo.hideturtle()


ground = Screen()
ground.setup(650, 650)
ground.bgcolor("black")
ground.title("snake")
ground.tracer(0)
ground.listen()

keeper = Turtle()
create_screen(keeper)

snake_food = Food()
my_snake = Snake()
watcher = ScoreBoard()

ground.onkey(my_snake.up, "Up")
ground.onkey(my_snake.down, "Down")
ground.onkey(my_snake.left, "Left")
ground.onkey(my_snake.right, "Right")

ground.update()
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

    if my_snake.snake_head.xcor() < -282 or my_snake.snake_head.ycor() < -282 or my_snake.snake_head.xcor() > 282 or\
            my_snake.snake_head.ycor() > 282:
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
