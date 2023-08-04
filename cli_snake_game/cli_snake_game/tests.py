import unittest
from snake import Snake
from apple import Apple
from scoreboard import Scoreboard

class TestSnake(unittest.TestCase):
    def test_move(self):
        snake = Snake(5)
        snake.move()
        self.assertEqual(snake.body[0], (10, 16))

    def test_grow(self):
        snake = Snake(5)
        snake.grow()
        self.assertEqual(snake.length, 6)
        self.assertEqual(snake.body[-1], (10, 9))

    def test_check_collision(self):
        snake = Snake(5)
        self.assertTrue(snake.check_collision((10, 15)))
        self.assertFalse(snake.check_collision((0, 0)))

class TestApple(unittest.TestCase):
    def test_generate_new_position(self):
        apple = Apple()
        position_before = apple.position
        apple.generate_new_position()
        self.assertNotEqual(apple.position, position_before)

class TestScoreboard(unittest.TestCase):
    def test_load_and_save_scores(self):
        scoreboard = Scoreboard('test_scores.json')
        scoreboard.load_scores()
        self.assertEqual(scoreboard.scores, [])
        scoreboard.update_score(5)
        scoreboard.save_scores()
        scoreboard.load_scores()
        self.assertEqual(scoreboard.scores, [5])

if __name__ == '__main__':
    unittest.main()
