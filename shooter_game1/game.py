import pygame
import random
from player import Player
from opponent import Opponent
from boss import Boss
from shot import Shot
WIDTH, HEIGHT = 800, 600
player_img = pygame.Surface((50, 50)); player_img.fill((0, 255, 0))
enemy_img = pygame.Surface((50, 50)); enemy_img.fill((255, 0, 0))
shot_img = pygame.Surface((10, 20)); shot_img.fill((255, 255, 0))
boss_img = pygame.Surface((100, 100)); boss_img.fill((0, 0, 255))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
class Game:
    def __init__(self):
        self.player = Player(400, 500, player_img)
        self.opponents = [Opponent(random.randint(0, WIDTH-50), -50, enemy_img)]
        self.shots = []
        self.enemy_shots = []
        self.boss = None
        self.score = 0
        self.is_running = True

    def start(self):
        while self.is_running:
            screen.fill((0, 0, 0))
            self.update()
            pygame.display.flip()
            clock.tick(60)

    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.shots.append(self.player.shoot(shot_img))

        self.player.move(keys)
        self.player.draw(screen)

        for opponent in self.opponents[:]:
            opponent.move()
            opponent.draw(screen)
            if random.randint(0, 100) < 1:
                self.enemy_shots.append(opponent.shoot(shot_img))

        if self.boss:
            self.boss.move()
            self.boss.draw(screen)
            if random.randint(0, 50) < 2:
                self.enemy_shots.append(self.boss.special_attack(shot_img))

        for shot in self.shots[:]:
            shot.move()
            shot.draw(screen)
            for opponent in self.opponents[:]:
                if shot.hit_target(opponent):
                    opponent.is_star = True
                    self.opponents.remove(opponent)
                    self.shots.remove(shot)
                    self.player.score += 1
                    if self.player.score == 5:
                        self.boss = Boss(300, 0, boss_img)
                    break

        for e_shot in self.enemy_shots[:]:
            e_shot.y += 7
            e_shot.draw(screen)
            if e_shot.hit_target(self.player):
                self.player.lives -= 1
                self.enemy_shots.remove(e_shot)
                if self.player.lives <= 0:
                    self.end_game("Derrota")
                    return

        self.draw_ui()

        if self.boss and self.boss.is_star:
            self.end_game("Victoria")

    def draw_ui(self):
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {self.player.lives}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

    def end_game(self, result):
        font = pygame.font.SysFont(None, 60)
        msg = font.render(result, True, (255, 255, 0))
        screen.blit(msg, (WIDTH//2 - 100, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        self.is_running = False
