import random

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.bullet_position = random.randint(1, 6)
        self.current_postion = 1
        self.alive = True

    def shot(self):
        if not self.alive:
            return "game over"
        
        if self.current_postion == self.bullet_position:
            self.alive = False
            return "boom"
        else:
            self.current_postion += 1
            return 'empty'