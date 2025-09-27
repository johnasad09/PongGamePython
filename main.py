# Import necessary modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# === GAME SETUP ===
# Create and configure the game screen
screen = Screen()
screen.bgcolor("black")                 # Set background color to black (classic Pong style)
screen.setup(width=800, height=600)    # Set screen dimensions (800x600 pixels)
screen.title("Pong Game")               # Set window title
screen.tracer(0)                        # Turn off animation for smoother gameplay

# === GAME OBJECTS INITIALIZATION ===
# Create paddles at opposite sides of the screen
r_paddle = Paddle((350, 0))     # Right paddle positioned at x=350, y=0 (right side)
l_paddle = Paddle((-350, 0))    # Left paddle positioned at x=-350, y=0 (left side)
ball = Ball()                   # Create ball object (starts at center)

# Create scoreboard to track points for both players
scoreboard = Scoreboard()

# === CONTROLS SETUP ===
# Set up keyboard controls for both paddles
screen.listen()                         # Enable screen to listen for key presses
# Right paddle controls (arrow keys)
screen.onkey(r_paddle.go_up, "Up")      # Up arrow moves right paddle up
screen.onkey(r_paddle.go_down, "Down")  # Down arrow moves right paddle down
# Left paddle controls (WASD keys)
screen.onkey(l_paddle.go_up, "w")       # W key moves left paddle up
screen.onkey(l_paddle.go_down, "s")     # S key moves left paddle down

# === MAIN GAME LOOP ===
game_on = True  # Game state flag
while game_on:
    time.sleep(ball.ball_speed)  # Control game speed based on ball's current speed
    screen.update()              # Refresh screen to show all updates
    ball.move()                  # Move ball in its current direction

    # === WALL COLLISION DETECTION ===
    # Check if ball hits top or bottom walls (y-coordinates ±280)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Reverse ball's vertical direction

    # === PADDLE COLLISION DETECTION ===
    # Check collision with right paddle (ball moving right, x > 320)
    # or left paddle (ball moving left, x < -320)
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()  # Reverse ball's horizontal direction and increase speed

    # === SCORING SYSTEM ===
    # Ball missed by right paddle (goes off right edge)
    if ball.xcor() > 380:           # Ball passed right boundary
        ball.reset_position()       # Reset ball to center for next round
        scoreboard.l_point()        # Award point to left player

    # Ball missed by left paddle (goes off left edge)
    if ball.xcor() < -380:          # Ball passed left boundary
        ball.reset_position()       # Reset ball to center for next round
        scoreboard.r_point()        # Award point to right player

# Keep the screen open until clicked
screen.exitonclick()
