## main.py
import argparse
import curses
from game import Game
from scoreboard import Scoreboard

def main(stdscr, args):
    # Create a new game
    game = Game(stdscr, args.length, args.speed)
    
    # Create a scoreboard
    scoreboard = Scoreboard('scores.json')
    
    # Load the high scores
    scoreboard.load_scores()
    
    # Start the game
    game.start_game()
    
    # Main game loop
    while game.running:
        # Update the game
        game.update_game()
        
        # Draw the game
        game.draw_game()
        
        # Update the score
        scoreboard.update_score(game.score)
        
        # Save the high scores
        scoreboard.save_scores()
    
    # End the game
    game.end_game()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI Snake Game')
    parser.add_argument('--length', type=int, default=5, help='Initial length of the snake')
    parser.add_argument('--speed', type=int, default=1, help='Speed of the snake')
    args = parser.parse_args()
    
    # Start the game
    curses.wrapper(main, args)
