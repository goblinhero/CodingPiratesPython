import pygame

class Fjende(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Fjende, self).__init__(*groups)
        self.changeSpeed()
        self.image = grafik[1]
        self.rect = pygame.rect.Rect((450,240), self.image.get_size())
        self.moving = 1 #1 = Højre, -1 = Venstre
    def changeSpeed(self):
        self.speed = random.randint(1,8)
    def update(self, dt, game):
        self.rect.x += self.moving*self.speed
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.moving *= -1 #Skift retning
            self.changeSpeed()
