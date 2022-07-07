"""
Module containing the Net class.
"""

# Imports
from turtle import Turtle


class Net(Turtle):
    """
    Net class from which to instantiate Net objects.  It inherits from the Turtle class.
    """
    def __init__(self):
        """
        Upon instantiation the Net object is assigned attributes: hideturtle(), speed(), turtlesize(), shape(),
        color(), pensize(), and penup().
        """
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.turtlesize(1)
        self.shape("square")
        self.color("white")
        self.pensize(6)
        self.penup()

    def setup_net(self, mark_length, y_cor):
        """
        Method that draws a net across the center of the screen from top to bottom with the Net object.

        Where 'mark_length' is a user defined value for the length of each dash, and in turn the accompanying gap.
        Where 'y_cor' is the y-axis value for where the net is supposed to start at the top of the screen.
        """
        x_pos = 0
        y_pos = y_cor
        self.goto((x_pos, y_pos))
        self.setheading(270)
        for n in range(int(y_cor / mark_length)):
            self.pendown()
            self.forward(mark_length)
            self.penup()
            self.forward(mark_length)
