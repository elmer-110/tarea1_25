from character import Character

class Opponent(Character):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.is_star = False
        

    def move(self):
        self.y += 2
        