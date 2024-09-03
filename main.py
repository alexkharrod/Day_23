#setup game - import files needed
import random
import time
from turtle import Screen
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from player import Player
from scoreboard import Scoreboard




# instantiate my classes
screen = Screen()
player = Player()
scoreboard = Scoreboard()


FLEET = []
# Setup Screen
screen.tracer(0)
screen.screensize(600, 600)


# start game loop
game_is_on = True
while game_is_on:
    time.sleep = 1
    screen.update()

    # randomly create cars
    coin_toss = random.random()
    if coin_toss < .040:
        new_car = CarManager()
        FLEET.append(new_car)

    #  Make the turtle cross the road - can only move forwards

    screen.listen()
    screen.onkey(player.move_turtle, "Up")




    for car in FLEET:
        car.forward(1)
        if player.detect_collision(car):
            game_is_on = False






#  set screen score create levels and  increase car speeds


# create levels

# make the game stop when you are hit by a car

screen.exitonclick()