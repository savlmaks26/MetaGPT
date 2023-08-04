import curses
import time
from snake import Snake
from apple import Apple

class Game:
    def __init__(self, stdscr, length, speed):
        self.stdscr = stdscr
        self.snake = Snake(length)
        self.apple = Apple((10, 10))
        self.score = 0
        self.speed = speed
        self.running = False

    def start_game(self):
        self.running = True

    def end_game(self):
        self.running = False

    def update_game(self):
        # Move the snake
        self.snake.move()

        # Check if the snake has collided with the apple
        if self.snake.check_collision(self.apple.position):
            # Increase the score
            self.score += 1

            # Grow the snake
            self.snake.grow()

            # Generate a new position for the apple
            self.apple.generate_new_position()

        # Check if the snake has collided with itself
        if self.snake.check_collision(self.snake.body[0]):
            self.end_game()

    def draw_game(self):
        # Clear the screen
        self.stdscr.clear()

        # Draw the snake
        for segment in self.snake.body:
            self.stdscr.addch(segment[0], segment[1], '#')

        # Draw the apple
        self.stdscr.addch(self.apple.position[0], self.apple.position[1], '@')

        # Draw the score
        self.stdscr.addstr(0, 0, f'Score: {self.score}')

        # Refresh the screen
        self.stdscr.refresh()

        # Control the game speed
        time.sleep(1 / self.speed)
