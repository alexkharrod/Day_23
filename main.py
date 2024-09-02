#setup game - import files needed
import time

from turtle import Screen

from car_manager import CarManager

from player import Player

from scoreboard import Scoreboard



# instantiate my classes
screen = Screen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Setup Screen
screen.tracer(0)
screen.screensize(600, 600)

# start game loop
game_is_on = True
while game_is_on:
    time_delay = 0.1
    screen.update()
    #  Make the turtle cross the road - can only move forwards
    screen.listen()
    screen.onkey(player.move_turtle, "Up")



# create cars



#  set screen score create levels and  increase car speeds


# create levels

# make the game stop when you are hit by a car

screen.exitonclick()