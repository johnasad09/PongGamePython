# Import necessary modules
from turtle import Turtle

class Scoreboard(Turtle):
    """
    Manages the scoring display for the Pong game.
    Inherits from Turtle class to display text on screen and tracks
    scores for both left and right players with classic Pong styling.
    """

    def __init__(self):
        """Initialize the scoreboard with starting scores and display configuration."""
        super().__init__()  # Initialize parent Turtle class
        
        # Display configuration
        self.FONT = ("Courier", 50, "normal")  # Large, bold font for clear score visibility
        self.color("white")    # White text color (visible on black background)
        self.penup()          # Don't draw lines when moving
        self.hideturtle()     # Hide the turtle cursor/shape
        
        # Score tracking variables
        self.l_score = 0      # Left player's score (starts at 0)
        self.r_score = 0      # Right player's score (starts at 0)
        
        # Display initial scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Refresh the scoreboard display with current scores for both players.
        Clears previous text and writes updated scores at their respective positions.
        Uses classic Pong layout with scores positioned above each side of the court.
        """
        self.clear()  # Remove all previous text from screen
        
        # Display left player's score
        self.goto(-100, 200)  # Move to left side, top of screen
        self.write(self.l_score, align="center", font=self.FONT)
        
        # Display right player's score  
        self.goto(100, 200)   # Move to right side, top of screen
        self.write(self.r_score, align="center", font=self.FONT)

    def l_point(self):
        """
        Award a point to the left player and update the display.
        Called when the ball goes off the right edge (right player misses).
        """
        self.l_score += 1         # Increment left player's score
        self.update_scoreboard()  # Refresh display with new score

    def r_point(self):
        """
        Award a point to the right player and update the display.
        Called when the ball goes off the left edge (left player misses).
        """
        self.r_score += 1         # Increment right player's score
        self.update_scoreboard()  # Refresh display with new score
