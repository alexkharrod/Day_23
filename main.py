#setup game - import files needed
import random
import time
from turtle import Screen
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from player import Player, STARTING_POSITION
from scoreboard import Scoreboard

def game_loop(level):
   pass


# instantiate my classes
screen = Screen()
player = Player()
score_board = Scoreboard()


FLEET = []
# Setup Screen
screen.tracer(0)
screen.screensize(600, 600)
screen.title("Turtle Crossing")
score_board.level_up(player.level)

# start game loop
game_is_on = True
while game_is_on:
    time.sleep = 0.01
    screen.update()

    # randomly create cars
    coin_toss = random.random()
    if coin_toss < .040:
        new_car = CarManager()
        FLEET.append(new_car)

    #  Make the turtle cross the road - can only move forwards
    screen.listen()
    screen.onkey(player.move_turtle, "Up")

    # make the game stop when you are hit by a car
    for car in FLEET:
        car.forward(car.move)
        if player.detect_collision(car):
            score_board.game_over()
            game_is_on = False

#  set screen score create levels and  increase car speeds
    if player.ycor() >= 290:
        player.made_it()
        score_board.clear()
        score_board.level_up(player.level)
       ### how to figure this out car_manager.move += MOVE_INCREMENT













screen.exitonclick()