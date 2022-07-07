"""
Module containing the Paddle class.
"""

# Imports
from turtle import Turtle

# Constants
PADDLE_SEGMENTS = 5
PADDLE_SEGMENT_SIZE = 20
PADDLE_SEGMENT_MULTIPLIER = 1


# Class
class Paddle(Turtle):
    """
    Paddle class from which to instantiate Paddle objects.  It inherits from the Turtle class.
    """
    def __init__(self, name, colour):
        """
        Upon instantiation an object is assigned, hideturtle, penup, shape, color, and segments attributes.
        """
        super().__init__()
        self.hideturtle()
        self.name = name
        self.color(colour)
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=10, stretch_len=1)

    def spawn(self, position):
        """
        Method that moves the instantiated Paddle object to a position and makes it visible.
        """
        self.goto(position)
        self.showturtle()

    def move_up(self):
        """
        Method that moves the Paddle object up on the screen up to the court boundary.

        It does so by moving the Paddle object up 20 units on the y-axis until the y-axis value reaches 320.
        Then it stops.
        """
        if self.ycor() <= 280:
            self.goto((self.xcor(), self.ycor() + 20))

    def move_down(self):
        """
        Method that moves the Paddle object down on the screen up to the court boundary.

        It does so by moving the Paddle object down 20 units on the y-axis until the y-axis value reaches -320.
        Then it stops.
        """
        if self.ycor() >= -280:
            self.goto((self.xcor(), self.ycor() - 20))
