# Imports
from turtle import Screen   # Turtle Screen class
from time import sleep      # sleep() from time speeds up or slows down time.
from random import randint  # randint() generates a random number from a range of two numbers given
from net import Net
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# Play background music as a loop.
mixer.music.load("background.wav")
mixer.music.play(-1)

# Create a sound object for a paddle strike.
paddle_hit = mixer.Sound("paddle_beep.wav")

# Setup screen.
screen = Screen()
screen.setup(width=1440, height=800)
screen.bgcolor("dark green")
screen.tracer(0)

# Create net.
net = Net()
net.setup_net(10, 380)  # Where (x, y) represents desired dash length, and y-coordinate for start of net.

# Instantiate scoreboards.
scoreboard = Scoreboard()
p1_scoreboard = Scoreboard()
p2_scoreboard = Scoreboard()

# Create score counters.
p1_score = 0
p2_score = 0

# Instantiate paddles.
p1 = Paddle("Nico", "orange")   # Where (x, y) are player name and paddle colour.
p2 = Paddle("Adri", "cyan")     # Where (x, y) are player name and paddle colour.

# Define scoreboard positions
p1_scoreboard_position = (-120, 340)    # x-coordinate and y-coordinate for position.
p2_scoreboard_position = (120, 340)     # x-coordinate and y-coordinate for position.
game_over_scoreboard_position = (0, -80)    # x-coordinate and y-coordinate for position.

# Display scoreboards.
p1_scoreboard.create(p1_scoreboard_position, p1, p1_score)
p2_scoreboard.create(p2_scoreboard_position, p2, p2_score)

# Draw paddles on screen.
p1.spawn((-700, 0))    # Where (x, y) is position for centre of paddle.
p2.spawn((700, 0))     # Where (x, y) is position for centre of paddle.

# Instantiate game ball.
ball = Ball()

# Update screen.
screen.update()

# Set game starting player as p1.
starting_player = p1

# Set score with which to win game.
score_to_win = 10

# Set rally length at which to speed up the ball.
speed_up = 2

# Start listening for key presses.
screen.listen()
screen.onkeypress(p1.move_up, "q")  # 'q' key moves p1 paddle up.
screen.onkeypress(p1.move_down, "a")    # 'a' key moves p1 paddle up.
screen.onkeypress(p2.move_up, "p")  # 'p' key moves p1 paddle up.
screen.onkeypress(p2.move_down, "l")    # 'l' key moves p1 paddle up.

# Start game over loop.
game_over = False
while not game_over:

    # Start rally length counter.
    rally_length = 0

    # Check if either player's score is enough to win the game.
    if p1_score == score_to_win:
        game_over = True
        break
    elif p2_score == score_to_win:
        game_over = True
        break

    # Check which player is starting or has scored previous goal and set a random ball heading in opposite direction.
    if starting_player == p1:
        ball_heading = randint(0, 45)
    else:
        ball_heading = randint(135, 180)

    # Kick off ball.
    ball.kick_off(ball_heading)

    # Set starting match delay.
    time_delay = 0.05

    # Start goal loop.
    goal = False
    while not goal:

        # Edit game time.
        sleep(time_delay)
        screen.update()

        # Start ball moving.
        ball.move()

        # Detect wall collisions and bounce ball.  Walls set to -380 and 380 on the y-axis.
        if ball.ycor() >= 380 or ball.ycor() <= -380:
            ball.setheading(360 - ball.heading())

        # Detect paddle 1 collision by comparing xcor and ycor of ball and paddle.  Bounce ball if True.
        if p1.xcor() + 40 > ball.xcor() and abs(ball.ycor() - p1.ycor()) < 100:
            paddle_hit.play()
            ball.setheading(180 - ball.heading())
            rally_length += 1
            # Check if rally length speed up value reached.  Increase ball speed if True.
            if rally_length % speed_up == 0:
                time_delay *= 0.75

        # Detect paddle 2 collision by comparing xcor and ycor of ball and paddle.  Bounce ball if True.
        if p2.xcor() - 40 < ball.xcor() and abs(ball.ycor() - p2.ycor()) < 100:
            paddle_hit.play()
            ball.setheading(180 - ball.heading())
            rally_length += 1
            # Check if rally length speed up value reached.  Increase ball speed if True.
            if rally_length % speed_up == 0:
                time_delay *= 0.75

        # Detect if p1 has scored a goal by checking if ball x-coordinate is greater than 780.
        if ball.xcor() > 700:
            p1_score += 1
            p1_scoreboard.clear()
            p1_scoreboard.create(p1_scoreboard_position, p1, p1_score)
            starting_player = p1
            goal = True

        # Detect if p2 has scored a goal by checking if ball x-coordinate is less than -780.
        if ball.xcor() < -700:
            p2_score += 1
            p2_scoreboard.clear()
            p2_scoreboard.create(p2_scoreboard_position, p2, p2_score)
            starting_player = p2
            goal = True

# Clear net and scoreboards from screen.
net.clear()
p1_scoreboard.clear()
p2_scoreboard.clear()
# Write game over scoreboard.
scoreboard.game_over(game_over_scoreboard_position, p1, p1_score, p2, p2_score)
screen.exitonclick()
