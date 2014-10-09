import pygame
from spiller import Spiller
from fjende import Fjende
class Spil(object):
    def main(self,screen):
        clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.player = Spiller(self.sprites)
        self.walls = pygame.sprite.Group()
        self.playerWon = False
        for x in range(0, 640, 32):
            for y in range(0, 480, 32):
                if x in (0,640-32) or y in (0, 480-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = grafik[2]
                    wall.rect = pygame.rect.Rect((x,y), wall.image.get_size())
        self.sprites.add(self.walls)
        self.enemies = pygame.sprite.Group()
        for x in range(0,antal_fjender):
            self.addEnemy()
        while 1:
            if self.playerWon:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            dt = clock.tick(30)/1000
            self.sprites.update(dt, self)
            screen.fill((255,255,255))
            self.sprites.draw(screen)
            pygame.display.flip()
    def addEnemy(self):
        enemy = Fjende(self.enemies)
        self.enemies.add(enemy)
        self.sprites.add(enemy)
