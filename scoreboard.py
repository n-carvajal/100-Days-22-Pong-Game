"""
Module containing the Scoreboard class.
"""

# Imports
from turtle import Turtle


class Scoreboard(Turtle):
    """
    Scoreboard class from which to instantiate Scoreboard objects.  It inherits from the Turtle class.
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def create(self, position, player, score):
        """
        Method that writes a Scoreboard object at position given position.

        Where 'position' is a user defined tuple (x, y) and 'score' is a user_defined variable in main.py.
        """
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(f"{player.name}: {score}", True, "center", ('Arial', 20, 'normal'))

    def game_over(self, position, player_1, score_1, player_2, score_2):
        """
        Method that writes a Scoreboard object at position given position.

        Where:
        'score_1' is p1_score from main.py
        'score_2' is p1_score from main.py
        """
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(f"GAME OVER.\n\n{player_1.name}: {score_1}\n{player_2.name}: {score_2}", True, "center",
                   ('Arial', 40, 'normal'))


