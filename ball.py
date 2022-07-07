"""
Module containing the Ball class.
"""

# Imports
from turtle import Turtle
from random import randrange


class Ball(Turtle):
    """
    Ball class from which to instantiate ball objects.  It inherits from the Turtle class.
    """
    def __init__(self):
        """
        Upon instantiation a Ball object is assigned the attributes: shape(), color() and penup().
        """
        super().__init__()
        self.shape("circle")
        self.color("bisque")
        self.penup()

    def kick_off(self, heading):
        """
        Method that sends the Ball object to a random y-coordinate along the y-axis and then gives it a random heading.
        Where heading is a randomly generated value in main.py.
        """
        self.goto(0, randrange(-360, 360, 60))
        self.setheading(heading)

    def move(self):
        """
        Method that moves the ball forward by 20 on the screen.
        """
        self.forward(20)

