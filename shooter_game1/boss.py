from opponent import Opponent
from shot import Shot

class Boss(Opponent):
    def move(self):
        self.y += 4

    def special_attack(self, shot_img):
        return Shot(self.x + 20, self.y, shot_img)