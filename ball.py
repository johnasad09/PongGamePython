# Import necessary modules
from turtle import Turtle

class Ball(Turtle):
    """
    Represents the ball in the Pong game that bounces between paddles and walls.
    Inherits from Turtle class to create a visual ball object with physics-based
    movement, collision responses, and dynamic speed changes.
    """

    def __init__(self):
        """Initialize the ball with its appearance, movement vectors, and starting speed."""
        super().__init__()  # Initialize parent Turtle class
        
        # Configure ball appearance
        self.shape("circle")    # Set ball shape to circle (classic Pong ball)
        self.color("white")     # Set ball color to white (visible on black background)
        self.penup()           # Don't draw lines when moving
        
        # Movement vectors (pixels per move)
        self.x_move = 10       # Horizontal movement speed (positive = right, negative = left)
        self.y_move = 10       # Vertical movement speed (positive = up, negative = down)
        
        # Game speed control
        self.ball_speed = 0.1  # Time delay between moves (lower = faster ball)

    def move(self):
        """
        Move the ball by its current movement vectors.
        Called continuously in the main game loop to create ball motion.
        """
        # Calculate new position based on current position and movement vectors
        new_x = self.xcor() + self.x_move  # New x position
        new_y = self.ycor() + self.y_move  # New y position
        self.goto(new_x, new_y)           # Move ball to new position

    def bounce_y(self):
        """
        Reverse the ball's vertical direction (collision with top/bottom walls).
        Also slightly increases ball speed to add progressive difficulty.
        """
        self.y_move *= -1        # Reverse vertical direction (up becomes down, down becomes up)
        self.ball_speed *= 0.9   # Decrease delay time = increase speed (10% faster)

    def bounce_x(self):
        """
        Reverse the ball's horizontal direction (collision with paddles).
        Called when ball hits either the left or right paddle.
        """
        self.x_move *= -1        # Reverse horizontal direction (left becomes right, right becomes left)

    def reset_position(self):
        """
        Reset the ball to center position and restart with fresh settings.
        Called after a point is scored (when ball goes off either side).
        Changes direction so ball moves toward the player who just scored.
        """
        self.goto(0, 0)          # Move ball back to center of screen
        self.ball_speed = 0.1    # Reset speed to initial value
        self.bounce_x()          # Reverse horizontal direction for next round
