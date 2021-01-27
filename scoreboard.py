from turtle import Turtle


FONT = ("Courier", 24, "bold")
ALIGN = "center"


class ScoreBoard(Turtle):
    """
    Manage scores for the game
    """

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto((-250, 250))
        self.write(f"LEVEL {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        New message for game-over
        """
        self.goto(0.0, 0.0)
        self.write(
            "          Game Over\nclick anywhere to close the window",
            align="center",
            font=FONT,
        )
