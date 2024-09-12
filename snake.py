
from turtle import *

START_POSITION = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20  #constansts are always in capital letter
UP = 90 #constants for head angles of the snake
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self): #creating method that only assembles the segments of body using for loop
        for i in START_POSITION:  # creating snake body comprising of three square pieces together
            self.create_body(i)


    def create_body(self, i): #creating a method that creates each segments of snake body
        jack = Turtle()
        jack.shape("square")
        jack.color("white")
        jack.penup()
        jack.goto(i)
        self.snake_body.append(jack)

    def add_body(self): #method to add a new segment to the last position of the body segment everytime the snake eats food
        position = self.snake_body[-1].position()
        self.create_body(position)



    def move(self):
        for segments in range (len(self.snake_body)-1, 0, -1): #we start from length of the snake body-1 since the indexing in python starts form 0  to the total length -1
            new_x = self.snake_body[segments-1].xcor() #we take the second segment from the list and save its x coordinate
            new_y = self.snake_body[segments-1].ycor() # we take the second segment from the list and save its y coordinate
            self.snake_body[segments].goto(new_x, new_y) # now we update the third segment with the second segment coordinate, and the loop follows on till the second segment except the first segment, first segement has its own independent movement
        self.snake_body[0].forward(MOVE_DISTANCE) #head moves independently and is outside the for loop
        #or we can use self.head.forward but on doing so in up , down, left and right function use self.head.setheading


    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)


    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(0)
