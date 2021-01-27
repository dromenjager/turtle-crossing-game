# Import the required libraries
from turtle import Turtle, Screen
from player import Player
from car_manager import Cars
from scoreboard import ScoreBoard
import random
import time


# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")

# start screen animation
screen.tracer(0)

# Press enter to start the game
screen.textinput("Welcome to Turtle Crossing Game", 
                 "Press enter to start the game")

# listen to the screen input
screen.listen()

# setup player
player = Player()

# setup cars
cars = Cars()

# add scoreboard
score = ScoreBoard()

# setup keypress-actions
screen.onkey(player.move_up, "Up")

# start the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_cars()
    cars.move()
    # detect collision with player
    for car in cars.created_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # detect when the player successfully crosses the screen
    if player.detect_win():
        player.goto_start()
        # update scoreboard for next level
        score.level_up()
        # increase car speed.
        cars.speed_up()


# Keep display active after game over till keypress
screen.exitonclick()
