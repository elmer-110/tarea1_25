# character.py
from entity import Entity
from shot import Shot

class Character(Entity):
    def __init__(self, x, y, image, lives=1):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def shoot(self, shot_img):
        return Shot(self.x + 20, self.y, shot_img)

    def collide(self, shot):
        return self.x < shot.x < self.x + 50 and self.y < shot.y < self.y + 50
