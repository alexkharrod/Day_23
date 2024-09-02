from turtle import Turtle

import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [-280, -220, -170, -120, -70, -20, 30, 80, 130, 180, 230, 280]
FLEET = []


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1,2)
        self.setheading(180)
        self.move = STARTING_MOVE_DISTANCE
        self.speed = 1
        self.goto(400, random.choice(LANES))











