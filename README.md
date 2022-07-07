# 100 Days of Python Code

## Project 22: Pong Game

Create a clone of the classic Atari pong game.
This version of the game is a 2 player clone.

### Rules

* Each player is represented by a paddle at either end of the court.
* Player 1 can move their paddle up and down using the 'q' and 'a' keys respectively.
* Player 2 can move their paddle up and down using the 'p' and 'l' keys respectively.
* Once the game is started a red ball is randomly fired onto the court.
* The player's must avoid the ball passing their paddles by hitting and bouncing back in the opposite direction.
* A point is scored when the ball gets past a player's paddle.
* If no goal is scored and a rally length reaches 10 then the ball speed is increased.
* If no goal continues to be scored the ball speed will be increased every additional 10 rally points.

To play the program run main.py

The match duration and rally value to speed up the ball can be modified within main.py under the
`score_to_win` and `speed up` variables.