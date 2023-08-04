import random

class Apple:
    def __init__(self, position: tuple = (10, 10)):
        self.position = position

    def generate_new_position(self):
        self.position = (random.randint(0, 20), random.randint(0, 20))
