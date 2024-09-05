from turtle import Turtle

import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [-220, -170, -120, -70, -20, 30, 80, 130, 180, 230, 280]


STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1
FLEET =[]



class CarManager(Turtle):
    move = STARTING_MOVE_DISTANCE
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1,2)
        self.setheading(180)
        self.goto(400, random.choice(LANES))
        print(self.move)


















