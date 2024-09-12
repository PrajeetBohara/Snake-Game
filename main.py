import turtle
from turtle import *
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  #screen is turned off now. this method is used to control the speed at which the turtle graphics screen updates.

score = 0 #to keep track of score every time the snake eats food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.snake_body[0].distance(food) < 15: #condition to measure the distance between the snake head and the food
        food.spawn_food()
        snake.add_body()
        scoreboard.update_score()
 #detect collision with wall
    if snake.snake_body[0].xcor() > 298 or snake.snake_body[0].xcor() < -298 or snake.snake_body[0].ycor() > 299 or snake.snake_body[0].ycor() < -299:
        game_is_on = False
        scoreboard.end_game()
 #detect collision with tail
    for i in snake.snake_body:
        if i == snake.snake_body[0]: #the loop started with the head so was showing game over at the start of game. So to bypass that we ignored for the head segment and game over only for other body segment
            pass
        elif snake.snake_body[0].distance(i) < 10:
            game_is_on = False
            scoreboard.end_game()

    #detecting collision with tail using slicing
    # for i in snake.snake_body[1:]:
    #     if snake.snake_body[0].distance(i) < 10:
    #        game_is_on = False
    #        scoreboard.end_game()













screen.exitonclick()
