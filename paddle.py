# Import necessary modules
from turtle import Turtle

class Paddle(Turtle):
    """
    Represents a paddle in the Pong game that players control to hit the ball.
    Inherits from Turtle class to create a visual paddle object that can move
    up and down on the screen while maintaining its horizontal position.
    """

    def __init__(self, position):
        """
        Initialize the paddle with its appearance and position.
        
        Args:
            position (tuple): (x, y) coordinates where the paddle should be placed
                             Typically (-350, 0) for left paddle or (350, 0) for right paddle
        """
        super().__init__()  # Initialize parent Turtle class
        
        # Configure paddle appearance
        self.shape("square")    # Use square shape as base
        self.color("white")     # Set paddle color to white (visible on black background)
        
        # Reshape paddle to be tall and narrow (classic Pong paddle dimensions)
        self.shapesize(stretch_wid=5, stretch_len=1)  # 5x taller, same width (100x20 pixels)
        
        self.penup()           # Don't draw lines when moving
        self.goto(position)    # Move paddle to specified starting position

    def go_up(self):
        """
        Move the paddle up by 20 pixels.
        Called when player presses the assigned "up" key.
        Maintains the paddle's x-coordinate while increasing y-coordinate.
        """
        new_y = self.ycor() + 20        # Calculate new y position (20 pixels higher)
        self.goto(self.xcor(), new_y)   # Move to new position (same x, new y)

    def go_down(self):
        """
        Move the paddle down by 20 pixels.
        Called when player presses the assigned "down" key.
        Maintains the paddle's x-coordinate while decreasing y-coordinate.
        """
        new_y = self.ycor() - 20        # Calculate new y position (20 pixels lower)
        self.goto(self.xcor(), new_y)   # Move to new position (same x, new y)
