from turtle import Turtle
import random


COLORS = [
    "gold",
    "green",
    "magenta",
    "yellow green",
    "red",
    "blue",
    "orange",
]
INITIAL_MOVE_STEP = 5
STEP_INCREMENT = 3


class Cars(Turtle):
    """
    Create cars for the
    game
    """

    def __init__(self):
        super().__init__()
        self.created_cars = []
        self.create_cars()
        self.car_speed = INITIAL_MOVE_STEP

    def create_cars(self):
        """
        Create all the cars
        """
        # Generate cars object at random instances
        random_gen = random.randint(1, 6)
        if random_gen == 3:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto((280.0, random.randint(-250, 250)))
            self.created_cars.append(new_car)

    def move(self):
        """
        Move the cars
        by given  STEP_INCREMENT
        """
        for car in self.created_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        """
        speed up the cars
        """
        self.car_speed += STEP_INCREMENT
