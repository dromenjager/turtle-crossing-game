from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Create the player
    turtle object
    """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("sky blue")
        self.penup()
        self.seth(90)
        self.goto_start()

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        """
        Move the turtle
        forward
        """
        ycor = self.ycor() + MOVE_DISTANCE
        self.goto((self.xcor(), ycor))

    def detect_win(self):
        """
        Detect player crossed
        screen
        """
        if self.ycor() > 280:
            return True
        else:
            return False
