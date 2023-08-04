import random

class Snake:
    def __init__(self, length: int, direction: str = 'right'):
        self.length = length
        self.direction = direction
        self.body = [(10, 10 + i) for i in range(length)]

    def move(self):
        head = self.body[0]
        if self.direction == 'up':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'down':
            new_head = (head[0] + 1, head[1])
        elif self.direction == 'left':
            new_head = (head[0], head[1] - 1)
        else:  # self.direction == 'right'
            new_head = (head[0], head[1] + 1)

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.length += 1
        tail = self.body[-1]
        if self.direction == 'up':
            new_tail = (tail[0] + 1, tail[1])
        elif self.direction == 'down':
            new_tail = (tail[0] - 1, tail[1])
        elif self.direction == 'left':
            new_tail = (tail[0], tail[1] + 1)
        else:  # self.direction == 'right'
            new_tail = (tail[0], tail[1] - 1)

        self.body.append(new_tail)

    def check_collision(self, position):
        return position in self.body
