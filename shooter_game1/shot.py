from entity import Entity

class Shot(Entity):
    def move(self):
        self.y -= 10

    def hit_target(self, target):
        return target.collide(self)