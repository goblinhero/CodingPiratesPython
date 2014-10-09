import pygame

class Spiller(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Spiller, self).__init__(*groups)
        self.image = grafik[0]
        self.rect = pygame.rect.Rect((320,240),self.image.get_size())
        self.dy = 0
        self.score = 0

    def update(self, dt, game):
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        if key[pygame.K_SPACE]:
            self.dy = -500
        self.dy = min(400, self.dy+40)
        self.rect.y += self.dy * dt
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
        for cell in pygame.sprite.spritecollide(self, game.enemies, True):
            self.score += point_for_fjende
            print("Point:",self.score)
        if len(game.enemies) == 0:
            print("Du vandt!")
            game.playerWon = True
